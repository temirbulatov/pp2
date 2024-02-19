def down_generator(n):
    return (i for i in range(n, -1, -1))

n = int(input())

print("Decreasing list from {} to 0:".format(n), end=" ")
print(*down_generator(n), sep=", ")