def startRange(nums ,target):
    left, right = 0, len(nums) -1
    index = -1
    while left <= right :
        mid = (left + right) // 2
        mid_point = nums[mid]

        if mid_point == target:
            index = mid
            # because we need to calculate the position for the first position of sorted array, so write following code.
            # Else, if we want to find target value, so just return index is alright.
            # find the first position
            right = mid - 1
        elif mid_point < target:
            left = mid + 1
        elif  mid_point > target :
            right = mid - 1
    return index

def endRange(nums, target):
    left, right = 0, len(nums) - 1
    index = -1
    while left <= right:
        mid = (left + right )// 2
        mid_point = nums[mid]
        if mid_point == target:
            index = mid
            left = mid  + 1
        elif mid_point < target:
            left = mid + 1
        else:
            right = mid -1
    return index
def total(nums ,target) :
    result = [-1,-1]
    if target not in nums :
        return result
    else:
        result = [startRange(nums ,target),endRange(nums, target)]
        return result
print(total([5, 7, 7, 8, 8, 10],  8))
#【3，4】
print(total([5,7,7,7,7,7,8, 8, 10], 7))
#【1，5】
print(total([5,7,7,8,8,10], 10))
#【-1，-1】
print(total([], 0))
#【-1，-1】