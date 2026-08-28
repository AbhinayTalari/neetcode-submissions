class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        def expand(l, r):
            while l >=0 and r < len(s) and s[l]==s[r]:
                l-=1; r+=1
            return s[l+1:r]

        for i in range(len(s)):
            # odd
            t = expand(i, i)
            if len(t) > len(res): res = t
            # even
            t = expand(i, i+1)
            if len(t) > len(res): res = t
        return res