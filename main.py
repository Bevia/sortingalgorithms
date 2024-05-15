# Bubble Sort is generally used for educational purposes to illustrate the concept of sorting algorithms due to its simplicity,
# but it is not efficient for large datasets compared to more advanced algorithms like Quick Sort, Merge Sort, or Heap Sort.

# For large datasets, more efficient sorting algorithms are recommended due to their better time complexity.
# Some commonly used sorting algorithms for large datasets include:
#
# 1. **Quick Sort**:
#    - **Time Complexity**: Average-case \(O(n \log n)\), worst-case \(O(n^2)\) (with good pivot selection, the worst-case is rare).
#    - **Space Complexity**: \(O(\log n)\) due to the recursive call stack.
#    - **Description**: A divide-and-conquer algorithm that picks an element as a pivot and partitions the array around the pivot.
#
# 2. **Merge Sort**:
#    - **Time Complexity**: \(O(n \log n)\) for all cases (worst, average, and best).
#    - **Space Complexity**: \(O(n)\) due to the need for additional temporary arrays.
#    - **Description**: A stable, divide-and-conquer algorithm that divides the array into halves, sorts them, and then merges them back together.
#
# 3. **Heap Sort**:
#    - **Time Complexity**: \(O(n \log n)\) for all cases.
#    - **Space Complexity**: \(O(1)\) (in-place sorting).
#    - **Description**: Converts the array into a heap data structure, then repeatedly extracts the maximum element from the heap
#     and rebuilds the heap.
#
# 4. **Tim Sort**:
#    - **Time Complexity**: \(O(n \log n)\) for all cases.
#    - **Space Complexity**: \(O(n)\).
#    - **Description**: A hybrid sorting algorithm derived from Merge Sort and Insertion Sort. It is the default sorting algorithm
#    in Python's built-in `sort()` and `sorted()` functions.
#
# Here’s an example of using Python’s built-in sorting, which uses Tim Sort:
#
#
# For large datasets, using Python's built-in `sort()` or `sorted()` is recommended because it is highly optimized and efficient.

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Here we have a list of Sorting Algorithms')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
