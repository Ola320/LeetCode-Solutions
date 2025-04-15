class Solution(object):
    def removeElement(self, nums, val):

        i = 0
        n = len(nums)
        while i <= n:
            if nums[i] == val:
                nums[i] = nums[n-1]
                n -= 1

            else:
                i += 1

        return n


class Solution(object):
    def removeElement(self, nums, val):
        k = 0
        for i in range(len(nums)):
            if val != nums[i]:
                nums[k] = nums[i]
                k += 1

            return k


s = Solution()
nums = [3,6,3,2,5,7]
val = 3
print(s.removeElement(nums,val))