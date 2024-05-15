def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # left child
    right = 2 * i + 2  # right child

    # See if left child of root exists and is greater than root
    if left < n and arr[i] < arr[left]:
        largest = left

    # See if right child of root exists and is greater than the largest so far
    if right < n and arr[largest] < arr[right]:
        largest = right

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Heapify the root
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    # Build a maxheap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)

    return arr


# Example usage
if __name__ == "__main__":
    large_dataset = [64, 34, 25, 12, 22, 11, 90, 88, 76, 45, 34, 23, 12, 34, 56, 78, 89, 90, 11]
    sorted_dataset = heap_sort(large_dataset)
    print("Sorted dataset is:", sorted_dataset)

# In this implementation of Heap Sort:
# 1. The `heapify` function ensures the subtree with root at index `i` is a max heap.
# 2. The `heap_sort` function builds a max heap from the input array.
# 3. It then repeatedly extracts the maximum element (which is at the root of the heap)
# and places it at the end of the array, reducing the heap size by one each time.
# 4. The heap property is restored by calling `heapify` on the reduced heap.
#
# Heap Sort has a time complexity of \(O(n \log n)\) for all cases and operates in-place, requiring
#     only a constant amount of extra memory. This makes it efficient and suitable for large datasets.

