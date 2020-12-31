from typing import *

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        if intervals:
            intervals.sort()
            merged.append(intervals[0])
            for (start2, end2) in intervals[1:]:
                if merged[-1][1] >= start2:
                    merged[-1][1] = max(merged[-1][1], end2)
                else:
                    merged.append([start2, end2])
        return merged


if __name__ == '__main__':
    intervals = [[1,3],[3, 6], [2, 7], [8,10],[15,18]]
    
    answer = Solution().merge(intervals)
    print(answer)
