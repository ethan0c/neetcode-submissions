class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        empty_dict = {}
        for num in nums:
            if num in empty_dict:
                return True
            empty_dict[num] = num
        return False
        