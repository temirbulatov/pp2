#task1
def generate_squares(N):
    for i in range(N + 1):
        yield i ** 2

N = 5
squares_generator = generate_squares(N)

for square in squares_generator:
    print(square)


#task2
def even_numbers_generator(n):
    for i in range(0, n + 1, 2):
        yield i

def main():
    try:
        n = int(input("Enter a number (n): "))
        if n < 0:
            print("Please enter a non-negative number.")
            return

        even_gen = even_numbers_generator(n)
        even_numbers = list(even_gen)

        print("Even numbers between 0 and {}:".format(n), end=" ")
        print(*even_numbers, sep=", ")


if __name__ == "__main__":
    main()

#task3
def divisible_by_3_and_4_generator(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

def main():
    try:
        n = int(input())
        div_gen = divisible_by_3_and_4_generator(n)
        print("Numbers divisible by 3 and 4 between 0 and {}:".format(n), end=" ")
        for num in div_gen:
            print(num, end=", ")

if __name__ == "__main__":
    main()

#task4
def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

# Test the generator with a for loop
def main():
    try:
        a = int(input("Enter the starting number (a): "))
        b = int(input("Enter the ending number (b): "))

        if a > b:
            print("Invalid range. The starting number should be less than or equal to the ending number.")
            return

        # Iterate through the generated squares and print each value
        print("Squares of numbers from {} to {}:".format(a, b))
        for square in squares(a, b):
            print(square, end=", ")

    except ValueError:
        print("Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    main()

#task5

def countdown_generator(n):
    while n >= 0:
        yield n
        n -= 1

# Test the generator with a for loop
def main():
    try:
        n = int(input("Enter a number (n): "))

        # Iterate through the countdown and print each value
        print("Countdown from {} to 0:".format(n))
        for number in countdown_generator(n):
            print(number, end=", ")

    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()

    