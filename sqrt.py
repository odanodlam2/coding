import math

def BabylonianAlgorithm(number):
    if number == 0: return 0
    
    guess = 1
    i = 1
    
    print("\nProcess to find the initial guess:")
    while True:
        guess = i**2
        if guess > number: 
            break
        else: 
            print(f'Guess: {i} = {guess}')
            i += 1
    i -= 1
    print(f"\n The Guess Number is: {i}, because {i}*{i} = {i*i} which is less than: {number} \n")
    root = i
    for i in range(10):
        print(f"interation {i}: {root}")
        root = (root + number/root)*0.5

    return root

number = int(input("Enter a number to get its square root: "))
result = BabylonianAlgorithm(number)
print(f"\nThe square root with this Babylonian method is: {result}")
print(f"The square root using the internal function math.sqrt() is: {math.sqrt(number)}")
print("----------------------------------------------------------------------------------------------------------------------------------------")
