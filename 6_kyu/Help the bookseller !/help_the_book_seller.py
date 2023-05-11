def stock_list(list_of_art, list_of_cat):
    if not list_of_cat or not list_of_art:
        return ''
    quantities = {category: 0 for category in list_of_cat}
    for book in list_of_art:
        code, quantity = book.split()
        category = code[0]
        if category in quantities:
            quantities[category] += int(quantity)

    return " - ".join(f"({category} : {quantities[category]})" for category in list_of_cat)