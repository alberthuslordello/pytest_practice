"""
practice mocking and fixture

"""
import os
import pytest
from unittest.mock import call
from pytest_practice.preprocess import preprocess


# Define a function convert_to_int_bug_free
def convert_to_int_bug_free(row):
    # Assign to the dictionary holding the correct return values 
    return_values = {"1,801": 1801, "201,411": 201411,
                     "2,002": 2002, "333,209": 333209,
                     "1990": None, "782,911": 782911,
                     "1,285": 1285, "389129": None
                    }
    # Return the correct result using the dictionary return_values
    return return_values[row]

def row_to_list_bug_free(row):
    return_values = {
        "1,801\t201,411\n": ["1,801", "201,411"],
        "1,767565,112\n": None,
        "2,002\t333,209\n": ["2,002", "333,209"],
        "1990\t782,911\n": ["1990", "782,911"],
        "1,285\t389129\n": ["1,285", "389129"],
        }
    return return_values[row]

#fixtures do setup for functions that need it.
@pytest.fixture
def raw_and_clean_data_file(tmpdir):
    raw_data_file_path = tmpdir.join("raw.txt")
    clean_data_file_path = tmpdir.join("clean.txt")
    with open(raw_data_file_path, "w") as f:
        f.write("1,801\t201,411\n"
                "1,767565,112\n"
                "2,002\t333,209\n"
                "1990\t782,911\n"
                "1,285\t389129\n"
                )
    yield raw_data_file_path, clean_data_file_path
    

def test_on_raw_data(raw_and_clean_data_file, mocker): # between parenthesis are the fixtures to be called, result is on local variable with same name
    raw_path, clean_path = raw_and_clean_data_file # unpacking result
    convert_to_int_mock = mocker.patch("pytest_practice.preprocessing_helpers.convert_to_int",
                 side_effect = convert_to_int_bug_free
                )
    row_to_list_mock = mocker.patch("pytest_practice.preprocessing_helpers.row_to_list")
    row_to_list_mock.side_effect = row_to_list_bug_free
    preprocess(raw_path, clean_path)
     # Check if preprocess() called the dependency correctly
    assert convert_to_int_mock.call_args_list == [call("1,801"), call("201,411"), call("2,002"), call("333,209"), call("1990"), call("782,911"), call("1,285"), call("389129")]
    with open(clean_data_file_path) as f:
        lines = f.readlines()
    first_line = lines[0]
    assert first_line == "1801\t201411\n"
    second_line = lines[1]
    assert second_line == "2002\t333209\n"

