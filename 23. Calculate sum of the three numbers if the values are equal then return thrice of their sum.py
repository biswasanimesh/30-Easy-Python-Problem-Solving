def sum_thrice(x, y, z):
    sum = x + y + z

    if x == y == z:
        sum = sum * 3
    return sum

print(sum_thrice(1, 52, 3))