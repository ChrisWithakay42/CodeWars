def arr_adder(arr):
    words = [''.join([arr[row][col] for row in range(len(arr)) if arr[row][col] != '']) for col in range(len(arr[0]))]
    sentence = ' '.join(words)
    return sentence