"""Tests for the redparser module."""
# Standard library imports
import pathlib

# Third party imports
import pytest

# redparser imports
from redparser import arguments
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
# mmap tests
def test_timestamps_timestamp_ipv4_log(test_log_file):
    """Test that we are getting right data for timestamp lines.  so should be 4"""
    with open('./tests/timestamp.log', 'rb') as file_obj:
        args = arguments.Arguments(['-t', '-i', 'test.log'], 1)
        p = Parser(file_obj, args)
        result = p.engine()
        result_list = result.splitlines()
    assert len(result_list) == 4

def test_timestamps_timestamp_ipv6_log(test_log_file):
    """Test that we are getting right data for timestamp lines.  so should be 4"""
    with open('./tests/timeipv6.log', 'rb') as file_obj:
        args = arguments.Arguments(['-t', '-I', 'test.log'], 1)
        p = Parser(file_obj, args)
        result = p.engine()
        result_list = result.splitlines()
    assert len(result_list) == 4
