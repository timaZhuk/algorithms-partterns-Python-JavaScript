
# decision for two arrays (sorted in ascending order) nums1 and nums 2
# find median with O(n) 

def median_arr(nums1, nums2):
    # accumulate two arrays elements in sorted order
    nums = []
    # for method of two pointers use
    i=0
    j=0

    while i < len(nums1) and j < len(nums2):
        # if element in nums1 less than element in nums2 
        # then add nums1 el to nums and increment i
        if nums1[i] < nums2[j]:
            nums.append(nums1[i])
            i+=1
        elif nums1[i]==nums2[j]:
            nums.append(nums1[i])
            nums.append(nums2[j])
            i+=1
            j+=1
        else:
            nums.append(nums2[j])
            j+=1
    
    # wether we have different lengths of arrays we add tails to nums
    while i < len(nums1):
        nums.append(nums1[i])
        i+=1

    while j < len(nums2):
        nums.append(nums2[j])
        j+=1

    # find the median
    res = len(nums)//2
    if len(nums)%2 == 0:
        res += len(nums)//2 - 1
    
    return res

print(median_arr([1,2], [3, 4, 5]))
