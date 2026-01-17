"""
    Find maximum element in array
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
def find_max(arr):
    if len(arr) == 0:
        return None
    max_value = arr[0]
    for num in arr:
        if num>max_value:
            max_value = num
    return max_value
arr=[3,1,4,1,5,9,2,6,5,3,5]
print(f"Maximum value in the array is: {find_max(arr)}")