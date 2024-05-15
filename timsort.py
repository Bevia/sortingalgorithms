def insertion_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def merge(arr, left, mid, right):
    len1, len2 = mid - left + 1, right - mid
    left_part = arr[left:mid + 1]
    right_part = arr[mid + 1:right + 1]

    i, j, k = 0, 0, left

    while i < len1 and j < len2:
        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1
        k += 1

    while i < len1:
        arr[k] = left_part[i]
        i += 1
        k += 1

    while j < len2:
        arr[k] = right_part[j]
        j += 1
        k += 1


def tim_sort(arr):
    min_run = 32
    n = len(arr)

    for i in range(0, n, min_run):
        insertion_sort(arr, i, min(i + min_run - 1, n - 1))

    size = min_run
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))
            if mid < right:
                merge(arr, left, mid, right)
        size *= 2

    return arr


# Example usage
if __name__ == "__main__":
    large_dataset = [64, 34, 25, 12, 22, 11, 90, 88, 76, 45, 34, 23, 12, 34, 56, 78, 89, 90, 11]

    #sorted_dataset = tim_sort(large_dataset)
    #print("Sorted dataset is:", sorted_dataset)

    # Example usage of Python's built-in sorting, which uses TIM sort:
    sorted_dataset = sorted(large_dataset)
    print("Sorted dataset is:", sorted_dataset)

# In this implementation of Tim Sort:
#
# 1. Insertion Sort: This function is used for sorting small chunks (runs) of the array. It is efficient for small datasets and nearly sorted arrays.
# 2. Merge: This function merges two sorted sub-arrays into a single sorted array.
# 3. Tim Sort: This function performs the following steps:
# - Divides the array into small chunks (runs) and sorts each chunk using insertion sort.
# -Merges the sorted runs using the merge function, doubling the size of runs to be merged in each pass until the entire array is sorted.
#
# Tim Sort is efficient with a time complexity of \(O(n \log n)\) for all cases and works well with real-world data which
# often contains ordered sequences. It combines the best aspects of merge sort and insertion sort, making it very practical for a wide range of applications.
