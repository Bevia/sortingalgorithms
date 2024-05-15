def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Divide the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort each half
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # Merge the two sorted halves
    return merge(left_sorted, right_sorted)


def merge(left, right):
    result = []
    left_index = 0
    right_index = 0

    # Merge the two arrays while maintaining order
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    # Append any remaining elements from the left array
    result.extend(left[left_index:])

    # Append any remaining elements from the right array
    result.extend(right[right_index:])

    return result


# Example usage
if __name__ == "__main__":
    large_dataset = [64, 34, 25, 12, 22, 11, 90, 88, 76, 45, 34, 23, 12, 34, 56, 78, 89, 90, 11]
    sorted_dataset = merge_sort(large_dataset)
    print("Sorted dataset is:", sorted_dataset)

# In this implementation of Merge Sort:
# 1. The `merge_sort` function recursively divides the array into two halves until the base case of a single-element (or empty) array is reached.
# 2. The `merge` function then merges two sorted halves into a single sorted array.
# 3. This process is repeated until the entire array is sorted.
#
# Merge Sort is efficient and has a time complexity of \(O(n \log n)\) for all cases, making it suitable for large datasets.
# However, it requires additional space proportional to the size of the input array due to the use of auxiliary arrays during the merging process.
