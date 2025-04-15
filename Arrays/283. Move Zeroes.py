class Solution(object):
    def moveZeroes(self,nums):
        k = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[k] = nums[i]
                k += 1


        for i in range(k,len(nums)):
            nums[i] = 0

        return nums

s = Solution()
nums = [0,1,0,3,12]
print(s.moveZeroes(nums))