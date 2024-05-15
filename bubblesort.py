# This code defines the `bubble_sort` function which sorts an array in ascending order.
# The function iteratively compares and swaps adjacent elements if they are in the wrong order.
# The process repeats until the array is sorted.

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Track if any swaps happen
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap if the element found is greater
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no elements were swapped, the array is sorted
        if not swapped:
            break
    return arr


# Example usage
if __name__ == "__main__":
    sample_array = [64, 34, 25, 12, 22, 11, 90]
    sorted_array = bubble_sort(sample_array)
    print("Sorted array is:", sorted_array)

# Bubble Sort is a simple comparison-based sorting algorithm.
#
# Here are some key characteristics:
#
# 1. Comparison-Based: It repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.
# 2. Stable Sorting: It maintains the relative order of equal elements.
# 3. In-Place Sorting: It requires only a constant amount \(O(1)\) of additional memory space.
# 4. Time Complexity: It has a worst-case and average-case time complexity of \(O(n^2)\), where \(n\) is the number of
#           elements in the list. The best-case time complexity is \(O(n)\) when the list is already sorted.
# 5. Adaptive: It can terminate early if the list becomes sorted before completing all passes.

