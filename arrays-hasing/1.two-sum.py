class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        '''for i in range(len(nums)):
            for j in range(len(nums)):
                if (nums[i] + nums[j]) == target and i != j:
                    return [ i, j ]
        '''
        h = {}
        for i, j in enumerate(nums):
            h[j] = i
        for i in range(len(nums)):
            diff = target-nums[i]
            if diff in h and h[diff] != i:
                return [ h[diff], i ]