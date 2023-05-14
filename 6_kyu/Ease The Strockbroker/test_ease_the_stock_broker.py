import pytest
from ease_the_stock_broker import balance_statement


@pytest.fixture
def orders():
    return 'ZNGA 1300 2.66 B, CLH15.NYM 50 56.32 B,OWW 1000 11.623 B,OGG 20 580.1 B'
def test_split_orders(orders):
    assert isinstance(balance_statement(orders), list)

def test_return_when_empty_order():
    assert balance_statement('') == 'Buy: 0 Sell: 0'