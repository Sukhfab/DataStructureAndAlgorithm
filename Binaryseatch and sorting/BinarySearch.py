from math import ceil, floor

# Define a list to search through
lst = [1, 2, 30, 40, 50, 66, 79, 86, 98, 109, 780]

# Define a naive linear search function
def naive(target, lst):
    for x in lst:
        if x == target:
            return lst.index(x)
    return "does not exist"

# Call the naive search function with a target of 30 and the list defined above
print(naive(30, lst))

# Define a binary search function
def binary_search(lst, target, low, high):
    middle = (low+high)//2
    if target not in lst:
        return "none"
    if target == lst[middle]:
        return middle
    if target < lst[middle]:
        return binary_search(lst, target, 0, middle)
    if target > lst[middle]:
        return binary_search(lst, target, middle, high)

# Define the lower and upper bounds of the search
low = 0
high = len(lst)

# Call the binary search function with a target of 5, the list defined above, and the low/high bounds
print(binary_search(lst, 5, low, high))
