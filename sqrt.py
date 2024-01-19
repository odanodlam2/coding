import math

def sqrt(num):
    guess = 1
    last = -1
    while guess<=num:
        guess+=1
        guess*=guess
    root = guess
    while True:
        root=(root + num/root)/2
        if last == root:
            break
        else: 
            last = root

    return root


number = float(input("input number to sqrt"))

print("my method: " + str(sqrt(number)))
print("internal function " + str(math.sqrt(number)))
