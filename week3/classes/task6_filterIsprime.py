#task6
def filter_primes(lst):
    primes = []
    for x in lst:
        if is_prime(x):
            primes.append(x)
    return primes

def is_prime(x):
    cnt = 0
    for i in range(1, x+1):
        if x % i == 0:
            cnt += 1
    return cnt == 2

numbers = list(map(int, input().split()))

prime_numbers = filter_primes(numbers)
print(prime_numbers)