"""Tests for core module."""

import pytest
from python_goods.core import hello


def test_hello_default():
    """Test hello function with default argument."""
    assert hello() == "Hello, World!"


def test_hello_with_name():
    """Test hello function with custom name."""
    assert hello("Python") == "Hello, Python!"
