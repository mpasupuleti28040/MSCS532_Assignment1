def insertion_sort_descending(arr):
    # Loop over the array from the second element to the end
    for i in range(1, len(arr)):
        key = arr[i] # The current element to be compared
        j = i - 1    # The index of the previous element
    # Move elements of arr[0..i-1], that are smaller than key, to one position ahead
        # of their current position. This loop will help in finding the correct position
        # for the key element by comparing it with elements to its left.
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j] # Shift element to the right
            j -= 1            # Move to the previous element
         # Insert the key element into its correct position
        arr[j + 1] = key
    return arr   # Return the sorted array

# Example usage
sample_array = [5, 2, 9, 1, 5, 6]
sorted_array = insertion_sort_descending(sample_array)
print("Sorted array in decreasing order:", sorted_array)
