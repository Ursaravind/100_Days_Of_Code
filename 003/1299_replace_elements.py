
nums = [17, 18, 5, 4, 6, 1]
ans = []
# for i in range(0, len(nums) - 1):
#     max = -1
#     for j in range(i + 1, len(nums)-1):
#       if nums[j] > nums[j+1]:
#          max = nums[j]
#     if max > -1:
#         nums[i] = max
#     nums[len(nums)-1] = -1
# print(nums)
for i in range(0,len(nums)):
    if nums[i] in ans:
        continue

# Work in Progress WIP
