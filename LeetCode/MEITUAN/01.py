n, m = map(int, input().strip().split())
nums = []
for _ in range(n):
    nums.extend([x for x in map(int, input().strip().split())])

tmp, n, index = n, len(nums), 1
while index < n:
    j = index
    while j < n // 2 and nums[:j*m] == nums[j*m:j*2*m][::-1]:
        j *= 2
    if j == tmp: break
    index += 1

res, tmp, count = [], "", 0
for ele in nums[:index*m]:
    count += 1
    tmp += str(ele) + " "
    if count % m == 0:
        res.append(tmp)
        tmp = ""

for ele in res:
    print(ele)