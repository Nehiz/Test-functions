"""A program to verify that the make_full_name, 
extract_family_name and extract_given_name functions work correctly."""

from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest


def test_make_full_name():
    """Verify that the make_full_name function works correctly.
    Parameters: none
    Return: nothing
    """
    # Call the make_full_name function and use an assert
    # statement to verify that the string returned by the
    # make_full_name function is correct.
    assert make_full_name("Sally", "Brown") == "Brown;Sally"


def test_extract_family_name():
    """Verify that the extract_family_name function works correctly.
    Parameters: none
    Return: nothing
    """
    # Call the extract_family_name function and use an assert
    # statement to verify that the string returned by the
    # extraxt_family_name function is correct.
    assert extract_family_name("Brown; Sally") == "Brown"

def test_extract_given_name():
    """Verify that the extract_given_name function works correctly.
    Parameters: none
    Return: nothing
    """

    # Call the extract_given_name function and use an assert
    # statement to verify that the string returned by the
    # extract_given_name function is correct.
    assert extract_given_name("Brown; Sally") == "Sally"


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
