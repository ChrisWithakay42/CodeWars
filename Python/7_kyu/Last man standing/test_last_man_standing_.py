import pytest
from last_man_standing_ import last_man_standing


@pytest.fixture
def numbers():
    return 9

def test_last_man_standing(numbers):
    result = last_man_standing(numbers)
    assert result == 6