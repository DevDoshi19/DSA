n = 5
m = 6

edges = [[1,2],[1,3],[2,4],[3,4],[3,5],[4,5]]

# becase in worst can it can reach up to O(n) , in avg case it will also same as list O(1) 

my_dict = {i:[] for i in range(1,n+1)}

for u,v in edges:
    my_dict[u].append(v)
    my_dict[v].append(u)

print(my_dict)