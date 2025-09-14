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


def merge_sort(arr):
    """
    Implements merge sort algorithm using divide-and-conquer.
    
    Time Complexity: O(n log n) - always, even worst case!
    Space Complexity: O(n) - needs extra space for merging
    
    Better than quick sort for:
    - Guaranteed O(n log n) performance
    - Stable sorting (preserves order of equal elements)
    - Predictable performance
    """
    # Base case: single element or empty
    if len(arr) <= 1:
        return arr
    
    # Divide: Split array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Conquer: Recursively sort both halves
    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)
    
    # Combine: Merge the sorted halves
    return merge(sorted_left, sorted_right)


def merge(left, right):
    """
    Helper function to merge two sorted arrays.
    
    Args:
        left: Sorted array
        right: Sorted array
    
    Returns:
        Merged sorted array
    """
    result = []
    i = j = 0
    
    # Compare elements from left and right, adding smaller one
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Add remaining elements (if any)
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result


if __name__ == "__main__":
    # Test all three sorting algorithms
    test_arr = [64, 34, 25, 12, 22, 11, 90]
    
    print("Original array:", test_arr)
    print("Bubble sorted:", bubble_sort(test_arr.copy()))
    print("Quick sorted:", quick_sort(test_arr.copy()))
    print("Merge sorted:", merge_sort(test_arr.copy()))