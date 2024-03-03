class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count_nums = {}
        for i in nums:
            if i not in count_nums:
                count_nums[i] = 1
            elif count_nums[i] == 1:
                return True
        return False