import random

arr = []

for i in range(1000000):
    arr.append(i)
    arr.append(i)

random.shuffle(arr)
rand_index = random.randint(0, len(arr))
num = arr.pop(rand_index)
print('arr', arr)
print('num', num)

'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    # make a temp array
    # sort the arr
    # loop through the array adding the items to temp array
    # using a pointer, if the pointer reaches the end of the array return it
    # in the loop if the item at index pointer equals the item in the temp array. remove it from the temp array
    # else if the next item is not equal to the item in the temp
    temp_list = []
    pointer = 0
    arr.sort()
    while pointer < len(arr):
        temp_list.append(arr[pointer])
        if pointer == len(arr) -1:
            return arr[pointer]
        if arr[pointer+1] == temp_list[0]:
            # print(arr[pointer])
            temp_list.remove(temp_list[0])
        else: 
            return temp_list[0]
        pointer+=2
    return temp_list[0]

# time complexity is O(n) for the the loop 
# plus O(n log n) for the .sort method



# sample_arr = [1, 1, 4, 4, 5, 5, 3, 9, 9, 0, 0]
# random.shuffle(sample_arr)
# answer = single_number(arr)
# print(answer, 'answer')
if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")