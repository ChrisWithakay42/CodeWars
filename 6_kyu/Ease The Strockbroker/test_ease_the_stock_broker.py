import pytest
from ease_the_stock_broker import balance_statement
from ease_the_stock_broker import is_valid_order

@pytest.fixture
def orders():
    return 'ZNGA 1300 2.66 B, CLH15.NYM 50 56.32 B,OWW 1000 11.623 B,OGG 20 580.1 B'

@pytest.fixture
def badly_formed_orders():
    return

def test_return_when_empty_order():
    assert balance_statement('') == 'Buy: 0 Sell: 0'

def test_is_valid_order():
    # Valid orders
    assert is_valid_order("GOOG 300 542.0 B") == True
    assert is_valid_order("ZNGA 1300 2.66 B") == True
    assert is_valid_order("CLH15.NYM 50 56.32 B") == True

    # Invalid orders
    assert is_valid_order("") == False  # Empty order
    assert is_valid_order("GOOG 300 542.0 s") == False  # Missing status
    assert is_valid_order("GOOG 300 542.0 X") == False  # Invalid status
    assert is_valid_order("GOOG 300 ABC b") == False  # Invalid quantity
    assert is_valid_order("GOOG 300 542.0 B S") == False  # Extra component
