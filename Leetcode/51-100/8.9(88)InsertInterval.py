# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def insert(self, intervals, newInterval):
        left = newInterval.start
        right = newInterval.end
        index = 0
        insertP = 0
        while index < len(intervals):
            temp = intervals[index]
            tend = temp.end
            tsta = temp.start
            if tend >= right and tsta <= left:
                insertP = -1
                break
            elif tend <= right and tsta >= left:
                del intervals[index]
            elif tend >= left and tend <= right:
                left = tsta
                del intervals[index]
                insertP = index
            elif tsta <= right and tsta >= left:
                right = tend
                del intervals[index]
                insertP = index 
            else:
                index += 1
                if  tend< left:
                    insertP = index
        if insertP != -1:
            intervals.insert(insertP,Interval(s=left,e=right))
        return intervals
            
            
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        
