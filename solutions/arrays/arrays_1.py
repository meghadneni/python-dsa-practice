from typing import List  # Import List from typing module

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numSet = set(nums)
        if len(nums) != len(numSet):
            return True
        else:
            return False

# Create an instance of the Solution class to call the method
solution = Solution()
print(solution.hasDuplicate([1, 2, 3, 3]))  # This will return True