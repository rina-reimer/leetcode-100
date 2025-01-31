# Stats
Time: 29 minutes

Runtime: $O(n)$

Memory: $O(1)$

# Approach
I started the pointer at index 1, and for every element that was not in the middle of two same-valued elements, it was kept in the array. Should it be an element in the middle, the secondary pointer would not move, making it so that only elements that had one duplicate would be kept. I was quite proud of the speed at which I achieved this solution, even though I am in the bottom 5% of runtime.

# Analysis of Other Solutions
From Alanto

```sh
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        current = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                count = 0
                nums[current] = nums[i]
                current += 1
            else:
                count += 1
                if count <= 1:
                    nums[current] = nums[i]
                    current += 1
        return current
```

The use of a `count` variable is very useful, and it definitely helps the runtime. I do think that this is very similar to my solution and that the runtime problem is likely caused by my use of Python, a notoriously slow language.