import pytest


@pytest.fixture
def digits_to_compare():
    return [
        (10, 11), (33, 33), (45, 45), (29, 92), (14, 24), (56, 57), (38, 84), (10, 22), (11, 44), (98, 70), (66, 16)
    ]
