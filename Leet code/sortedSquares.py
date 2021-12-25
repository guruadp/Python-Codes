class Solution:
    def sortedSquares(self, nums):
        arr = []
        for x in nums:
            arr.append(x*x)   
        new = []
        while arr:
            min = arr[0]
            for x in arr:
                if x < min:
                    min = x
            new.append(min)
            arr.remove(min)

        return new

nums = [-7,-3,2,3,11]

print(Solution().sortedSquares(nums))