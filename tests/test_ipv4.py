"""Tests for the redparser module."""
# Standard library imports
import pathlib

# Third party imports
import pytest

# redparser imports
from redparser.arguments import Arguments
from redparser.parser import Parser

# Current directory
HERE = pathlib.Path(__file__).resolve().parent

@pytest.fixture
def test_log_file():
    """Use local file instead of downloading log from web."""
    return HERE / "test.log"
#
# Tests
#
def test_ipv4_count_test_log(test_log_file):
    """Test that we are getting right number of ipv4 lines"""
    expected = 210 # ipv4 lines
    with open('./tests/test.log', 'rb') as file_obj:
        args = Arguments(['-i', 'test.log'], 1)
        p = Parser(file_obj, args)
        result = p.engine()
        result_list = result.splitlines()
    assert len(result_list) == expected

def test_ipv4_count_ipv4_log(test_log_file):
    """Test that we are getting right number of ipv4 lines"""
    expected = 8
    with open('./tests/ipv4.log', 'rb') as file_obj:
        args = Arguments(['-i', 'test.log'], 1)
        p = Parser(file_obj, args)
        result = p.engine()
        print(result)
        result_list = result.splitlines()
    assert len(result_list) == expected