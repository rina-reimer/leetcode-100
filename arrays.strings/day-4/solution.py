class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 1
        j = 1
        while i < len(nums) - 1:
            if nums[i] != nums[i-1] or nums[i] != nums[i+1]:
                print(nums[i])
                nums[j] = nums[i]
                j += 1
            
            i += 1
            print(nums)

        if j < i:
            nums[j] = nums[-1]

        return j + 1