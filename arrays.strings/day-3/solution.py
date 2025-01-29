class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # the values after the expectedNums are irrelevant
        i = 0
        j = 1
        k = 1
        # need to cycle thru the initial array until it reaches the garbage array
        while i < len(nums) - 1 and k == i + 1:
            # find a value amongst the garbage that is not equal to the current element
            while j < len(nums) - 1 and nums[i] == nums[j]:
                j = j + 1
            # switches with that element
            nums[i+1] = nums[j]
            # if it hasn't reached the garbage yet
            if nums[i] < nums[i+1]:
                k = k + 1
            i = i + 1

        return k