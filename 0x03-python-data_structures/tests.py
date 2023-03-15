####### List Comprehensions
# squares = [x**2 for x in range(10)]
# print(squares)

# cords = [(x, y)for x in [1, 2, 3] for y in range(5) if x != y]
# print(cords)

# cords1 = [(x, y)for x in range(1, 4) for y in range(5) if x != y]
# print(cords1)

# vec = [-2, -1, 0, 1, 2]
# print([x*2 for x in vec])

# nums = [(-x, x, x**2) for x in range(10)]
# print(nums)

# print([(x, y, z) for x in range(4) for y in range(4) for z in range(4)
#        if x != y and y != z and x != z])

# vec = [[1,2,3], [4,5,6], [7,8,9]]
# print([num for elem in vec for num in elem])
# vec = list(zip(vec[0], vec[1], vec[2], strict=True))
# print(vec)
# vec = list(zip(vec[0], vec[1], vec[2], strict=True))
# print(vec)
