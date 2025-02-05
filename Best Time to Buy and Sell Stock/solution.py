from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        max_profit = 0
        buy = prices[0]

        for i in range(1, length):
            sell = prices[i]
            if (sell > buy):
                max_profit = max(max_profit, sell-buy)
            elif (sell < buy):
                buy = sell
        
        return max_profit
        '''
        min, idx_min = self.find_min(prices)
        max, idx_max = self.find_max(prices[idx_min:])
        
        print(f"min {min}, index {idx_min}, max {max}, index {idx_max}")
        
        if(idx_min < idx_max+idx_min):
            return max - min
        
        return 0
    
    def find_min(self, a):
        index = 0
        min = a[index]
        
        for i in range(1, len(a)):
            if a[i] < min:
                min = a[i]
                index = i
        
        return min, index
        '''
    
    def find_max(self, a):
        index = 0
        max = a[index]
        
        for i in range(1, len(a)):
            if max < a[i]:
                max = a[i]
                index = i
        
        return max, index
    
solution = Solution()

print(solution.maxProfit([3,5,1,2]))