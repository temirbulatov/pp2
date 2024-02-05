#task6 - >  We are ready -> ready are We

def reverse_words(s):
    w = s.split()
    rw = ' '.join(reversed(w))
    return rw

u = input("enter smth: ")
r = reverse_words(u)
print("Reversed:", r)