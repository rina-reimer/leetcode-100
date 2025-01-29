# Stats
Time: 28 minutes

Runtime: $O(n)$, $O(k)$ amortized

Memory: $O(1)$

# Approach
I started by switching pairs of elements if they weren't equal, but I quickly found that it broke the non-decreasing order. I then worked to make it so that a pointer would search the rest of the array for a value that wasn't equal to the current element, not worrying about upholding the non-decreasing order past the kth element. I learned that I had to keep track of where the garbage started, as the `while` loop had to run to the end of the array without an auxilary constant. 

During the coding process, I ran into multiple barriers, however, I have learned to reorient myself and not be stressed when I come across challenges. I am learning that rewriting code is not the end of the world and my code leading up to the rewrite helps me to understand the theory behind what I am trying to achieve. 

# Analysis of Other Solutions
From Rahul Varma

```sh
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        return j
```

As always, another solution has managed to complete the problem in a faster time. The logic in my solution is very similar, however this solution is much more streamlined. Rahul's use of the second pointer as starting from the beginning of the array has shown me that I don't need to search far in the length of the array and that replacing values can start early. 