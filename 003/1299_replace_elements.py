nums = [17, 18, 5, 4, 6, 1]
# for i in range(0, len(nums) - 1):
#     max = -1
#     for j in range(i + 1, len(nums)-1):
#       if nums[j] > nums[j+1]:
#          max = nums[j]
#     if max > -1:
#         nums[i] = max
#     nums[len(nums)-1] = -1
# print(nums)

# Time limit Exceed - O(n)^2
# for i in range(0, len(nums) - 1):
#     max = -1
#     for j in range(i + 1, len(nums)):
#         if nums[j] > max:
#             max = nums[j]
#     nums[i] = max
# nums[-1] = -1
# print(nums)


max = -1
i = len(nums)-1
while i >= 0:
    current = nums[i]
    nums[i] = max
    if current > max:
        max = current
    i -= 1
print(nums)
# Work in Progress WIP
