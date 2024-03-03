class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count_nums = {}
        for i in nums:
            if i not in count_nums:
                count_nums[i] = 1
            elif count_nums[i] == 1:
                return True
        return False

# Bit manipulation solution
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         nums.sort()
#         for i in range(1, len(nums)):
#             if nums[i - 1] ^ nums[i] == 0: return True
#         return False
