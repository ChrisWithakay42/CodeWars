def draw(deck):
    drawn_cards = []

    for _ in  range(len(deck)):
        top_card = deck.pop(0)
        drawn_cards.append(top_card)
        if len(deck) > 0:
            next_card = deck.pop(0)
            deck.append(next_card)

    return drawn_cards