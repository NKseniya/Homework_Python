import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected_output", [
    (" Skypro", "Skypro"),
    ("Hel lo", "Hel lo"),
])
def test_trim_positive(input_str, expected_output):
    string_utils = StringUtils()
    result = string_utils.trim(input_str)
    assert result == expected_output


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected_output", [
    ("", "")
])
def test_trim_negative(input_str, expected_output):
    assert string_utils.trim("") == ""


@pytest.mark.positive
def test_contains_positive():
    assert string_utils.contains("Skypro", "k") is True


@pytest.mark.negative
def test_contains_negativ():
    assert string_utils.contains("Skypro", "1") is False


@pytest.mark.positive
def test_delete_symbol_positive():
    assert string_utils.delete_symbol("Skypro", "k") == "Sypro"


@pytest.mark.negative
def test_delete_symbol_negative():
    assert string_utils.delete_symbol("Skypro", "1") == "Skypro"
