'''
Input: a List of integers
Returns: a List of integers
'''
from functools import reduce

def multiply(a,b):
    return a*b

def product_of_all_other_numbers(arr):
    # Your code here
    # for each number make a temp array without that number 
    # add up temp arr
    # replace the the number in the original array with the sum
    for i in range(0, len(arr)):
        temp_arr = []
        temp_arr.extend(arr)
        temp_arr.remove(temp_arr[i])
        product = reduce(multiply, temp_arr)
        print(product)
        arr[i] = product
        temp_arr = []
    return arr

arr = [2, 6, 9, 8]
# print(product_of_all_other_numbers(arr))
if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 2, 3, 4, 5]
    # arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
