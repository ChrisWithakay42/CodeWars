import pytest
from change_it_up import changer


class TestChanger:

    def test_chars_shifted_by_one(self):
        assert changer("Hello World!") == "ifmmp xpsme!"
        assert changer("abcdefghijklmnopqrstuvwxyz") == "bcdefghijklmnopqrstuvwxyza"
        assert changer("ABCDEFGHIJKLMNOPQRSTUVWXYZ") == "BCDEFGHIJKLMNOPQRSTUVWXYZA"
        assert changer("1234567890") == "1234567890"
        assert changer("") == ""
