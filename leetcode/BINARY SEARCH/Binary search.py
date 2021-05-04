def BinarySearch(nums, target):
    # if we want to use binary search method, nums_list need to be sorted

    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right ) // 2
        mid_value = nums[mid]
        if mid_value == target:
            return "Yes"
        elif mid_value < target :
            left = mid + 1
        elif mid_value > target :
            right = mid  -1
    return None
print(BinarySearch([2,3,4,5,6,9],6))
print(BinarySearch([2,3,4,5,6,9],69))

