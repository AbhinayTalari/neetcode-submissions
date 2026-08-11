class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        count1, count2 = {}, {}
        for c in s1:
            count1[c] = count1.get(c, 0) + 1

        for i in range(len(s2)):
            count2[s2[i]] = count2.get(s2[i], 0) + 1
            if i >= len(s1):
                count2[s2[i - len(s1)]] -= 1
                if count2[s2[i - len(s1)]] == 0:
                    del count2[s2[i - len(s1)]]
            if count1 == count2:
                return True
        return False
        