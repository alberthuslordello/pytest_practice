import pytest
from pytest_practice.preprocessing_helpers import convert_to_int, row_to_list


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


class TestRowToList():
    def test_row_to_list(self):
        pass

    def test_for_clean_row(self):
        assert row_to_list("2,081\t314,942\n") == ["2,081", "314,942"]

    def test_for_missing_area(self):
        # edited to have a prettier pytest FAILED message
        # assert row_to_list(self"\t293,410\n") is None
        actual = row_to_list("\t293,410\n")
        expected = None
        message = ("row_to_list('\t293,410\n') "
                    "returned {0} instead "
                    "of {1}".format(actual, expected)
        )
        assert actual is expected, message

    def test_for_missing_tab(self):
        assert row_to_list("1,463238,765\n") is None


    # (m, n) m is number of tabs, n is if the number of values is wrong (1 for true) 


    ################################### TEST Boundaries #####################################

    def test_on_no_tab_no_missing_value(self):    # (0, 0) boundary value
        # Assign actual to the return value for the argument "123\n"
        actual = row_to_list("123\n")
        assert actual is None, "Expected: None, Actual: {0}".format(actual)
        
    def test_on_two_tabs_no_missing_value(self):    # (2, 0) boundary value
        actual = row_to_list("123\t4,567\t89\n")
        # Complete the assert statement
        assert actual is None, "Expected: None, Actual: {0}".format(actual)
        
    def test_on_one_tab_with_missing_value(self):    # (1, 1) boundary value
        actual = row_to_list("\t4,567\n")
        # Format the failure message
        assert actual is None, "Expected: None, Actual: {0}".format(actual)


    ################################### TEST Special logic #####################################


    def test_on_no_tab_with_missing_value(self):    # (0, 1) case
        # Assign to the actual return value for the argument "\n"
        actual = row_to_list("\n")
        # Write the assert statement with a failure message
        assert actual is None, "Expected: None, Actual: {0}".format(actual)
        
    def test_on_two_tabs_with_missing_value(self):    # (2, 1) case
        # Assign to the actual return value for the argument "123\t\t89\n"
        actual = row_to_list("123\t\t89\n")
        # Write the assert statement with a failure message
        assert actual is None, "Expected: None, Actual: {0}".format(actual)


    ################################### TEST Normal cases  #####################################


    def test_on_normal_argument_1(self):
        actual = row_to_list("123\t4,567\n")
        # Fill in with the expected return value for the argument "123\t4,567\n"
        expected = ["123", "4,567"]
        assert actual == expected, "Expected: {0}, Actual: {1}".format(expected, actual)
        
    def test_on_normal_argument_2(self):
        actual = row_to_list("1,059\t186,606\n")
        expected = ["1,059", "186,606"]
        # Write the assert statement along with a failure message
        assert actual == expected, "Expected: {0}, Actual: {1}".format(expected, actual)
