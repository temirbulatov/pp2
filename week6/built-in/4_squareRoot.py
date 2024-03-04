from time import sleep
import math

def delay(fn, ms, *args):
    sleep(ms / 1000)
    return fn(*args)

result = delay(lambda x: math.sqrt(x), 2123, 25100)

print("Square root of " + str(result) + " after 2123 milliseconds is " + str(result))