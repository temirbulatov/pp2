#task3  - > def solve(numheads, numlegs):

def solve(numheads, numlegs):

    for i in range(1, numheads):
        for j in range(1, numheads):
            if(i+j==numheads):
                if(i*2 + j*4 == numlegs):
                    return i, j


print(solve(35, 94))