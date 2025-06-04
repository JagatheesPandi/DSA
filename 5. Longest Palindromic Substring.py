# Given a string s, return the longest palindromic substring in s.

# Example 1:
#
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:
#
# Input: s = "cbbd"
# Output: "bb"

# Constraints:
#
# 1 <= s.length <= 1000
# s consist of only digits and English letters.


class Solution:
    def findLongestPalindrome(self, s : str) -> str:
        def extract_from_center(left : int, right : int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1 : right]

        longest = ''

        for i in range(len(s)):
            odd = extract_from_center(i, i)
            even = extract_from_center(i, i + 1)

            if len(odd) > len(longest):
                longest = odd
            if len(even) > len(longest):
                longest = even
        return longest

sol = Solution()
input = 'cbbd'
print(sol.findLongestPalindrome(input))
