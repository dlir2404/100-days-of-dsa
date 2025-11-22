# Given a string s, return the longest palindromic substring in s.
# Example 1:
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.

# Example 2:
# Input: s = "cbbd"
# Output: "bb"

# Constraints:
# 1 <= s.length <= 1000
# s consist of only digits and English letters.
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        def expand_arround_center(s:str, left: int, right: int):
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            # (right - 1) - (left + 1) + 1
            return right - left - 1

        max_start = 0
        max_end = 0

        for i in range(n):
            # there are two case: odd and even
            # even: abba
            # odd: aba
            odd = expand_arround_center(s, i - 1, i + 1)
            even = expand_arround_center(s, i, i + 1)
            curr_len = max(odd, even)
            if curr_len > (max_end - max_start + 1):
                max_start = i - (curr_len - 1) // 2
                max_end = i + curr_len // 2

        return s[max_start:max_end+1]
