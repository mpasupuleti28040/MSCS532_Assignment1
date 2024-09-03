def insertion_sort_descending(arr):
    # Loop over the array from the second element to the end
    for i in range(1, len(arr)):
        key = arr[i]         # The current element to be compared
        j = i - 1            # The index of the previous element
        # Move elements of arr[0..i-1], that are smaller than key, to one position ahead
        # of their current position. This loop will help in finding the correct position
        # for the key element by comparing it with elements to its left.
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]      # Shift element to the right
            j -= 1
         # Insert the key element into its correct position
        arr[j + 1] = key
    return arr # Return the sorted array

# Example usage
sample_array = [5, 2, 9, 1, 5, 6]
sorted_array = insertion_sort_descending(sample_array)
print("Sorted array in decreasing order:", sorted_array)

# Test case 1: Regular array with mixed numbers
sample_array_1 = [5, 2, 9, 1, 5, 6]
sorted_array_1 = insertion_sort_descending(sample_array_1)
print("Sorted array in decreasing order:", sorted_array_1)  # Expected output: [9, 6, 5, 5, 2, 1]

# Test case 2: Empty array
sample_array_2 = []
sorted_array_2 = insertion_sort_descending(sample_array_2)
print("Sorted empty array:", sorted_array_2)  # Expected output: []

# Test case 3: Array with one element
sample_array_3 = [42]
sorted_array_3 = insertion_sort_descending(sample_array_3)
print("Sorted single-element array:", sorted_array_3)  # Expected output: [42]

# Test case 4: Array with all elements the same
sample_array_4 = [3, 3, 3, 3, 3]
sorted_array_4 = insertion_sort_descending(sample_array_4)
print("Sorted array with identical elements:", sorted_array_4)  # Expected output: [3, 3, 3, 3, 3]

# Test case 5: Array that is already sorted in decreasing order
sample_array_5 = [10, 8, 6, 4, 2]
sorted_array_5 = insertion_sort_descending(sample_array_5)
print("Sorted array already in decreasing order:", sorted_array_5)  # Expected output: [10, 8, 6, 4, 2]