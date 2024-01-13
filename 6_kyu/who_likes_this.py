def likes(names: list[str]) -> str:
    if not names:
        return 'no one likes this'
    if len(name) == 1:
        return f'{name[0]} likes this'
    elif len(names) == 2:
        return f'{names[0]} and {names[1]} like this'
    elif len(names) == 3:
        return f'{names[0]}, {names[1]} and {names[2]} like this'
    else:
        return f'{names[0]}, {names[1]} and {len(names) - 2} others like this'
