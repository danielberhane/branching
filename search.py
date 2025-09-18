# search.py
"""
Binary Search Implementation
A search algorithm for finding elements in sorted arrays
"""

def binary_search(arr, target):
    """
    Performs binary search on a sorted array.
    
    Args:
        arr: A sorted list of comparable elements
        target: The element to search for
    
    Returns:
        int: Index of target if found, -1 if not found
    
    Time Complexity: O(log n)
    Space Complexity: O(1)
    
    Example:
        >>> binary_search([1, 3, 5, 7, 9], 5)
        2
        >>> binary_search([1, 3, 5, 7, 9], 6)
        -1
    """
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        # Calculate middle index (avoid overflow in other languages)
        mid = left + (right - left) // 2
        
        # Check if target is at mid
        if arr[mid] == target:
            return mid
        
        # If target is greater, ignore left half
        elif arr[mid] < target:
            left = mid + 1
        
        # If target is smaller, ignore right half
        else:
            right = mid - 1
    
    # Element not found
    return -1


def binary_search_recursive(arr, target, left=0, right=None):
    """
    Recursive implementation of binary search.
    
    Args:
        arr: A sorted list
        target: Element to find
        left: Starting index
        right: Ending index
    
    Returns:
        int: Index if found, -1 if not found
    
    Time Complexity: O(log n)
    Space Complexity: O(log n) due to recursion stack
    """
    if right is None:
        right = len(arr) - 1
    
    # Base case: element not found
    if left > right:
        return -1
    
    # Calculate middle
    mid = left + (right - left) // 2
    
    # Found the element
    if arr[mid] == target:
        return mid
    
    # Search in left half
    elif arr[mid] > target:
        return binary_search_recursive(arr, target, left, mid - 1)
    
    # Search in right half
    else:
        return binary_search_recursive(arr, target, mid + 1, right)


def find_first_occurrence(arr, target):
    """
    Finds the FIRST occurrence of a target in a sorted array with duplicates.
    
    Example:
        >>> find_first_occurrence([1, 2, 2, 2, 3, 4], 2)
        1
    """
    result = -1
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            result = mid  # Found target, but keep looking left
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result


def find_last_occurrence(arr, target):
    """
    Finds the LAST occurrence of a target in a sorted array with duplicates.
    
    Example:
        >>> find_last_occurrence([1, 2, 2, 2, 3, 4], 2)
        3
    """
    result = -1
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            result = mid  # Found target, but keep looking right
            left = mid + 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result


if __name__ == "__main__":
    # Demo the algorithms
    test_array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    
    print("Test array:", test_array)
    print("\nSearching for 7:")
    print("  Iterative:", binary_search(test_array, 7))
    print("  Recursive:", binary_search_recursive(test_array, 7))
    
    print("\nSearching for 6 (not in array):")
    print("  Iterative:", binary_search(test_array, 6))
    print("  Recursive:", binary_search_recursive(test_array, 6))
    
    # Test with duplicates
    dup_array = [1, 2, 2, 2, 3, 4, 5]
    print("\nArray with duplicates:", dup_array)
    print("First occurrence of 2:", find_first_occurrence(dup_array, 2))
    print("Last occurrence of 2:", find_last_occurrence(dup_array, 2))