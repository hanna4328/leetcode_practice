class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maximum=-1
        for customer in accounts:
            if sum(customer)>maximum:
                    maximum = sum(customer)
        return maximum