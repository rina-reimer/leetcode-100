class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # initial thoughts: sort array with insertion sort
            # if the element = val, add it to the back
        k = 1
        for i in range(0, len(nums)):
            if nums[i] == val and i <= len(nums) - k:
                while (i != len(nums) - k and nums[len(nums) - k] == val) and len(nums) > k:
                    k = k + 1
                nums[i] = nums[len(nums) - k]
                nums[len(nums) - k] = val
                print(nums)
                k = k + 1
        
        return len(nums) - k + 1