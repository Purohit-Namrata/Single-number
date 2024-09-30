from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res=0
        for n in nums:
            res^=n
        return res
    
s=Solution()
output=s.singleNumber([2, 2, 1])
print("Single number in array ",output)