# tests/test_security.py
import pytest
from unittest.mock import MagicMock
from apishield.static_analyzer import static_analysis
from apishield.dynamic_analyzer import dynamic_analysis, analyze_view

# Mock view function
@pytest.fixture
def mock_view():
    view = MagicMock()
    view.__name__ = "mock_view"
    return view

# Test static analysis function
def test_static_analysis(mock_view):
    result = static_analysis(mock_view)
    assert result is True, f"Static analysis failed for {mock_view.__name__}"

# Test dynamic analysis function
def test_dynamic_analysis():
    # Simulate a URL for testing
    url = "http://localhost:8000/test_view"
    result = dynamic_analysis(mock_view, url)
    assert result is None, "Dynamic analysis failed"

# Test combined static and dynamic analysis
def test_analyze_view(mock_view):
    url = "http://localhost:8000/test_view"
    result = analyze_view(mock_view, url)
    assert result is None, "Combined security analysis failed"

