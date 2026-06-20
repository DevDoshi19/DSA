class Meeting:
    def __init__(self, start, end, position):
        self.start = start
        self.end = end
        self.position = position

class Solution:
    
    def activitySelection(self, start, finish):
        #code here
        n = len(start)
        # Create Meeting objects with start, end, and position
        meets = [Meeting(start[i], finish[i], i + 1) for i in range(n)]
        
        # Sort meetings by end time (then by start time if needed)
        meets.sort(key=lambda x: (x.end, x.start))
        
        lastTime = meets[0].end
        count = 1  # Select the first meeting by default
        
        # Iterate through the rest of the meetings
        for i in range(1, n):
            if meets[i].start > lastTime:
                count += 1
                lastTime = meets[i].end
                
        return count    
                