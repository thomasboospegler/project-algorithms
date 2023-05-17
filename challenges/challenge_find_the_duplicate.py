def find_duplicate(nums):
    nums.sort()
    for i in range(len(nums)):
        if (
            i + 1 >= len(nums)
            or not isinstance(nums[i + 1], int)
            or not isinstance(nums[i], int)
            or nums[i] < 0
        ):
            return False
        if nums[i] == nums[i + 1]:
            return nums[i]
    return False
