class Solution(object):
    def twoSum(self, nums, target):
        complement_indices = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in complement_indices:
                return [complement_indices[complement], i]
            complement_indices[num] = i
        return []


# class Solution(object):
#     def twoSum(self, nums, target):
#         result = []
#         for x in range(len(nums)-1):
#             for y in range(len(nums)):
#                 if nums[x] == nums[y] and x == y:
#                     y = y+1
#                 if nums[x]+ nums[y] == target:
#                     if nums[x]+ nums[y] not in result and nums[y]+ nums[x] not in result:
#                         result = [x,y]
#                         break
#         return result
s = Solution()
nums = [3,4,5]
target = 9
print(s.twoSum(nums, target))