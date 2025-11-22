# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"

# Write the code that will take a string and make this conversion given a number of rows:

# string convert(string s, int numRows);
# Example 1:
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"

# Example 2:
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I

# Example 3:
# Input: s = "A", numRows = 1
# Output: "A"

# Constraints:
# 1 <= s.length <= 1000
# s consists of English letters (lower-case and upper-case), ',' and '.'.
# 1 <= numRows <= 1000

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        queue = []
        display_arr = []
        final_str = ""
        #zag_pos is the pos from top of char that alone in one column
        zag_pos = numRows - 1
        for char in s:
            if (len(queue) == numRows):
                display_arr.append(queue)
                
                zag_pos -= 1
                if (zag_pos > 0):
                    queue = [None] * numRows
                    queue[zag_pos] = char
                else:
                    zag_pos = numRows - 1
                    queue = [char]

            else:
                queue.append(char)
        
        display_arr.append(queue)

        for i in range(numRows):
            for arr in display_arr:
                if i < len(arr) and arr[i] is not None:
                    final_str += arr[i]
        return final_str
