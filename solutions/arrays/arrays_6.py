"""
Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in O(n)
**O(n) time without using the division operation?

- Without division , only way is : maintaining prefix and post fix arrays.
- But to have O(1) time complexity , we can use the result array as the prefix and while calculating postfix, we actually populate the results.
- First step is to iterate and calculate the prefix and populate the result array
- Then go in reverse order and calculate the results
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prefix = 1 
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1 
        for j in range(len(nums)-1,-1,-1):
            res[j] *= postfix
            postfix *= nums[j]
        return res
        