class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return 'false'
        else:
            return str(x) == str(x)[::-1]

sol = Solution()
print(sol.isPalindrome(-121))
