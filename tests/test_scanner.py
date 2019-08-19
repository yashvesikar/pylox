# WORK IN PROGRESS
from unittest import TestCase
from lox import Lox
from token_type import TokenType

class TestScanner(TestCase):

    def test_1(self):
        my = Lox(['scan_1.l'])
        assert 10 == len(my.tokens)

    def test_2(self):
        my = Lox(["scan_2.l"])
        print(len(my.tokens))
        assert 17 == len(my.tokens)

    def test_3(self):
        my = Lox(["scan_3.l"])
        assert 4 == len(my.tokens)

    def test_4(self):
        my = Lox(["scan_4.l"])
        print(len(my.tokens))
        assert 19 == len(my.tokens)

