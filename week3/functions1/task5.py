#task5 - > str permutations
import itertools

strf = str(input())
per = itertools.permutations(strf)
 
for val in per:
    print(''.join(val))