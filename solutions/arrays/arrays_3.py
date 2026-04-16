"""
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

-parse through every element in array
-sort 
-check if exists in map - if so, add it 
-return List.map.values
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dd = {}
        for s in strs:
            ss = ''.join(sorted(s))
            if ss not in  dd:
                dd[ss] = []
            dd[ss].append(s)
        return list(dd.values())