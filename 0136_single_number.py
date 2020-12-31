from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # nums.sort()
        # i = 0
        # while i < len(nums) - 1:
        #     if nums[i] != nums[i+1]:
        #         break
        #     i += 2
        # return nums[i]

       integers = {}
       for i in nums:
           if integers.get(i):
               integers.pop(i)
           else:
               integers[i] = 1
       return next(iter(integers.keys()))


if __name__ == '__main__':
    numbers = [1, 2, 2, 1, 4]
    answer = Solution().singleNumber(numbers)
    print(answer)
