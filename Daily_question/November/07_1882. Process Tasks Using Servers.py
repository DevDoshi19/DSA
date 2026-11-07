import heapq

# both approach are correct and have same time complexity : O((n + m) log n), where n is the number of servers and m is the number of tasks. The first approach processes tasks in order, while the second approach uses a time variable to manage task assignment more efficiently.
"""
What is we doing is :
- simply take the minimum weight server and assign the task to it and then push it to busy servers with the time when it will be free again.
- now we maily check 3 conditions :
    1. if in busy servers there is any server which is free at the current time then we pop up and move it into avaliable servers.
    2. if there is no avaliable server then we pop the minimum time server from busy servers and assign the task to it and push it back to busy servers with the new time when it will be free again.
    3. if there is avaliable server then we pop the minimum weight server from avaliable servers and assign the task to it and push it back to busy servers with the new time when it will be free again.

- at every point when we assign server to the task we store the index of that server in the ans array.
"""
class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        available = [(q,i) for i,q in enumerate(servers)]
        heapq.heapify(available)
        
        busy = []
        ans = [-1] * len(tasks)
 
        for i,task in enumerate(tasks):
            
            while busy and busy[0][0] <= i :
                freetime,weight,index = heapq.heappop(busy)
                heapq.heappush(available,(weight,index))

            if not available :
                freetime,weight,index = heapq.heappop(busy)
                ans[i] = index
                heapq.heappush(busy,(freetime+task,weight,index))
                
            else:
                weight,index = heapq.heappop(available)
                ans[i] = index
                heapq.heappush(busy,(i+task,weight,index))
                
        return ans

# in this apporch we are kept track of time , cause we know that time will always increase and we can assign the task to the server which is free at that time. So we can use time variable to keep track of the current time and assign the task to the server which is free at that time.
class Solution2:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:

        available = [(weight, i) for i, weight in enumerate(servers)]
        heapq.heapify(available)

        busy = []
        ans = [-1] * len(tasks)

        time = 0

        for i, task in enumerate(tasks):

            time = max(time, i)

            while busy and busy[0][0] <= time:
                freetime, weight, index = heapq.heappop(busy)
                heapq.heappush(available, (weight, index))

            if not available:
                time = busy[0][0]

                while busy and busy[0][0] <= time:
                    freetime, weight, index = heapq.heappop(busy)
                    heapq.heappush(available, (weight, index))

            weight, index = heapq.heappop(available)
            ans[i] = index
            heapq.heappush(busy, (time + task, weight, index))

        return ans
