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
def test_first(test_log_file):
    """Test that we are getting right data for first lines"""
    expected = b'nova-api.log.1.2017-05-16_13:53:08 2017-05-16 00:00:00.008 25746 INFO nova.osapi_compute.wsgi.server ' \
               b'[req-38101a0b-2096-447d-96ea-a692162415ae 113d3a99c3da401fbd62cc2caa5b96d2 54fadb412c4e40cdbaed9335e4c35a9e' \
               b' - - -] 2001:db8:3333:4444:5555:6666:7777:8888 "GET /v2/54fadb412c4e40cdbaed9335e4c35a9e/servers/detail HTTP/1' \
               b'.1" status: 200 len: 1893 time: 0.2477829\nnova-api.log.1.2017-05-16_13:53:08 2017-05-16 00:00:00.272 25746 INFO ' \
               b'nova.osapi_compute.wsgi.server [req-9bc36dd9-91c5-4314-898a-47625eb93b09 113d3a99c3da401fbd62cc2caa5b96d2 54fadb412c4e40cdbaed9335e4c35a9e ' \
               b'- - -] 2001:db8:3333:4444:5255:6666:7777:8888 "GET /v2/54fadb412c4e40cdbaed9335e4c35a9e/servers/detail HTTP/1.1" ' \
               b'status: 200 len: 1893 time: 0.2577181\n'
    with open('./tests/test.log', 'rb') as file_obj:
        result = redparser.first(file_obj, 2)
        print(result)
    assert result == expected.decode('utf-8')