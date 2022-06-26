class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = []
        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        # 팰린드롬 여부 판별
        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                return False

        return True

# test Example code
# > from Solution1 import Solution
# > f = Solution()
# > f.isPalindrome('12321')
# > True
# > f.isPalindrome('12333')
# > False

