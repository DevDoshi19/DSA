
from typing import List


class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        # n = len(parent)

        # adj = [[] for _ in range(n)]

        # for node in range(1, n):
        #     adj[parent[node]].append(node)

        # new_parent = parent[:]
        # last = [-1] * 26

        # stack = [(0, False, -1)]

        # while stack:
        #     node, exiting, previous = stack.pop()
        #     ch = ord(s[node]) - ord('a')

        #     if exiting:
        #         last[ch] = previous
        #         continue

        #     previous = last[ch]

        #     if previous != -1:
        #         new_parent[node] = previous

        #     last[ch] = node

        #     stack.append((node, True, previous))

        #     for child in reversed(adj[node]):
        #         stack.append((child, False, -1))

        # new_adj = [[] for _ in range(n)]

        # for node in range(1, n):
        #     new_adj[new_parent[node]].append(node)

        # order = []
        # stack = [0]

        # while stack:
        #     node = stack.pop()
        #     order.append(node)

        #     for child in new_adj[node]:
        #         stack.append(child)

        # result = [1] * n

        # for node in reversed(order[1:]):
        #     result[new_parent[node]] += result[node]

        # return result

        n = len(parent)
        adj_list = [[] for _ in range(n)]

        for i in range(1, n):
            adj_list[parent[i]].append(i)

        new_parent = parent[:]
        last = [-1] * 26

        def dfs(currentNode):
            ch = ord(s[currentNode]) - ord('a')

            nearestAncestor = last[ch]
            last[ch] = currentNode

            for child in adj_list[currentNode]:
                dfs(child)

            last[ch] = nearestAncestor

            if nearestAncestor != -1:
                new_parent[currentNode] = nearestAncestor

        dfs(0)

        new_adj = [[] for _ in range(n)]

        for node in range(1, n):
            new_adj[new_parent[node]].append(node)

        result = [1] * n

        def dfs_size(node):
            for child in new_adj[node]:
                dfs_size(child)
                result[node] += result[child]

        dfs_size(0)

        return result