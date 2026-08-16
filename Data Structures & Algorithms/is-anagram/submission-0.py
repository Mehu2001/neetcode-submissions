class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        res = {}

        for char in s:
            res[char] = res.get(char,0) + 1

        for char in t:
            if char not in res:
                return False
            res[char] -= 1
            if res[char] < 0:
                return False
        return True