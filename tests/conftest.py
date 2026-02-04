"""Shared test fixtures."""

import pytest


@pytest.fixture
def sample_html_content() -> str:
    """Sample HTML content for testing classifiers."""
    return """
    <!DOCTYPE html>
    <html>
    <head><title>Test Page - A Comprehensive Example</title></head>
    <body>
        <h1>Welcome to the Test Page</h1>
        <p>This is a paragraph with actual content that should be detected as real HTML.
        The content here is substantial enough to pass the length threshold checks.</p>
        <p>Another paragraph with more substantive text to ensure the classifier sees
        this as real content. We need enough text to exceed 500 characters total.</p>
        <p>Here is additional content to make sure we have enough text in this HTML
        document. This paragraph adds more words and characters to the total count.</p>
        <p>Finally, a closing paragraph with some more text content. This should now
        be well over the 500 character threshold that triggers short_content detection.</p>
    </body>
    </html>
    """


@pytest.fixture
def js_rendered_content() -> str:
    """Sample JS-rendered garbage content."""
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <script src="/_next/static/chunks/webpack-123.js"></script>
    </head>
    <body>
        <div id="__next"></div>
        <script>window.__NEXT_DATA__ = {};</script>
    </body>
    </html>
    """


@pytest.fixture
def loading_content() -> str:
    """Sample loading spinner content."""
    return """
    <html>
    <body>
        <div class="spinner">Loading...</div>
        <noscript>Please enable JavaScript to view this page.</noscript>
    </body>
    </html>
    """


@pytest.fixture
def short_content() -> str:
    """Very short content that indicates JS rendering."""
    return "Loading..."
