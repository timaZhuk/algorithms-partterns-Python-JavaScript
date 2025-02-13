# Given 1-indexed array of integers that is already sorted in ascending order, 
# find two numbers if we add it up we get the target value

# commands to create a nested directories: 
# mkdir -p python/src/coding_interview_patterns
# cd coding_interview_patterns
#---------------------------------------------------------------
# TWO POINTERS, Time complexity O(n) we iterate once throug the array

def twoPointersSum(nums, target):
    # we create two pointers that will move from begining(pointer_one) of array 
    # and from the end (pointer_two) of array
    # [pointer1-->,.........., <---pointer2]
    pointer_one = 0
    pointer_two = len(nums)-1

# condition while pointer1 less than pointer2 our while loop is valid
    while pointer_one < pointer_two:
        # we calculate sum of two pointers's values
        sum = nums[pointer_one] + nums[pointer_two]
        
        # if sum equal to target return the array of pointers
        if sum==target:
            return [pointer_one+1, pointer_two+1] 
        # if sum less than target we need increment pointer1 by one
        # because our array is ascending then pointer1 will be a greater number in array
        elif sum < target:
            pointer_one +=1
        else:
            # uf sum greater than target, we need decrement pointer2 by one 
            # because our array is ascending array then pointer2 will get lesser value
            pointer_two -=1
    return "No Solution" # or [None, None]



#-----------------------
if __name__ =="__main__":
    array_num =[2,7,11,15] 
    target=90
    print(twoPointersSum(array_num, target))
