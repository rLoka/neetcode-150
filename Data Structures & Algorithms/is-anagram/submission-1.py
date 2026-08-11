class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # So, first we have to convert a string to list in order to sort in in place
        # Once list is sorted, we can check if it is an anagram
        # there is also a bruteforce method, but no need to implement that
        s_list: list = list(s)
        s_list.sort()
        t_list: list = list(t)
        t_list.sort()
        return s_list == t_list
        
        