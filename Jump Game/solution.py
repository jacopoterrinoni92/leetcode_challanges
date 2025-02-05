from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        print(f"nums{nums}")
        return self.canJumpRec(nums, 0)
        '''
        length = len(nums)
        
        if(length == 1):
            return True
        if nums[0] == 0:
            return False
        
        fisrt_jump = nums[0]
        print(f"{nums}")
        i = 1
        for jump in nums[1:fisrt_jump]:
            a = nums[i+1:i+nums[i]+1]            
            print(f"max_jump: {jump}, a: {a}")  
            
            for j in range(i+1, i+jump+1):
                print(f"a[j]: {nums[j]}")
            
            i+=1
        return False

    def canJump(self, nums: List[int]) -> bool:
        length = len(nums)
        
        if(length == 1):
            return True
        if nums[0] == 0:
            return False
        
        first_jump = nums[0] 
        i=0
        for jump in nums[0:first_jump]:
            #jump = nums[i]
            
            if jump > 0:
                print(f"i: {i}, jump: {jump}")
                if(jump >= length-i-1):
                    return True
                for j in range(i+1, jump+i+1):
                    print(f"j: {j}, a[j]: {nums[j]}")
                    if nums[j] > 0:
                        if(nums[j] >= length-j-1):
                            return True
            i+=1
        return False
    '''
    
    def canJumpRec(self, nums: List[int], idx:int):
        if(idx == len(nums)-1): 
            print("|-- End reached")
            return True
        if(nums[idx] == 0): 
            print("|-- 0 jump")
            pass
        
        reach = idx + nums[idx]
        print(f"idx: {idx}, a[idx]: {nums[idx]}, reach:{reach}")
        
        for j in range(idx+1, reach+1):
            print(f"|- j: {j}, nums[j]: {nums[j]}")  
            if(j < len(nums) and self.canJumpRec(nums, j)):
                return True
            
        return False
            
solution = Solution()

print(solution.canJump([5,9,3,2,1,0,2,3,3,1,0,0]))

print(solution.canJump([3,2,1,0,4]))

print(solution.canJump([1,2]))

print(solution.canJump([1,2,3]))

print(solution.canJump([2,1,0,1,0]))

print(solution.canJump([1,1,1,1,0]))

print(solution.canJump([4,0,4,2,2,0,1,3,3,0,3]))

print(solution.canJump([2,3,1,1,4]))

print(solution.canJump([2,5,0,0]))