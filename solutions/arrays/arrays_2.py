###
#Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.
#You may assume that every input has exactly one pair of indices i and j that satisfy the condition.
#Return the answer with the smaller index first.
###
from typing import List  # Import List from typing module

class Solution:
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i,num in enumerate(nums):
            rem = target - num

            if rem in dict:
                return [dict[rem],i]
            
            dict[num] = i