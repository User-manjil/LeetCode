# Given an integer x, return true if x is a palindrome, and false otherwise.
from operator import truediv


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s=str(x)
        revX=s[::-1]

            
        if s==revX:
            return True
        else:
            return False
         

        # python
# class Solution(object):
#     def isPalindrome(self, x):
#         """
#         :type x: int
#         :rtype: bool
#         """
#         if x <0:
#             return False
#         rev = 0
#         num = x

#         while num != 0:
#             rev = rev * 10 
#             rev += num % 10
#             num = num // 10
#         print(rev)