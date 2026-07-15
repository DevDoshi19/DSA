"""https://www.geeksforgeeks.org/problems/implementing-floyd-warshall2042/1"""

class Solution:
	def floydWarshall(self, dist):
		#Code here
		n = len(dist)
		
		for val in range(n) :
		    for i in range(n) :
		        for j in range(n):
		            if dist[i][val] != 10 **8 and dist[val][j] != 10 **8 :
		                dist[i][j] = min(dist[i][j],dist[i][val]+dist[val][j])
		            
		