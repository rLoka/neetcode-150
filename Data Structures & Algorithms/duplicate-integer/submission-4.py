# So, basically, simplest way is to use set() func which returns a strict set from array
# Complexity of this solution is O(0), meaning there is no explicit iteration on array items
# There could be implicit python iterations
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(set(nums)) == len(nums):
            return False
        return True
        