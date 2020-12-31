from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        x = max(nums)
        if x < len(nums):
            return x + 1
        return x*(x+1)//2 - sum(nums)


if __name__ == '__main__':
    nums = [1]
    answer = Solution().missingNumber(nums)
    print(answer)