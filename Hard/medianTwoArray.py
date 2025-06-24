# num1 = [1,2,3]
# num2 =[3,4,5]
# num3 =sorted(num1+num2)
# # leng = len(num3)

# def calcNum():
#     length = len(num3)+1
#     if length % 2 == 0:
#         median1 = num3[length//2+1]
#         median2 =num3[length//2]
#         median= (median1 + median2)/2
#         return median
#     else :
#         median = num3[length//2+1]
#         return median
# result =calcNum()
# # print(result)
# # print(leng)

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        num3 = sorted(nums1 + nums2)
        length = len(num3)
        if length % 2 == 0:
            mid1 = length // 2 - 1
            mid2 = length // 2
            median = (num3[mid1] + num3[mid2]) / 2.0
            return median
        else:
            mid = length // 2
            median = num3[mid]
            return median


