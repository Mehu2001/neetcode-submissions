class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s = sorted(nums)
        res = []
        
        for i in range(len(nums)):
            if i>0 and s[i] == s[i-1]:
                continue
            l = i+1
            r = len(nums) - 1
            while l < r:
                total = s[i] + s[l] + s[r]
                if total ==0:
                    res.append([s[i],s[l],s[r]])
                    while l < r and s[l] == s[l+1]:
                        l +=1
                    while l < r and s[r] == s[r-1]:
                        r -= 1
                    l +=1
                    r -=1
                elif total < 0:
                    l +=1
                else:
                    r -=1
        return res           