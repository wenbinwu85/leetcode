class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        y = abs(x)
        while y:
            y, remainder = divmod(y, 10)
            rev = rev * 10 + remainder
            if 2147483647 < rev or rev < -2147483648:
                return 0
        return -rev if x < 0 else rev
            
answer = Solution().reverse(-12345)
print(answer)
