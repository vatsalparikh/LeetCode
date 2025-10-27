class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        minimum = 0
        intervals.sort(key = lambda x : x[1])
        prev = intervals[0]
        for index in range(1, len(intervals)):
            if intervals[index][0] >= prev[1]:
                prev = intervals[index]
            else:
                minimum += 1
        return minimum


'''
The intuition behind is greedy. The idea is that if I have one day to schedule 100 intervals, for example, I would want to choose the interval that ends earliest. This will allow maximization of the number of intervals that can be scheduled for that day. If I take the intervals that ends later, I am choosing a less efficient interval. Didn't go into details why greedy works here, but the intuition does make sense. 

There is also a DP solution to it but it's unnecessary and I don't have time!

We might take [1,4] first (starts earliest).
But now everything else overlaps with it!
→ We can only keep 1 interval.
→ Must remove 3 intervals.

[1 ─────── 4]
								 [2 ─ 3]
													[3 ─── 5]
																[4 ─── 6]
																
Now ask: Which interval blocks the timeline the least?
→ [2,3] ends first. Take it.
Now the timeline is free from 3 onward.

Next, skip [1,4] (ends at 4 but starts at 1 → overlaps with [2,3]).
Next: [3,5] → starts at 3, which is exactly when last ended → ✅ no overlap. Take it.
Now free from 5 onward.

Next: [4,6] → starts at 4, but we’re busy until 5 → ❌ overlap. Skip.

✅ We kept 2 intervals: [2,3] and [3,5].

Can we do better? Try any other combo—you’ll never get 3 non-overlapping intervals here.
So 2 is maximum → remove 4 – 2 = 2 intervals.
'''