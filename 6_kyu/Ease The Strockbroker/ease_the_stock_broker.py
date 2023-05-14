def balance_statement(lst):
    if not lst:
        return 'Buy: 0 Sell: 0'



def is_valid_order(order):
    components = order.split()
    if len(components) != 4:
        return False
    quote, quantity, price, status = components
    try:
        quantity = int(quantity)
        price = float(price)
        if status not in ['B', 'S']:
            return False
    except ValueError:
        return False
    return True