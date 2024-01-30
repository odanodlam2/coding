import random

list_random = [random.randint(1,100) for i in range(20)]
list_ascending = sorted(list_random)
list_descending = sorted(list_random, reverse=True)

print(f"Original: {list_random} \n")
print("Ascending list: {list_ascending} \n")
print("Descending list: {list_descending}")
