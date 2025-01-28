# Stats
Time to solution: 96 minutes

Runtime: $O(m+n)$

Memory: no auxiliary memory
# Initial Approach

When I first started solving this problem, I attempted to work from the 0th index onwards, checking the pointer in each nums array and inserting or keeping the element in `nums1` depending on the comparision. The issue with checking from the front is that there were often times where the program would not know when to stop, especially checking values from the intial array.

I will admit that it took a long time (60 minutes) to discover that this approach was not at all optimal. This is signaling to me the reasoning as to why I am embarking on this endeavor - to increase my coding ability to reflect my skills.

# Secondary Approach

After it became increasingly clearer that starting from the front was not working, I reached an epiphany: what if I started from the back? It was very simple to code this solution, and it passed all the testcases immediately. This experience has shown me how important it is to take a step back, breathe, and try a new approach

# Runtime

This program runs in $O(m+n)$ time because it checks each value exactly once, and the length of the combined arrays is $m+n$. This is the optimal solution because every value must be checked in order to ensure that the list is properly sorted.