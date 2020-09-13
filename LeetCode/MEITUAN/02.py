# 两行输入 第一行是各种参数，数组行数，一些限定条件等等
# 第二行是输入数组的数值
T = map(int, input().strip().split())

n, m, k = map(int, input().strip().split())
nums = [x for x in map(int, input().strip().split())]
price =[]
for i in range(m+1):
    price = nums[-1]
    print(nums)
    print(price)


# def get_m(nums, m, k):
#     res, n = [], len(nums)
#
#     left, right = 0, 0
#     tmp = []
#
#     while left < n and right < n:
#         if nums[right] >= k:
#             tmp.append(nums[right])
#             right += 1
#         else:
#             left, right = right + 1, right + 1
#             tmp.clear()
#
#         if len(tmp) == m:
#             res.append(tmp[:])
#             left += 1
#             tmp.pop(0)
#
#     return len(res)
#
#
# print(get_m(nums, m, k))
