import pytest
from pytest_practice.convert_to_int import convert_to_int

class TestConvertToInt():

    ################### Normal arguments ############################

    def test_with_no_comma(self):
        actual = convert_to_int("756")
        # Complete the assert statement
        assert actual==756, "Expected: 756, Actual: {0}".format(actual)

    def test_with_one_comma(self):
        actual = convert_to_int("2,081")
        # Complete the assert statement
        assert actual==2081, "Expected: 2081, Actual: {0}".format(actual)

    def test_with_two_commas(self):
        actual = convert_to_int("1,034,891")
        # Complete the assert statement
        assert actual==1034891, "Expected: 1034891, Actual: {0}".format(actual)


    ################ Special arguments #############################

    def test_on_string_with_missing_comma(self):
        actual = convert_to_int("178100,301")
        assert actual is None, "Expected: None, Actual: {0}".format(actual)
        
    def test_on_string_with_incorrectly_placed_comma(self):
        # Assign to the actual return value for the argument "12,72,891"
        actual = convert_to_int("12,72,891")
        assert actual is None, "Expected: None, Actual: {0}".format(actual)
        
    def test_on_float_valued_string(self):
        actual = convert_to_int("23,816.92")
        # Complete the assert statement
        assert actual is None, "Expected: None, Actual: {0}".format(actual)
"""
def test_with_int(self):
    return_value = convert_to_int(2081)
    assert isinstance(return_value, int)
    assert return_value == 2081
"""
#####################  Bad arguments #########################
""" no bad arguments
def test_wit_invalid_type(self):
    with pytest.raises(TypeError):
        return_value = convert_to_int(2081.1)
    with pytest.raises(TypeError):
        return_value = convert_to_int([1234,1234])
"""

