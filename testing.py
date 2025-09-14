# testing.py

import sys
import time
from sorting import bubble_sort, quick_sort, merge_sort

class Colors:
    """ANSI color codes for pretty output"""
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

def run_test(test_name, input_arr, expected, test_num):
    """
    Run a single test case
    
    Args:
        test_name: Description of the test
        input_arr: Input array to sort
        expected: Expected output
        test_num: Test number for reporting
    
    Returns:
        Boolean indicating if test passed
    """
    # Make a copy since bubble_sort modifies in-place
    input_copy = input_arr.copy()
    
    try:
        # Run the sort
        start_time = time.perf_counter()
        result = bubble_sort(input_copy)
        end_time = time.perf_counter()
        elapsed = (end_time - start_time) * 1000  # Convert to milliseconds
        
        # Check if result matches expected
        if result == expected:
            print(f"{Colors.GREEN}✅ Test {test_num} PASSED{Colors.RESET}: {test_name}")
            print(f"   Input:    {input_arr}")
            print(f"   Output:   {result}")
            print(f"   Time:     {elapsed:.4f}ms")
            return True
        else:
            print(f"{Colors.RED}❌ Test {test_num} FAILED{Colors.RESET}: {test_name}")
            print(f"   Input:    {input_arr}")
            print(f"   Expected: {expected}")
            print(f"   Got:      {result}")
            return False
            
    except Exception as e:
        print(f"{Colors.RED}💥 Test {test_num} ERRORED{Colors.RESET}: {test_name}")
        print(f"   Input: {input_arr}")
        print(f"   Error: {str(e)}")
        return False

