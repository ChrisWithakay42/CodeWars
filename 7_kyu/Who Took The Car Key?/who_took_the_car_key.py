def who_took_the_car_key(message: list) -> str:
    return ''.join([chr(int(binary, 2)) for binary in message])
