class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        missing = []
        
        for num in nums:
            pos = abs(num) - 1 
            if nums[pos] > 0:
                nums[pos] *= -1
                    
        for i in range(len(nums)):
            if nums[i] > 0:
                missing.append(i+1)
        
        
        return missing
        '''
        according to the question, if we sort the list in every index there is supposed to be index + 1 number
        so we loop through the numbers, subtract each by 1 to get their *pos and mark it (by negating it) to know it's filled
        we return numbers of non filled (+ve ones) indexes, by returning idx + 1

        '''
        
