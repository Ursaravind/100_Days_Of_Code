def countNegativesBruteForce(grid: list[list[int]]) -> int:
    # TC : O(M*N)
    count = 0
    for index in range(len(grid)):
        arr = grid[index]
        for num in arr:
            if num < 0:
                count += 1
    return count


def countNegativesBinary(grid: list[list[int]]) -> int:
    count = 0
    for nums in grid:
        low = 0
        high = len(nums) - 1
        first_neg_index = len(nums)
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] < 0:
                count += 1
                first_neg_index = mid
                high = mid - 1
            else:
                low = mid + 1
    return count + (len(nums) - first_neg_index)


print(
    f"Negative numbers in array {countNegativesBinary(grid=[[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]])}"
)
