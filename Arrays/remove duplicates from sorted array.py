class Solution(object):
    def removeDuplicates(self, nums):
        licznik = 0
        output = []
        for key, value in enumerate(nums):
            if value not in output:
                output.append(value)
                licznik += 1

        return output, licznik

nums = [0,0,1,1,1,2,2,3,3,4]
s = Solution()
wynik, licznik = s.removeDuplicates(nums)



