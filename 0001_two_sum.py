class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for idx, val in enumerate(nums):
            if target-val in num_map:
                return [idx, num_map[target-val]]
            num_map[val] = idx
        return []
