from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] >= target:
                return i 
        return i + 1

        
if __name__ == '__main__':
    nums, target = [1,3,5,6], 5
    
    answer = Solution().searchInsert(nums, target)
    print(answer)
