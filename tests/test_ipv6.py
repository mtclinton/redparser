"""Tests for the redparser module."""
# Standard library imports
import pathlib

# Third party imports
import pytest

# redparser imports
import redparser

# Current directory
HERE = pathlib.Path(__file__).resolve().parent


@pytest.fixture
def test_log_file():
    """Use local file instead of downloading log from web."""
    return HERE / "test.log"

#
# Tests
#
def test_ipv6_count(test_log_file):
    """Test that we are getting right number of ipv6 lines"""
    expected = 1012 # ipv6 lines
    with open('./tests/test.log', 'rb') as file_obj:
        result = redparser.ipv6_all(file_obj)
        result_list = result.splitlines()
    assert len(result_list)== expected