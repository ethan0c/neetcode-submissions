class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n_dict = {}
        for num in nums:
            n_dict[num] = 1
        if len(nums) == len(n_dict):
            return False
        return True