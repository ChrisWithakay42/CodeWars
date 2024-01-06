def warn_the_sheep(queue: list) -> str:
    if queue[-1] == 'wolf':
        return 'Pls go away and stop eating my sheep'
    else:
        wolf_position = queue.index('wolf')
        sheep_to_warn = len(queue) - wolf_position - 1
        return f'Oi! Sheep number {sheep_to_warn}! You are about to be eaten by a wolf!'
