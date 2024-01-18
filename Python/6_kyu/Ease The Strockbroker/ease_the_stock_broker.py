def balance_statement(lst):
    if not lst:
        return 'Buy: 0 Sell: 0'
    orders = lst.split(', ')
    valid = []
    invalid = []
    for order in orders:
        if is_valid_order(order):
            valid.append(order)
        else:
            invalid.append(order)





def is_valid_order(order):
    components = order.split()
    if len(components) != 4:
        return False
    quote, quantity, price, status = components
    try:
        if status not in ['B', 'S']:
            return False
    except ValueError:
        return False
    return True