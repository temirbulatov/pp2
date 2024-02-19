def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

def main():
    try:
        a = int(input("Enter a: "))
        b = int(input("Enter b: "))

        if a > b:
            print("Invalid range: a > b.")
            return

        print("Squares of numbers from {} to {}:".format(a, b))
        for square in squares(a, b):
            print(square, end=", ")

if __name__ == "__main__":
    main()