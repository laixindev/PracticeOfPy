n, k, d = map(int, input().strip().split())
sub_a = [_ for _ in range(1, k + 1)]
sub_b = [_ for _ in range(1, d + 1)]

nums = []
nums.extend(sub_a)
nums.extend(sub_b)


def get_num(nums, n, k, d):
    length = len(nums)
    res = []

    def back_trace(nums, cur):
        if sum(cur) == n:
            if cur not in res:  res.append(cur[:])
            return

        if sum(cur) > n: return
        for ele in nums:
            back_trace(nums, cur + [ele])

    back_trace(nums, [])
    return len(res) - 1


print(get_num(nums, n, k, d))
