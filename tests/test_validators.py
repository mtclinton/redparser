"""Tests for the redparser module."""

# redparser imports
import redparser

def test_validate_first():

    # test that positive number is true
    assert redparser.validate_first(1) == True
    assert redparser.validate_first(5) == True
    assert redparser.validate_first(100000000000) == True

    # test that zero is false
    assert redparser.validate_first(0) == False

    # test that negative numbers are false
    assert redparser.validate_first(-1) == False
    assert redparser.validate_first(-5) == False
    assert redparser.validate_first(-100000000000) == False

    # test that strings non integers are false
    assert redparser.validate_first('a') == False
    assert redparser.validate_first('test') == False

    # test that string positive number is true
    assert redparser.validate_first("1") == True
    assert redparser.validate_first("5") == True
    assert redparser.validate_first("100000000000") == True

    # test that string zero is false
    assert redparser.validate_first("0") == False

    # test that string negative numbers are false
    assert redparser.validate_first("-1") == False
    assert redparser.validate_first("-5") == False
    assert redparser.validate_first("-100000000000") == False

    # test that binary positive number is true
    assert redparser.validate_first(b"1") == True
    assert redparser.validate_first(b"5") == True
    assert redparser.validate_first(b"100000000000") == True

    # test that binary zero is false
    assert redparser.validate_first(b"0") == False

    # test that binary negative numbers are false
    assert redparser.validate_first(b"-1") == False
    assert redparser.validate_first(b"-5") == False
    assert redparser.validate_first(b"-100000000000") == False

def test_validate_last():

    # test that positive number is true
    assert redparser.validate_last(1) == True
    assert redparser.validate_last(5) == True
    assert redparser.validate_last(100000000000) == True

    # test that zero is false
    assert redparser.validate_last(0) == False

    # test that negative numbers are false
    assert redparser.validate_last(-1) == False
    assert redparser.validate_last(-5) == False
    assert redparser.validate_last(-100000000000) == False

    # test that strings non integers are false
    assert redparser.validate_last('a') == False
    assert redparser.validate_last('test') == False

    # test that string positive number is true
    assert redparser.validate_last("1") == True
    assert redparser.validate_last("5") == True
    assert redparser.validate_last("100000000000") == True

    # test that string zero is false
    assert redparser.validate_last("0") == False

    # test that string negative numbers are false
    assert redparser.validate_last("-1") == False
    assert redparser.validate_last("-5") == False
    assert redparser.validate_last("-100000000000") == False

    # test that binary positive number is true
    assert redparser.validate_last(b"1") == True
    assert redparser.validate_last(b"5") == True
    assert redparser.validate_last(b"100000000000") == True

    # test that binary zero is false
    assert redparser.validate_last(b"0") == False

    # test that binary negative numbers are false
    assert redparser.validate_last(b"-1") == False
    assert redparser.validate_last(b"-5") == False
    assert redparser.validate_last(b"-100000000000") == False

def test_validate_timestamp():

    # test that validate timestamps return true
    assert redparser.validate_timestamp(b"00:00:00") == True

    # test that validate timestamps return false
    assert redparser.validate_timestamp(b"90:00:00") == False

def test_validate_ipv4():

    # test that valid ipv4 return true
    assert redparser.validate_ipv4("127.0.0.1") == True
    assert redparser.validate_ipv4("192.168.1.1") == True
    assert redparser.validate_ipv4("192.168.1.255") == True
    assert redparser.validate_ipv4("255.255.255.255") == True
    assert redparser.validate_ipv4("0.0.0.0") == True
    assert redparser.validate_ipv4("1.2.3.4") == True
    assert redparser.validate_ipv4("1.1.1.1") == True


    # test that invalid ipv4 return false
    assert redparser.validate_ipv4("30.168.1.255.1") == False
    assert redparser.validate_ipv4("192.168.1.256") == False
    assert redparser.validate_ipv4("1.1.1.01") == False
    assert redparser.validate_ipv4("3...3") == False
    assert redparser.validate_ipv4("127.1") == False

def test_validate_ipv6():

    # test that valid ipv6 return true
    assert redparser.validate_ipv6("21E5:69AA:FFFF:1:E100:B691:1285:F56E") == True
    assert redparser.validate_ipv6("2001:db8:3333:4444:5555:6666:7777:8888") == True
    assert redparser.validate_ipv6("2001:db8:3333:4444:CCCC:DDDD:EEEE:FFFF") == True
    assert redparser.validate_ipv6("::") == True
    assert redparser.validate_ipv6("2001:db8::") == True
    assert redparser.validate_ipv6("::1234:5678") == True
    assert redparser.validate_ipv6("2001:db8::1234:5678") == True
    assert redparser.validate_ipv6("2001:0db8:0001:0000:0000:0ab9:C0A8:0102") == True


    # test that invalid ipv6 return false
    assert redparser.validate_ipv6("21E5:69AA:FFGF:1:E100:B691:1285:F56E") == False
    assert redparser.validate_ipv6("G9::") == False
    assert redparser.validate_ipv6("::1H") == False
    assert redparser.validate_ipv6("3...9999") == False
    assert redparser.validate_ipv6("2001:db8:3333:4444:CCCC:DDDD:EEEE:99999") == False
