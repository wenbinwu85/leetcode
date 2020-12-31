class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1
        }
        num = 0
        prev = 1001
        for i in s:
            current = mapping[i]
            if prev < current:
                num = num + current - prev * 2
            else:
                num += current
            prev = current
        return num

answer = Solution().romanToInt('MCD')
print(answer)
