"""Implement quick sort in Python.
Input a list.
Output a sorted list.

Here's how it works:
    First, the quicksort function checks the length of the array. If the length is less than 2, then the array is already sorted, and it is returned as-is.
    If the length of the array is 2 or greater, then the function selects the first element of the array as the pivot value.
    The function then creates two new arrays: one containing all the elements less than or equal to the pivot, and one containing all the elements greater than the pivot.
    Finally, the function recursively sorts the two new arrays (using quicksort) and concatenates them with the pivot value in the middle to produce the final sorted array.
"""


# Define a function to sort an array using the quicksort algorithm
def quicksort(array):
    # Base case: if the array has less than two elements, it is already sorted
    if len(array) < 2:
        return array

    # Choose a pivot element and divide the array into two sub-arrays: one with elements less than or equal to the pivot, and another with elements greater than the pivot
    pivot = array[0]
    less = [x for x in array[1:] if x <= pivot]
    more = [x for x in array[1:] if x > pivot]

    # Recursively sort the two sub-arrays using the same quicksort function
    sorted_less = quicksort(less)
    sorted_more = quicksort(more)

    # Concatenate the sorted sub-arrays along with the pivot to get the final sorted array
    return sorted_less + [pivot] + sorted_more


# Test the quicksort function with a sample array
test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(quicksort(test))

