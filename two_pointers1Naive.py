# Given 1-indexed array of integers that is already sorted in ascending order, 
# find two numbers if we add it up we get the target value

# commands to create a nested directories: 
# mkdir -p python/src/coding_interview_patterns
# cd coding_interview_patterns
#---------------------------------------------------------------
# TWO POINTERS
# NAIVE SOLUTION (Unefficient), Time Comlexity O(n^2)

def twoSumNaive(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i]+nums[j] == target:
                # return 1 - indexed array
                return [i+1, j+1]
    return [None, None]


#-----------------------
if __name__ =="__main__":
    array_num =[2,7,11,15] 
    target=90
    print(twoSumNaive(array_num, target))
