class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()
        while n != 1 and n not in visit:
            visit.add(n)
            n = self.sumOfSquares(n)
        return n == 1

    def sumOfSquares(self, n: int) -> int:
        total = 0
        while n:
            total += (n % 10) ** 2
            n //= 10
        return total