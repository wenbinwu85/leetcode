from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 1
        for i in range(1, len(nums)):
            curr = nums[i]
            if curr > nums[i-1]:
                nums[count] = curr
                count += 1
        return count
            
    
x = [1, 2, 2, 3, 4, 4]
answer = Solution().removeDuplicates(x)
print(answer)
print(x)
