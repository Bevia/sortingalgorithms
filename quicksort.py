def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)


# Example usage
if __name__ == "__main__":
    large_dataset = [64, 34, 25, 12, 22, 11, 90, 88, 76, 45, 34, 23, 12, 34, 56, 78, 89, 90, 11]
    sorted_dataset = quick_sort(large_dataset)
    print("Sorted dataset is:", sorted_dataset)

# In this implementation of Quick Sort:
# 1. We choose the pivot as the middle element of the array.
# 2. We partition the array into three sub-arrays: `left` (elements less than the pivot),
# `middle` (elements equal to the pivot), and `right` (elements greater than the pivot).
# 3. We recursively apply Quick Sort to the `left` and
# `right` sub-arrays and concatenate the results.
#
# This version of Quick Sort is simple and easy to understand. However, in practice, more sophisticated
# versions that use in-place partitioning are often used to improve performance and reduce space complexity.
