# Stats
Time: 28 minutes

Runtime: $O(n)$

Memory: no auxilary memory

# Approach
I started by thinking of this problem in terms of insertion sort: whenever the pointer pointed to an element that was equal to the searched value, the program would send it to the back. At least, it would send it as far back as it could without going past where the rest of the moved elements went. There were a lot of assertions. For instance, the checking if the element was equal to the searched value must only take place if the element was not in the "garbage" already. Secondly, if the "garbage" wasn't properly calculated, it needed to be recalculated.

I am quite proud of this approach, even if the runtime is suboptimal, according to LeetCode. I believe that this is the best program I could run.

# Analysis of Other Solutions

```sh
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1
        return index
```

This did humble me. I think I was very focused on retaining all of the values that I failed to see that the values after k weren't necessary. I think as soon as I started adjusting based on edge cases, I should have started my approach over and recognized what was vitally important to the problem.