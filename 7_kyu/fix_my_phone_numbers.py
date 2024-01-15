def is_it_a_num(s: str) -> str:
    pn = ' '.join([char for char in s if char.isdigit()])
    if pn[0] == '0' and len(pn) == 11:
        return pn
    return 'Not a phone number'
