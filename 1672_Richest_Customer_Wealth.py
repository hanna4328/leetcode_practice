class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result=[]
        maximum=max(candies)
        for num in candies:
            if num + extraCandies >= maximum:
                result.append(True)
            else:
                result.append(False)
        return result

