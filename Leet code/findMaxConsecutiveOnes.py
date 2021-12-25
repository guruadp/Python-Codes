class Solution:
    def findMaxConsecutiveOnes(self, nums):
        count=0
        out = 0
        for i in nums:
            if i == 1:
                count+=1
            else:
                count=0

            if count > out:
             
                out = count               
        return out


answer = Solution().findMaxConsecutiveOnes(nums = [1,1,0,1,1,0,1,0,1])
print(answer)
