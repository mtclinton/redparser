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
def test_timestamps(test_log_file):
    """Test that we are getting right data for timestamp lines. right now all logs have timestamps so should be 2000"""
    with open('./tests/test.log', 'rb') as file_obj:
        args = Arguments(['-t', 'example.log'], 1)
        p = Parser(file_obj, args)
        result = p.engine()
        result_list = result.splitlines()
    assert len(result_list) == 2000