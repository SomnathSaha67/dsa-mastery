"""
    Reverse array in-place
    Time Complexity:  O(n)
    Space Complexity: O(1)
    """
def reverse_array(arr):
    left = 0
    right = len(arr)-1
    while left<right:
        arr[left], arr[right] = arr[right], arr[left]
        left+=1
        right-=1
    return arr
arr=[1,2,3,4,5,6,7,8,9,10,12,15,13,11]
print(f"Original array: {arr}")
print(f"Reversed array: {reverse_array(arr)}")