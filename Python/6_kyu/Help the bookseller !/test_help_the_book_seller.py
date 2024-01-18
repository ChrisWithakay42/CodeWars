import pytest

from help_the_book_seller import stock_list

@pytest.fixture
def stock():
    return ["ABART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"]

@pytest.fixture
def cat():
    return ["A", "B", "C", "W"]

def test_stock_list(stock, cat):
    assert stock_list(stock, cat) == '(A : 20) - (B : 114) - (C : 50) - (W : 0)'