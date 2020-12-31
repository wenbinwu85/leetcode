from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target < nums[0]:
            for i in range(len(nums)-1, -1, -1):
                if nums[i] > nums[0]:
                    break
                if nums[i] == target:
                    return i
        else:
            for i in range(len(nums)):
                if nums[i] < nums[0]:
                    break
                if nums[i] == target:
                    return i
        return -1

nums = [7,0,5]
target = 3

answer = Solution().search(nums, target)
print(answer)
        