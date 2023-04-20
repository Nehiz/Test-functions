"""a program to verify that the extract_city, 
extract_state and extract_zipcode functions work correctly."""

from address import extract_city, \
    extract_state, extract_zipcode
import pytest


def test_extract_city():
    """Verify that the extract_city function works correctly.
    Parameters: none
    Return: nothing
    """

    # Call the extract_city function and use an assert
    # statement to verify that the string returned by the
    # extract_city function is correct.
    assert extract_city("525 S Center St, Rexburg, ID 83460") == "Rexburg"


def test_extract_state():
    """Verify that the extract_state function works correctly.
    Parameters: none
    Return: nothing
    """

    # Call the extract_state function and use an assert
    # statement to verify that the string returned by the
    # extract_state function is correct.
    assert extract_state("525 S Center St, Rexburg, ID 83460") == "ID"


def test_extract_zipcode():
    """Verify that the extract_zipcode function works correctly.
    Parameters: none
    Return: nothing
    """

    # Call the extract_zipcode function and use an assert
    # statement to verify that the string returned by the
    # extract_zipcode function is correct.
    assert extract_zipcode("525 S Center St, Rexburg, ID 83460") == "83460"



# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
