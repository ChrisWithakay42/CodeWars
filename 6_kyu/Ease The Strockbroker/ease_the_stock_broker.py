def balance_statement(lst):
    if not lst:
        return 'Buy: 0 Sell: 0'

    return lst.split(', ')
