from Group3 import *
import pytest


def test_hex_to_digit():
    assert hex_to_digit("0") == 0
    assert hex_to_digit("9") == 9
    assert hex_to_digit("A") == 10
    assert hex_to_digit("F") == 15


def test_digit_to_hex():
    assert digit_to_hex(0) == "0"
    assert digit_to_hex(9) == "9"
    assert digit_to_hex(10) == "A"
    assert digit_to_hex(15) == "F"


def test_inp_base_to_dec():
    assert inp_base_to_dec("1010", 2) == 10
    assert inp_base_to_dec("FF", 16) == 255
    assert inp_base_to_dec("123", 8) == 83
    assert inp_base_to_dec("11", 2) == 3


def test_dec_to_out_base():
    assert dec_to_out_base(10, 2) == "1010"
    assert dec_to_out_base(255, 16) == "FF"
    assert dec_to_out_base(83, 8) == "123"


def test_add():
    assert add("50", "50", 16) == "A0"
    assert add("50", "50", 10) == "100"
    assert add("FA", "CE", 16) == "1C8"


def test_multiply():
    assert multi("50", "50", 16) == "1900"
    assert multi("50", "27", 10) == "1350"
    assert multi("FA", "CE", 16) == "C92C"


def test_minus():
    assert minus("50", "4F", 16) == "1"
    assert minus("100", "50", 10) == "50"
    assert minus("FA", "CE", 16) == "2C"
    assert minus("50", "50", 16) == "0"


def test_div():
    assert div("1010", "1", 2) == "1010"
    assert div("50", "5", 16) == "10"
    assert div("100", "2", 10) == "50"
    assert div("FF", "F", 16) == "11"
    assert div("123456789ABCDEF", "F", 16) == "136B06E70B7421"
    assert div("1010", "11", 2) == "11"
    assert div("1010", "10", 2) == "101"


def test_mod():
    assert mod("50", "50", 16) == "0"
    assert mod("100", "50", 10) == "0"
    assert mod("FA", "CE", 16) == "2C"
    assert mod("50", "50", 16) == "0"
