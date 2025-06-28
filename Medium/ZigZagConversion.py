# class Solution(object):
#     def convert(self, s, numRows):
#         """
#         :type s: str
#         :type numRows: int
#         :rtype: str
#         """

#         # 1   9   7
#         # 2  80  68
#         # 3 7 1 5 9
#         # 46  24  0
#         # 5   3   1

#         # 18 -> 4*9
#         # 12 -> 3*6
#         # 21 -> 5*9

#         if numRows == 1:
#             return s

#         numColumns = len(s)
#         arr = [['' for _ in range(numColumns)] for _ in range(numRows)]


#         i, j = 0, 0
#         dir_down = True
#         for c in s:
#             arr[i][j] = c

#             if i == numRows - 1:
#                 dir_down = False
#             elif i == 0:
#                 dir_down = True

#             if dir_down:
#                 i += 1
#             else:
#                 i -= 1
#                 j += 1

#         ans = ''
#         for row in arr:
#             ans += ''.join(row)

#         return ans
# # s= Solution()

# # print(s.convert('paypalishiring',numRows=4))

# # # numColumns =21
# # numRows =4


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s
        
        rows = [''] * numRows
        current_row = 0
        direction = -1 
        for char in s:
            rows[current_row] += char  

            if current_row == 0 or current_row == numRows - 1:
                direction *= -1

            current_row += direction

        return ''.join(rows)  
