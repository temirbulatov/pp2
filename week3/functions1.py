#task1  - > ounces = 28.3495231 * grams

def toOunce(x):
    return x * 28.3495231

print(toOunce(5))

#task2  - > C = (5 / 9) * (F – 32)

def toCentri(y):
    C = (5 / 9) * (y - 32)
    return C

print(toCentri(85))

#task3  - > def solve(numheads, numlegs):

def solve(numheads, numlegs):

    for i in range(1, numheads):
        for j in range(1, numheads):
            if(i+j==numheads):
                if(i*2 + j*4 == numlegs):
                    return i, j


print(solve(35, 94))


#task4  - > filter_prime
    
def isPrime(x):
    cnt = 0
    for i in range(1, x+1):
        if x % i ==0:
            cnt += 1
    return cnt ==2

def filter_primes(general_list):
    return set(filter(isPrime, general_list))

l = map(int, input().split())

print(filter_primes(l))

#task5 - > str permutations
import itertools

strf = str(input())
per = itertools.permutations(strf)
 
for val in per:
    print(*val)

#task6 - >  We are ready -> ready are We