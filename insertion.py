def insertion_sort_descending(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Example usage
sample_array = [5, 2, 9, 1, 5, 6]
sorted_array = insertion_sort_descending(sample_array)
print("Sorted array in decreasing order:", sorted_array)
