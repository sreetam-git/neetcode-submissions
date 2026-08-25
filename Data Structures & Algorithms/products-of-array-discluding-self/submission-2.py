class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)

        # first calculate the left side prefix
        prefix = 1
        for i in range(len(nums)):
            output[i] *= prefix
            prefix *= nums[i]

        # now calculate the right side of suffix
        suffix = 1
        for i in range(len(nums)-1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]

        return output