from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums_aux = []
        i = 0
        j = 0
        k = 0

        while i < m and j < n:

            x = nums1.pop(i)
            y = nums2.pop(j)

            if x <= y:
                nums_aux.insert(k, x)
                nums1.insert(i,x)
                nums2.insert(j, y)
                i += 1
            else:
                nums_aux.insert(k,y)
                nums1.insert(i, x)
                nums2.insert(j, y)
                j += 1
            
            k+=1
                
        while i < m:
            x = nums1.pop(i)
            nums_aux.append(x)
            nums1.insert(i, x)
            i += 1
        
        while (j < n):
            x = nums2.pop(j)
            nums_aux.append(x)
            nums2.insert(j, x)
            j += 1
        
        nums1[:] = nums_aux
        print(f"Solution: {nums1}")

#Solution.merge([1,2,3,0,0,0], 3, [2,5,6], 3)

solution = Solution()
#solution.merge(nums1=[1,2,3], m=3, nums2=[], n=0)

#solution.merge(nums1=[0,0,0], m=0, nums2=[2,5,6], n=3)

#solution.merge([1,2,3,0,0,0], 3, [2,5,6], 3)

#solution.merge([1,0], 1, [2], 1)

solution.merge([1,2,5,0], 3, [1], 1)

solution.merge([4,0,0,0,0,0], 1, [1,2,3,5,6], 5)