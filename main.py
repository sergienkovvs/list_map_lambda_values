values = [1, 2, "3", "forth", "end", 99, True, None]

print(list(map(lambda num: num if type(num) != int else str(num), values)))