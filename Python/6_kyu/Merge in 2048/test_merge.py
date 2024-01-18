import pytest
from merge_2048 import merge


def test_merge():
    assert merge([2, 2, 0, 0]) == [4, 0, 0, 0]
