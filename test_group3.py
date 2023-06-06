from Group3 import *
import pytest


def test_hex_to_digit():
    assert hex_to_digit("F") == 15
    assert hex_to_digit("A") == 10
    assert hex_to_digit("C") == 12
    assert hex_to_digit("E") == 14

    assert hex_to_digit("1") == 1
    assert hex_to_digit("9") == 9
    assert hex_to_digit("7") == 7
    assert hex_to_digit("5") == 5


def test_digit_to_hex():
    assert digit_to_hex(15) == "F"
    assert digit_to_hex(10) == "A"
    assert digit_to_hex(12) == "C"
    assert digit_to_hex(14) == "E"

    assert digit_to_hex(1) == "1"
    assert digit_to_hex(9) == "9"
    assert digit_to_hex(8) == "8"
    assert digit_to_hex(7) == "7"


def test_inp_base_to_dec():
    assert inp_base_to_dec(50, 16) == 80
    assert inp_base_to_dec("DEAD", 16) == 57005
    assert inp_base_to_dec("420", 8) == 272
    assert inp_base_to_dec(1000101, 2) == 69


def test_dec_to_out_base():
    assert dec_to_out_base(10, 2) == "1010"
    assert dec_to_out_base(15, 2) == "1111"
    assert dec_to_out_base(255, 16) == "FF"


def inp_base_to_dec_float():
    assert inp_base_to_dec_float("101", 2) == 0.625
    assert inp_base_to_dec_float("50", 10) == 0.5


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
