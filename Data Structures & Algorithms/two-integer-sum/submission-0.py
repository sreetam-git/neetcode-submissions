class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return None

        num_pos = {}
        for i, num in enumerate(nums):
            required = target - num
            if required in num_pos:
                return [num_pos[required], i]
            else:
                num_pos[num] = i

        return []