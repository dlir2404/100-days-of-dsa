class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        counts = {}
        for i, v in enumerate(nums):
            res = counts.get(target - v, None)
            if res is not None:
                return [res, i]
            counts[v] = i
