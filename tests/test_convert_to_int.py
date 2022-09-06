import pytest
from pytest_practice.convert_to_int import convert_to_int

def test_on_string_with_one_comma():
    return_value = convert_to_int("2,081")
    assert isinstance(return_value, int)
    assert return_value == 2081

def test_with_int():
    return_value = convert_to_int(2081)
    assert isinstance(return_value, int)
    assert return_value == 2081


def test_wit_invalid():
    with pytest.raises(TypeError):
        return_value = convert_to_int(2081.1)
    with pytest.raises(TypeError):
        return_value = convert_to_int([1234,1234])

# will make an example with TDD latter

