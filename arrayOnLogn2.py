# Second variant with O(nlog2(n))

def median_simple(nums1, nums2):
    nums = nums1+nums2
    nums=nums.sort()

    # find the median
    res = len(nums)//2
    if len(nums)%2 == 0:
        res += len(nums)//2 - 1
    
    return res