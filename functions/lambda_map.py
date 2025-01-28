# lambda, map, filter
nums = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x * x, nums))
evens = list(filter(lambda x: x % 2 == 0, nums))
print(squares, evens)

names = ['kim', 'lee', 'park']
upper = list(map(str.upper, names))
print(upper)

pairs = [(1, 'a'), (2, 'b')]
by_num = sorted(pairs, key=lambda p: p[0])
print(by_num)
