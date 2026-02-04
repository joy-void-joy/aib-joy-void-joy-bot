"""Tests for aib.tools.cache."""

import asyncio

import pytest

from aib.tools.cache import TTLCache, api_cache, cached


class TestTTLCache:
    """Tests for the TTLCache class."""

    @pytest.mark.asyncio
    async def test_set_and_get(self) -> None:
        """Basic set and get works."""
        cache = TTLCache(default_ttl=300.0)
        await cache.set("key1", "value1")

        found, value = await cache.get("key1")

        assert found is True
        assert value == "value1"

    @pytest.mark.asyncio
    async def test_get_missing_key(self) -> None:
        """Get returns not found for missing keys."""
        cache = TTLCache(default_ttl=300.0)

        found, value = await cache.get("nonexistent")

        assert found is False
        assert value is None

    @pytest.mark.asyncio
    async def test_ttl_expiration(self) -> None:
        """Entries expire after TTL."""
        cache = TTLCache(default_ttl=0.05)  # 50ms TTL
        await cache.set("key1", "value1")

        # Should be found immediately
        found, _ = await cache.get("key1")
        assert found is True

        # Wait for expiration
        await asyncio.sleep(0.06)

        # Should be expired
        found, _ = await cache.get("key1")
        assert found is False

    @pytest.mark.asyncio
    async def test_custom_ttl_per_entry(self) -> None:
        """Custom TTL can be set per entry."""
        cache = TTLCache(default_ttl=300.0)
        await cache.set("short_lived", "value", ttl=0.05)
        await cache.set("long_lived", "value", ttl=300.0)

        await asyncio.sleep(0.06)

        short_found, _ = await cache.get("short_lived")
        long_found, _ = await cache.get("long_lived")

        assert short_found is False
        assert long_found is True

    @pytest.mark.asyncio
    async def test_max_size_eviction(self) -> None:
        """Oldest entries are evicted when max size is reached."""
        cache = TTLCache(default_ttl=300.0, max_size=3)

        await cache.set("key1", "value1")
        await asyncio.sleep(0.01)
        await cache.set("key2", "value2")
        await asyncio.sleep(0.01)
        await cache.set("key3", "value3")
        await asyncio.sleep(0.01)

        # This should evict key1 (oldest)
        await cache.set("key4", "value4")

        found1, _ = await cache.get("key1")
        found4, _ = await cache.get("key4")

        assert found1 is False  # Evicted
        assert found4 is True  # Newly added

    @pytest.mark.asyncio
    async def test_clear_removes_all(self) -> None:
        """clear removes all entries."""
        cache = TTLCache(default_ttl=300.0)
        await cache.set("key1", "value1")
        await cache.set("key2", "value2")

        await cache.clear()

        found1, _ = await cache.get("key1")
        found2, _ = await cache.get("key2")

        assert found1 is False
        assert found2 is False

    @pytest.mark.asyncio
    async def test_stats_tracking(self) -> None:
        """Stats track hits and misses."""
        cache = TTLCache(default_ttl=300.0)
        await cache.set("key1", "value1")

        # Hit
        await cache.get("key1")
        # Miss
        await cache.get("key2")
        # Hit
        await cache.get("key1")

        stats = cache.stats

        assert stats["hits"] == 2
        assert stats["misses"] == 1
        assert stats["hit_rate"] == pytest.approx(2 / 3)

    @pytest.mark.asyncio
    async def test_stats_size(self) -> None:
        """Stats report correct size."""
        cache = TTLCache(default_ttl=300.0)
        await cache.set("key1", "value1")
        await cache.set("key2", "value2")

        assert cache.stats["size"] == 2

    @pytest.mark.asyncio
    async def test_overwrite_existing_key(self) -> None:
        """Setting an existing key overwrites the value."""
        cache = TTLCache(default_ttl=300.0)
        await cache.set("key1", "original")
        await cache.set("key1", "updated")

        _, value = await cache.get("key1")

        assert value == "updated"

    @pytest.mark.asyncio
    async def test_stores_various_types(self) -> None:
        """Cache stores various data types."""
        cache = TTLCache(default_ttl=300.0)

        await cache.set("string", "hello")
        await cache.set("number", 42)
        await cache.set("list", [1, 2, 3])
        await cache.set("dict", {"a": 1})
        await cache.set("none", None)

        _, str_val = await cache.get("string")
        _, num_val = await cache.get("number")
        _, list_val = await cache.get("list")
        _, dict_val = await cache.get("dict")
        _, none_val = await cache.get("none")

        assert str_val == "hello"
        assert num_val == 42
        assert list_val == [1, 2, 3]
        assert dict_val == {"a": 1}
        assert none_val is None


