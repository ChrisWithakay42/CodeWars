def filter_string(string):
    return int(''.join([elem for elem in string if elem.isdigit()]))