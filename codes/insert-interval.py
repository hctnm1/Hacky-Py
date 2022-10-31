class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if intervals is None or len(intervals) == 0:
            return [newInterval]
        intervals.sort(key=lambda x:x.start)
        pos = 0
        while pos < len(intervals):
            # left of pos
            if newInterval.end < intervals[pos].start:
                intervals.insert(pos, newInterval)
                return intervals
            # overlap with pos
            if self.check_overlap(intervals[pos], newInterval):
                temp = intervals.pop(pos)
                newInterval = self.merge_intervals(temp, newInterval)
            else:
                pos += 1
        if len(intervals) == 0 or pos == len(intervals):
            intervals.append(newInterval)
        return intervals

    def check_overlap(self, curr_int, new_int):
        if curr_int.start <= new_int.start:
           if curr_int.end > new_int.start:
               return True
        else:
            if curr_int.start <= new_int.end:
                return True
        return False

    def merge_intervals(self, int1, int2):
        temp_int = Interval()
        temp_int.start = min([int1.start, int2.start])
        temp_int.end = max([int1.end, int2.end])
        return temp_int
