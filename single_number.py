
# T:O(n) S: O(n) 


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s = set()
        for num in nums:
            if num in s:
                s.remove(num)                
            else:
                s.add(num)                
        return s.pop()
            
        class Solution:
            

# T:O(n) S: O(1) 
#a⊕b⊕a=(a⊕a)⊕b=0⊕b=b



    def singleNumber(self, nums: List[int]) -> int:
        accumulator = 0
        for num in nums:
            accumulator ^= num
        return accumulator
            
        
