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
def test_last(test_log_file):
    """Test that we are getting right data for last lines"""
    expected = b'nova-compute.log.1.2017-05-16_13:55:31 2017-05-16 00:14:47.663 2931 INFO nova.virt.libvirt.driver [-] ' \
               b'[instance: faf974ea-cba5-4e1b-93f4-3a3bc606006f] Instance destroyed successfully.\n' \
               b'nova-api.log.1.2017-05-16_13:53:08 2017-05-16 00:14:47.687 25746 INFO nova.osapi_compute.wsgi.server ' \
               b'[req-dd237280-5bc8-41cb-a035-26c8e64d49fc 113d3a99c3da401fbd62cc2caa5b96d2 54fadb412c4e40cdbaed9335e4c35a9e ' \
               b'- - -] 2001:db8:3333:4444:5555:6666:7727:8888 "GET /v2/54fadb412c4e40cdbaed9335e4c35a9e/servers/detail HTTP/1.1" ' \
               b'status: 200 len: 1916 time: 0.2717581'
    with open('./tests/test.log', 'rb') as file_obj:
        args = Arguments(['-l', '2', 'test.log'], 1)
        p = Parser(file_obj, args)
        result = p.engine()
        print(result)
    assert result == expected.decode('utf-8')