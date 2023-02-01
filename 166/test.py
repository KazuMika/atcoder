def longestSubarray(nums, limit) -> int:
    left = 0
    state = 1
    right = len(nums)

    while left <= right:
        print(nums[left:right])
        print(left, right)
        temp = abs(max(nums[left:right])-min(nums[left:right]))
        if temp <= limit:
            return len(nums[left:right])
        if state == 1:
            left += 1
            state = 2
        elif state == 2:
            right -= 1
            left -= 1
            state = 3
        elif state == 3:
            left += 1
            state = 1

    return 0


s = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 1000

b = longestSubarray(s, 1)
print(b)
