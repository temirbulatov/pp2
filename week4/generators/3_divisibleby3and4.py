
def divisible_by_3_and_4_generator(n):
    return (i for i in range(n + 1) if i % 3 == 0 and i % 4 == 0)

n = int(input())

div_gen = divisible_by_3_and_4_generator(n)

print("Numbers divisible by 3 and 4 between 0 and {}:".format(n), end=" ")
print(*div_gen, sep=", ")