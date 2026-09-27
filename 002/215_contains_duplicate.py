class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # for i in range(0,len(nums)-1):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] == nums[j]:
        #            return True           
        # return False
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

        # Stack => in python list can be used stack . 
        # stack = []
        # for num in nums :
        #     if num in stack:
        #         return True
        #     else:
        #         stack.append(num)
        # return False


# Notes 
# Approach 1 - TC = O(n)^2 , space O(n)
# # Approach 1 - TC = O(n) , space O(n) - efficient approach but why ?
#     - set uses the hash table to store the elements , that means if we want find the number 10 in set(1,5,3,10)
#     - python cannot check for each element like list does . python first calculates the hash of that element then directly find that element in O(1) TC