---
name: TDD Workflow
description: This skill should be used when the user is working with test files (test_*.py, *_test.py, conftest.py, tests/ directory), mentions "TDD", "test-driven development", "red-green-refactor", "write tests first", "make tests pass", or needs guidance on behavior-focused testing, test assertions, or the TDD cycle.
version: 1.0.0
---

# Test-Driven Development Workflow

## The Red-Green-Refactor Cycle

TDD follows a strict discipline:

1. **RED**: Write a failing test first
   - Define expected behavior before implementation
   - Test should fail because the code doesn't exist yet
   - Focus on WHAT the code should do, not HOW

2. **GREEN**: Write minimal code to pass the test
   - Implement just enough to make the test pass
   - Don't over-engineer or add extra features
   - Use the `implementer` agent for this phase

3. **REFACTOR**: Clean up while keeping tests green
   - Improve code structure and readability
   - Remove duplication
   - Tests must still pass after refactoring

## Behavior-Focused Testing

**Test the WHAT, not the HOW.**

### Good Tests (Behavior-Focused)

```python
def test_user_creation_returns_valid_user():
    """Test that creating a user returns expected data."""
    user = create_user(name="Alice", email="alice@example.com")

    assert user["name"] == "Alice"
    assert user["email"] == "alice@example.com"
    assert "id" in user  # Has an ID, don't care how it's generated


def test_invalid_email_raises_error():
    """Test that invalid emails are rejected."""
    with pytest.raises(ValidationError) as exc:
        create_user(name="Bob", email="not-an-email")

    assert "email" in str(exc.value).lower()
```

### Bad Tests (Implementation-Focused)

```python
# BAD: Tests internal implementation details
def test_user_creation_calls_database():
    with patch('app.db.insert') as mock_insert:
        create_user(name="Alice", email="alice@example.com")
        mock_insert.assert_called_once_with(
            "users",
            {"name": "Alice", "email": "alice@example.com"}
        )

# BAD: Tests specific SQL query
def test_user_query_format():
    query = build_user_query(user_id=1)
    assert query == "SELECT * FROM users WHERE id = 1"
```

### Why This Matters

- **Behavior tests** survive refactoring
- **Implementation tests** break when internals change
- Tests should be a safety net, not a straitjacket

## Writing Effective Test Assertions

### Assert on Outputs

```python
# Good: Assert on the return value
result = calculate_total(items=[10, 20, 30])
assert result == 60

# Good: Assert on side effects that matter
send_email(to="user@example.com", subject="Hello")
assert len(outbox) == 1
assert outbox[0].to == "user@example.com"
```

### Assert on Behavior, Not State

```python
# Good: Test observable behavior
cart = ShoppingCart()
cart.add_item("apple", quantity=3)
assert cart.total_items == 3
assert cart.get_item_quantity("apple") == 3

# Bad: Test internal state
assert cart._items == {"apple": 3}  # Don't access private attributes
```

### Use Descriptive Assertion Messages

```python
assert user.is_active, f"Expected user {user.id} to be active after verification"
assert response.status_code == 200, f"Expected 200 but got {response.status_code}: {response.text}"
```

## Using the Implementer Agent

When you have failing tests and need implementation:

1. The `implementer` agent writes production code only
2. It **cannot** modify test files (enforced by design)
3. If tests can't pass due to test issues, it returns a detailed report

### When Tests Need Changes

If the implementer agent determines tests need modification, it will return a report including:
- What test failed and why
- Root cause analysis
- Proposed test modifications with code
- Behavioral expectations that should be tested

Review this report and decide whether to modify tests yourself.

## TDD Commands

- `/tdd:start <feature>` - Start a new feature with TDD workflow
- `/tdd:finish` - Complete workflow with quality checks

## Common Pitfalls

### Pitfall 1: Testing Implementation Details

```python
# Don't do this - tests internal method calls
def test_save_calls_serialize():
    obj = MyObject()
    with patch.object(obj, '_serialize') as mock:
        obj.save()
        mock.assert_called_once()
```

**Fix**: Test the observable result of `save()` instead.

### Pitfall 2: Over-Mocking

```python
# Don't mock everything
def test_process_with_all_mocks(mock_db, mock_cache, mock_logger, mock_validator):
    # This tests nothing useful
    pass
```

**Fix**: Use real objects where possible, mock only external services.

### Pitfall 3: Testing Trivial Code

```python
# Don't test getters/setters
def test_name_getter():
    user = User(name="Alice")
    assert user.name == "Alice"  # Trivial, adds no value
```

**Fix**: Focus tests on business logic and edge cases.

### Pitfall 4: Modifying Tests to Pass

When tests fail, resist the urge to "fix" the test. Ask:
- Is the test wrong, or is the implementation wrong?
- Does the test describe the correct expected behavior?
- If the test is wrong, WHY is it wrong?

## Quick Reference

| Phase | Do | Don't |
|-------|-----|-------|
| RED | Write test for expected behavior | Write implementation first |
| GREEN | Write minimal passing code | Over-engineer or add features |
| REFACTOR | Clean up, keep tests green | Change test expectations |

| Good Test | Bad Test |
|-----------|----------|
| Tests outputs | Tests internal calls |
| Survives refactoring | Breaks on implementation changes |
| Documents behavior | Documents implementation |
| Uses real objects | Over-mocks everything |
