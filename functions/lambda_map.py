# lambda, map, filter
nums = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x * x, nums))
evens = list(filter(lambda x: x % 2 == 0, nums))
print(squares, evens)

names = ['kim', 'lee', 'park']
upper = list(map(str.upper, names))
print(upper)
