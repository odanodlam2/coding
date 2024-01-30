import random

def bubblesort(elements):
    swapped = False
    for n in range(len(elements)-1, 0, -1):
        for i in range(n):
            if elements[i] > elements[i + 1]:
                swapped = True
                elements[i], elements[i + 1] = elements[i + 1], elements[i]        
        if not swapped:
            return
    return elements

list_random = [random.randint(1,100) for i in range(20)]
list_ascending = bubblesort(list_random)
list_descending = list(reversed(list_ascending))

print(f"Original: {list_random} \n")
print(f"Ascending list: {list_ascending} \n")
print(f"Descending list: {list_descending}")
