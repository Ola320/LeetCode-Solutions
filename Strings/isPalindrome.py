class Solution(object):
    def isPalindrome(self,x):
        is_pali = True
        queue = []
        number = x
        if number < 0:
            return False
        while number > 0:
           digit = number % 10
           queue.append(digit)
           number = number // 10
        stock = queue.copy()
        stock.reverse()
        for i in range(len(queue)):
           if queue[i] != stock[i]:
                is_pali = False
        return is_pali
s = Solution()
print(s.isPalindrome(-101))