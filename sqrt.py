class Solution:
    def mySqrt(self, x: int) -> int:
        if x >= 1:
            max_length = x // 2
            if max_length > 1:
                for i in range(x):
                    if i * i == x:
                        return i
                    elif i * i > x:
                        return i - 1
            else:
                return 1
        else:
            return 0

    def srt_binary_search(self, x):
        left = 0
        right = x
        while left <= right:
            mid = (right+left) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1
        return left - 1


sol = Solution()
print(sol.srt_binary_search(7))
