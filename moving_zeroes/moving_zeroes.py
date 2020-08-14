'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    # make a temp list
    #  loop through array and pop any zeros adding those zeros to temp array
    # after the loop extent the array with the temp array
    temp_array = []
    if 0 not in arr:
        return arr
    for i in arr:
        if arr[i] == 0:
            zero = arr.pop(i)
            temp_array.append(zero)
    arr.extend(temp_array)
    if arr[0] == 0:
        arr.pop(arr[0])
    return arr

# arr1 = [0, 3, 1, 0, -2]
# print(moving_zeroes(arr1))

# Complexity is O(n) because of one loop


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")