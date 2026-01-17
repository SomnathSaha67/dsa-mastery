"""
    Search for target in array using linear search
    Time Complexity: O(n) - we check each element
    Space Complexity: O(1) - no extra space used
    """
def linear_search(arr, target):
    for index in range(len(arr)):
        if arr[index] == target:
            return index
    return -1
arr=[1,2,3,4,5,6,7,8,9,10]
target=int(input("Enter the target value to search: "))
print(f"Target found at index: {linear_search(arr, target)}")