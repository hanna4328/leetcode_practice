class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        total=0
        runningSum=[]
        for num in nums:
            total+=num
            runningSum.append(total)
        return runningSum