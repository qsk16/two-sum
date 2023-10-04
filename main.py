from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    idxs = {}
    
    for i in range(len(nums)):
        n = nums[i]
        other = target-n

        if other in idxs:
            return [idxs[other], i]
        
        idxs[n] = i
    
    #return []

