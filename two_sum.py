class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            key = target - nums[i]
            if key in nums and nums.index(key) != i:
                return [i, nums.index(key)]


sol = Solution()
print(sol.twoSum([2, 7, 11, 15], 9))
