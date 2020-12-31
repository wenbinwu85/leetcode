from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1, -1, -1):
            last_digit = digits[i] + 1
            if last_digit < 10:
                digits[i] = last_digit
                return digits
            digits[i] = 0
        if not digits[0]:
            return [1] + digits


n = [9, 9]
ans = Solution().plusOne(n)
print(ans)
