'''
Given an integer array nums and two integers left and right, return the number of contiguous non-empty subarrays such that 
the value of the maximum array element in that subarray is in the range [left, right].

The test cases are generated so that the answer will fit in a 32-bit integer.

 

Example 1:

Input: nums = [2,1,4,3], left = 2, right = 3
Output: 3
Explanation: There are three subarrays that meet the requirements: [2], [2, 1], [3].

Example 2:

Input: nums = [2,9,2,5,6], left = 2, right = 8
Output: 7
Explanation: [2], [2, 5], [5, 6], [2], [5], [6], [2, 5, 6]
'''
# Aryan Mittal's Non-Solution
def numSubarrayBoundedMax(nums, left, right):
    """
    :type nums: List[int]
    :type left: int
    :type right: int
    :rtype: int
    """
    # O(n^2), where n is nums
    res = 0
    for i in range(len(nums)): #O(n)
        for j in range(i, len(nums)): #O(n)
            if nums[j] > right:
                break
            elif nums[j] < left:
                continue
            else:
                res += 1

    return res