class TestTTLCacheDecorator:
    """Tests for the TTLCache.cached() decorator."""

    @pytest.mark.asyncio
    async def test_caches_result(self) -> None:
        """Decorator caches function result."""
        cache = TTLCache(default_ttl=300.0)
        call_count = 0

        @cache.cached()
        async def expensive_func(x: int) -> int:
            nonlocal call_count
            call_count += 1
            return x * 2

        result1 = await expensive_func(5)
        result2 = await expensive_func(5)

        assert result1 == 10
        assert result2 == 10
        assert call_count == 1  # Only called once

    @pytest.mark.asyncio
    async def test_different_args_different_cache(self) -> None:
        """Different arguments produce different cache entries."""
        cache = TTLCache(default_ttl=300.0)
        call_count = 0

        @cache.cached()
        async def func(x: int) -> int:
            nonlocal call_count
            call_count += 1
            return x * 2

        await func(5)
        await func(10)
        await func(5)

        assert call_count == 2  # 5 and 10 are different keys

    @pytest.mark.asyncio
    async def test_kwargs_included_in_key(self) -> None:
        """Keyword arguments are included in cache key."""
        cache = TTLCache(default_ttl=300.0)
        call_count = 0

        @cache.cached()
        async def func(x: int, multiplier: int = 2) -> int:
            nonlocal call_count
            call_count += 1
            return x * multiplier

        await func(5, multiplier=2)
        await func(5, multiplier=3)
        await func(5, multiplier=2)

        assert call_count == 2  # multiplier=2 and multiplier=3 are different

    @pytest.mark.asyncio
    async def test_custom_ttl_in_decorator(self) -> None:
        """Custom TTL can be specified in decorator."""
        cache = TTLCache(default_ttl=300.0)
        call_count = 0

        @cache.cached(ttl=0.05)  # 50ms
        async def func() -> str:
            nonlocal call_count
            call_count += 1
            return "result"

        await func()
        await asyncio.sleep(0.06)
        await func()

        assert call_count == 2  # Called again after expiration

    @pytest.mark.asyncio
    async def test_preserves_function_metadata(self) -> None:
        """Decorator preserves function name and docstring."""
        cache = TTLCache(default_ttl=300.0)

        @cache.cached()
        async def documented() -> None:
            """This is documentation."""
            pass

        assert documented.__name__ == "documented"
        assert documented.__doc__ == "This is documentation."


class TestGlobalCacheDecorator:
    """Tests for the global @cached decorator."""

    @pytest.fixture(autouse=True)
    async def clear_cache(self) -> None:
        """Clear global cache before each test."""
        await api_cache.clear()

    @pytest.mark.asyncio
    async def test_uses_global_cache(self) -> None:
        """@cached decorator uses the global api_cache."""
        call_count = 0

        @cached()
        async def global_cached_func() -> str:
            nonlocal call_count
            call_count += 1
            return "result"

        await global_cached_func()
        await global_cached_func()

        assert call_count == 1

    @pytest.mark.asyncio
    async def test_custom_ttl(self) -> None:
        """@cached accepts custom TTL."""
        call_count = 0

        @cached(ttl=0.05)
        async def short_cache_func() -> str:
            nonlocal call_count
            call_count += 1
            return "result"

        await short_cache_func()
        await asyncio.sleep(0.06)
        await short_cache_func()

        assert call_count == 2


class TestCacheKeyGeneration:
    """Tests for cache key generation."""

    @pytest.mark.asyncio
    async def test_key_includes_function_name(self) -> None:
        """Different functions produce different keys."""
        cache = TTLCache(default_ttl=300.0)

        @cache.cached()
        async def func_a() -> str:
            return "a"

        @cache.cached()
        async def func_b() -> str:
            return "b"

        result_a = await func_a()
        result_b = await func_b()

        assert result_a == "a"
        assert result_b == "b"

    @pytest.mark.asyncio
    async def test_complex_args_handled(self) -> None:
        """Complex argument types are handled in key generation."""
        cache = TTLCache(default_ttl=300.0)
        call_count = 0

        @cache.cached()
        async def func(data: dict[str, int], items: list[str]) -> int:
            nonlocal call_count
            call_count += 1
            return sum(data.values()) + len(items)

        await func({"a": 1, "b": 2}, ["x", "y"])
        await func({"a": 1, "b": 2}, ["x", "y"])
        await func({"a": 1, "b": 3}, ["x", "y"])  # Different dict

        assert call_count == 2
