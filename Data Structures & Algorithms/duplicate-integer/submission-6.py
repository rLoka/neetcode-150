# So, basically, simplest way is to use set() func which returns a strict set from array
# Complexity of this solution is O(0), meaning there is no explicit iteration on array items
# There could be implicit python iterations
"""
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(set(nums)) == len(nums):
            return False
        return True
"""        
# Since this is a built in function, let's try to implement solution ground up
# As suggested by hint, we shall try to use HashMap -> a dictionary that memorizes how 
# many times have we seen certain number - uses only one pass - O(n)
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        occurance_map = {}
        for elem in nums:
            if elem in occurance_map:
                return True
            else:
                occurance_map[elem] = True
        return False