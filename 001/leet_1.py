# Brute force
def bruteTwoSum(nums: list[int], target: int) -> list[int]:
    for i in range(0, len(nums)):
        for j in range(1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return [-1, -1]


# Optimized
# Two pointers , this approach is very efficient if the arrays is sorted . but in the given leetcode problem the array is not sorted.
# to apply two pointers , we need to sort the array ,
#  T.C -  worst case O(n long n) if the array is descending order ex = [9,8,7,6,5]
#         Best case  O(n) , if the arrays is partially sorted ex = [1,2,6,5]


def twoSum(nums: list[int], target: int) -> list[int]:
    arr = sorted([(val, index) for index, val in enumerate(nums)])  # O(n) , enumerate visits every ele once , also the tuple also happens once 
    left = 0
    right = len(arr) - 1
    while left < right:
        sum = arr[left][0] + arr[right][0]
        if sum == target:
            return [arr[left][1], arr[right][1]]
        elif sum < target:
            left += 1
        else:
            right -= 1
    return [-1, -1]


print(twoSum(nums=[3, 2, 4], target=6))
