def merge_sort(list):
    if len(list) <= 1:
        return list

    # Divide the list into two halves
    mid = len(list) // 2
    left_half = list[:mid]
    right_half = list[mid:]

    # Recursively sort each half
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the two sorted halves
    return merge(left_half, right_half)

# Define a function to merge two sorted lists into a single sorted list
def merge(left_half, right_half):
    # Initialize an empty list to store the merged result
    result = []

    # While both input lists are not empty, compare the first elements of each list and add the smaller one to the result list
    while len(left_half) > 0 and len(right_half) > 0:
        if left_half[0] <= right_half[0]:
            result.append(left_half[0])
            left_half = left_half[1:]
        else:
            result.append(right_half[0])
            right_half = right_half[1:]

    # If either input list still has elements remaining, append them to the end of the result list
    if len(left_half) > 0:
        result.extend(left_half)
    elif len(right_half) > 0:
        result.extend(right_half)

    # Return the merged and sorted result list
    return result


my_list = [3, 5, 2, 8, 1, 9, 4, 7, 6]
sorted_list = merge_sort(my_list)
print(sorted_list) # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]


