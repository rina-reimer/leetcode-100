class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # use pointer on each array
        # determine if m1 < n1
        # add to nums1 array accordingly, decreasing m or n until it reaches 0
        m1 = m - 1
        n1 = n - 1
        i = m + n - 1
        while m1 >= 0 and n1 >= 0:
            curr_m = nums1[m1]
            curr_n = nums2[n1]

            if curr_m > curr_n:
                nums1[i] = curr_m
                m1 = m1 - 1
            else:
                nums1[i] = curr_n
                n1 = n1 - 1
            
            i = i - 1

        while n1 >= 0 and i >= 0:
            curr_n = nums2[n1]
            nums1[i] = curr_n
            n1 = n1 - 1
            i = i - 1
        