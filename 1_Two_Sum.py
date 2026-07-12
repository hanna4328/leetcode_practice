class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for index,num in enumerate(nums):
            needed = target - num
            if needed in d:
                return [index,d[needed]]
            d[num]= index