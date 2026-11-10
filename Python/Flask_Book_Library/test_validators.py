import pytest
from project.books.views import validate_no_html

def test_validate_valid_text():
    """Test poprawnego wariantu danych."""
    assert validate_no_html("Wiedźmin") == "Wiedźmin"

def test_validate_xss_script_injection():
    """Test odrzucenia znacznika <script>."""
    with pytest.raises(ValueError):
        validate_no_html("<script>alert('ABC')</script>")

def test_validate_xss_img_onerror():
    """Test odrzucenia tagu HTML ze zdarzeniem JavaScript."""
    with pytest.raises(ValueError):
        validate_no_html("<img src=x onerror=alert(1)>")