def run_edge_case_tests():
    """Test edge cases and boundary conditions"""
    print(f"\n{Colors.BOLD}{Colors.BLUE}=== EDGE CASE TESTS ==={Colors.RESET}")
    
    edge_cases = [
        # (test_name, input, expected)
        ("Empty array", [], []),
        ("Single element", [42], [42]),
        ("Two elements (sorted)", [1, 2], [1, 2]),
        ("Two elements (unsorted)", [2, 1], [1, 2]),
        ("Duplicate elements", [3, 3, 3, 3], [3, 3, 3, 3]),
        ("All same values", [7, 7, 7, 7, 7], [7, 7, 7, 7, 7]),
        ("Already sorted", [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ("Reverse sorted", [5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ("Negative numbers", [-5, -1, -3, -2, -4], [-5, -4, -3, -2, -1]),
        ("Mixed positive/negative", [-2, 3, -1, 0, 2], [-2, -1, 0, 2, 3]),
        ("Floating point numbers", [3.14, 2.71, 1.41, 2.23], [1.41, 2.23, 2.71, 3.14]),
        ("Large numbers", [1000000, 999999, 1000001], [999999, 1000000, 1000001]),
    ]
    
    passed = 0
    failed = 0
    
    for i, (test_name, input_arr, expected) in enumerate(edge_cases, 1):
        if run_test(test_name, input_arr, expected, i):
            passed += 1
        else:
            failed += 1
    
    return passed, failed

def run_standard_tests():
    """Test standard cases with various sizes"""
    print(f"\n{Colors.BOLD}{Colors.BLUE}=== STANDARD TESTS ==={Colors.RESET}")
    
    standard_cases = [
        ("Small unsorted array", [64, 34, 25, 12, 22, 11, 90], [11, 12, 22, 25, 34, 64, 90]),
        ("Random order", [3, 7, 1, 4, 6, 2, 5], [1, 2, 3, 4, 5, 6, 7]),
        ("Many duplicates", [5, 2, 8, 2, 9, 1, 5, 5], [1, 2, 2, 5, 5, 5, 8, 9]),
        ("Single swap needed", [1, 3, 2, 4, 5], [1, 2, 3, 4, 5]),
        ("Alternating high/low", [10, 1, 9, 2, 8, 3, 7], [1, 2, 3, 7, 8, 9, 10]),
    ]
    
    passed = 0
    failed = 0
    
    for i, (test_name, input_arr, expected) in enumerate(standard_cases, 1):
        if run_test(test_name, input_arr, expected, i):
            passed += 1
        else:
            failed += 1
    
    return passed, failed

def run_performance_test():
    """Test performance with larger arrays"""
    print(f"\n{Colors.BOLD}{Colors.BLUE}=== PERFORMANCE TEST ==={Colors.RESET}")
    
    sizes = [10, 50, 100, 500]
    
    for size in sizes:
        # Create reverse-sorted array (worst case for bubble sort)
        test_arr = list(range(size, 0, -1))
        expected = list(range(1, size + 1))
        
        start_time = time.perf_counter()
        result = bubble_sort(test_arr.copy())
        end_time = time.perf_counter()
        elapsed = (end_time - start_time) * 1000
        
        is_correct = result == expected
        status = f"{Colors.GREEN}✅{Colors.RESET}" if is_correct else f"{Colors.RED}❌{Colors.RESET}"
        
        print(f"{status} Size {size:4d}: {elapsed:8.2f}ms - {'Correct' if is_correct else 'INCORRECT'}")
    
    print(f"\n{Colors.YELLOW}⚠️  Note: Bubble sort is O(n²), so time increases quadratically{Colors.RESET}")

def test_in_place_modification():
    """Test that bubble_sort modifies the array in-place"""
    print(f"\n{Colors.BOLD}{Colors.BLUE}=== IN-PLACE MODIFICATION TEST ==={Colors.RESET}")
    
    original = [3, 1, 2]
    arr_to_sort = original.copy()
    returned = bubble_sort(arr_to_sort)
    
    print(f"Original array:     {original}")
    print(f"Array after sort:   {arr_to_sort}")
    print(f"Returned value:     {returned}")
    
    if arr_to_sort == returned:
        print(f"{Colors.GREEN}✅ Confirms: Function modifies in-place AND returns the array{Colors.RESET}")
    else:
        print(f"{Colors.RED}❌ Warning: Return value doesn't match modified array{Colors.RESET}")
    
    if arr_to_sort == [1, 2, 3]:
        print(f"{Colors.GREEN}✅ Array correctly sorted{Colors.RESET}")
    else:
        print(f"{Colors.RED}❌ Array not correctly sorted{Colors.RESET}")

def test_merge_sort():
    """Test merge sort specifically"""
    print("\n{}{}=== MERGE SORT TESTS ==={}".format(Colors.BOLD, Colors.BLUE, Colors.RESET))
    
    test_cases = [
        ("Empty array", [], []),
        ("Single element", [42], [42]),
        ("Two elements", [2, 1], [1, 2]),
        ("Already sorted", [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ("Reverse sorted", [5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ("Random array", [64, 34, 25, 12, 22, 11, 90], [11, 12, 22, 25, 34, 64, 90]),
        ("Duplicates", [5, 2, 8, 2, 9, 1, 5, 5], [1, 2, 2, 5, 5, 5, 8, 9]),
        ("Negative numbers", [-3, -1, -7, -2], [-7, -3, -2, -1]),
    ]
    
    passed = 0
    failed = 0
    
    for test_name, input_arr, expected in test_cases:
        input_copy = input_arr.copy()
        result = merge_sort(input_copy)
        
        if result == expected:
            print("{} {}: PASSED{}".format(Colors.GREEN, test_name, Colors.RESET))
            passed += 1
        else:
            print("{} {}: FAILED{}".format(Colors.RED, test_name, Colors.RESET))
            print("   Expected: {}, Got: {}".format(expected, result))
            failed += 1
    
    print("Merge Sort: {} passed, {} failed".format(passed, failed))
    return passed, failed


def test_quick_sort():
    """Test quick sort specifically"""
    print(f"\n{Colors.BOLD}{Colors.BLUE}=== QUICK SORT TESTS ==={Colors.RESET}")
    
    test_cases = [
        ("Empty array", [], []),
        ("Single element", [42], [42]),
        ("Already sorted", [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ("Reverse sorted", [5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ("Random array", [64, 34, 25, 12, 22, 11, 90], [11, 12, 22, 25, 34, 64, 90]),
        ("Duplicates", [5, 2, 8, 2, 9, 1, 5, 5], [1, 2, 2, 5, 5, 5, 8, 9]),
    ]
    
    passed = 0
    failed = 0
    
    for test_name, input_arr, expected in test_cases:
        input_copy = input_arr.copy()
        result = quick_sort(input_copy)
        
        if result == expected:
            print(f"{Colors.GREEN}✅ {test_name}: PASSED{Colors.RESET}")
            passed += 1
        else:
            print(f"{Colors.RED}❌ {test_name}: FAILED{Colors.RESET}")
            print(f"   Expected: {expected}, Got: {result}")
            failed += 1
    
    print(f"Quick Sort: {passed} passed, {failed} failed")
    return passed, failed

def main():
    """Main test runner"""
    print(f"{Colors.BOLD}{Colors.YELLOW}")
    print("=" * 50)
    print("       BUBBLE SORT TEST SUITE")
    print("=" * 50)
    print(f"{Colors.RESET}")
    
    total_passed = 0
    total_failed = 0
    
    # Run edge case tests
    passed, failed = run_edge_case_tests()
    total_passed += passed
    total_failed += failed
    
    # Run standard tests
    passed, failed = run_standard_tests()
    total_passed += passed
    total_failed += failed
    
    # Run performance test
    run_performance_test()
    
    # Test in-place modification
    test_in_place_modification()

    # Add this in the main() function
    quick_passed, quick_failed = test_quick_sort()
    total_passed += quick_passed
    total_failed += quick_failed

    # Add after quick sort tests
    merge_passed, merge_failed = test_merge_sort()
    total_passed += merge_passed
    total_failed += merge_failed