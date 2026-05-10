class Solution:
    def reverse(self, x):
        x = str(x)
        return x[::-1]

s = Solution()
print(s.reverse(-125))