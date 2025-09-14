# sorting.py

def bubble_sort(arr):
    """
    Implements bubble sort algorithm.
    
    Time Complexity: O(n²)
    Space Complexity: O(1)
    """
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def quick_sort(arr):
    """
    Implements quick sort algorithm.
    
    Time Complexity: O(n log n) average, O(n²) worst case
    Space Complexity: O(log n) due to recursion
    """
    # Base case: arrays with 0 or 1 element are already sorted
    if len(arr) <= 1:
        return arr
    
    # Choose the middle element as pivot
    pivot = arr[len(arr) // 2]
    
    # Partition array into three parts
    left = [x for x in arr if x < pivot]    # Elements less than pivot
    middle = [x for x in arr if x == pivot]  # Elements equal to pivot
    right = [x for x in arr if x > pivot]    # Elements greater than pivot
    
    # Recursively sort left and right parts, then combine
    return quick_sort(left) + middle + quick_sort(right)


if __name__ == "__main__":
    # Test both sorting algorithms
    test_arr = [64, 34, 25, 12, 22, 11, 90]
    
    print("Original array:", test_arr)
    print("Bubble sorted:", bubble_sort(test_arr.copy()))
    print("Quick sorted:", quick_sort(test_arr.copy()))