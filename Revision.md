## Complete DSA Revision 🧠

---

## 1. HEAP 📦

```
Min Heap → smallest on top
Max Heap → largest on top (negate values in Python!)

Key functions:
heapq.heappush(heap, val)
heapq.heappop(heap)
heapq.heapify(list)
heap[0]  → peek min

Problems solved:
→ Kth Largest Element
→ Merge K Sorted Lists
→ Top K Frequent Elements

Pattern:
→ Kth largest/smallest  → Min heap of size K
→ K-way merge           → Push all heads, pop min, push next
```

---

## 2. SLIDING WINDOW 🪟

```
Fixed window:
→ window size is given (len(s1))
→ add right, remove left, check

Variable window:
→ expand right until invalid
→ shrink left until valid again

Problems solved:
→ Permutation in String    (fixed)
→ Longest Repeating Char   (variable)
→ Minimum Window Substring (variable)

Key variables:
→ left, right
→ window frequency map
→ have, need (for complex conditions)
```

---

## 3. TWO POINTERS 👆👆

```
When to use:
→ Sorted array
→ Find pair with condition
→ Left/right squeeze

Problems solved:
→ Valid Palindrome
→ Container With Most Water
→ Sort Colors (3 pointers!)

Pattern:
→ if condition: move left
→ else: move right
```

---

## 4. MONOTONIC STACK 📚

```
Stack stays in increasing/decreasing order!

When to use:
→ Next greater/smaller element
→ Temperature problems
→ Histogram problems

Problems solved:
→ Daily Temperatures

Pattern:
→ Store INDICES not values!
→ While stack and condition: pop and calculate
→ Push current index
```

---

## 5. LINKED LIST 🔗

```
Golden rules:
→ Always use DUMMY node!
→ Store next before changing pointers!
→ Draw it before coding!

Problems solved:
→ Copy List with Random Pointer  (HashMap)
→ Reorder List                   (Find mid + Reverse + Merge)
→ Remove Nth From End            (Two pointers with gap n)
→ Merge K Sorted Lists           (Min Heap)

Key patterns:
→ Find middle     → slow/fast pointers
→ Reverse list    → prev, curr, front
→ Detect cycle    → slow/fast meet
```

---

## 6. BINARY SEARCH 🔍

```
Template:
left, right = 0, n-1
while left <= right:
    mid = (left+right)//2
    if nums[mid] == target: return mid
    elif nums[mid] < target: left = mid+1
    else: right = mid-1

Problems solved:
→ Basic Binary Search
→ Search in Rotated Array
→ Find Minimum in Rotated Array

Key insight:
→ Rotated array → one half always sorted!
→ Check which half is sorted
→ Check if target is in that half
```

---

## 7. BACKTRACKING 🔄

```
Template:
def backtrack(index, current):
    if success: 
        result.append(current.copy())
        return
    if invalid: 
        return
    
    # include
    current.append(nums[index])
    backtrack(index, current)    # same index = reuse
    current.pop()
    
    # exclude
    backtrack(index+1, current)  # next index = no reuse

Problems solved:
→ Subsets
→ Permutations    (visited array!)
→ Combination Sum (reuse allowed → same index!)

Key difference:
→ Subsets/Combinations → index moves forward
→ Permutations         → visited array, loop all
→ Reuse allowed        → pass same index
→ No reuse             → pass index+1
```

---

## 8. TREES 🌳

```
Key traversals:
Inorder   (L→Root→R) → BST sorted order!
Preorder  (Root→L→R) → copy tree
Postorder (L→R→Root) → delete tree
Level order           → BFS with queue!

Problems solved:
→ Max Depth          → 1 + max(left, right)
→ Invert Tree        → swap left/right at every node
→ Level Order        → BFS with level_size trick!
→ Same Tree          → check null + value + recurse
→ Subtree of Tree    → isSame() + dfs()
→ Diameter           → self.maxi = left+right at each node
→ Balanced Tree      → return False if diff > 1
→ Path Sum           → check at LEAF node only!
→ LCA of BST         → both smaller→left, both larger→right
→ Kth Smallest BST   → inorder = sorted!

Universal tree template:
def dfs(node):
    if not node: return base_case
    left = dfs(node.left)
    right = dfs(node.right)
    return combine(left, right)

Null checking pattern (ALWAYS first!):
if not node1 and not node2: return True
if not node1 or not node2:  return False
```

---

## 9. ARRAYS 📊

```
Problems solved:
→ Kth Largest          → Heap / QuickSelect
→ Product Except Self  → Left pass × Right pass
→ Merge Intervals      → Sort + merge with max()!
→ Sort Colors          → Dutch National Flag (low/mid/high)
→ Rotate Image         → Reverse rows + Transpose
→ Top K Frequent       → Bucket sort / Heap

Key tricks:
→ Prefix product  → two pass (left then right)
→ Merge intervals → sort first, then max(end points)
→ Dutch flag      → 3 pointers, mid is traverser!
→ Rotate matrix   → transpose = j starts from i+1!
```

---

## 10. PREFIX SUM + HASHMAP 🗺️

```
When to use:
→ Count subarrays with sum k   → HashMap stores frequency
→ Longest subarray sum 0       → HashMap stores first index
→ Equal 0s and 1s              → Replace 0 with -1!

Template:
prefix = 0
map = {0: 1}   # COUNT problems
map = {0: -1}  # LONGEST problems

for num in nums:
    prefix += num
    # COUNT:   result += map.get(prefix-k, 0)
    # LONGEST: result = max(result, i - map[prefix])
    # Store:
    # COUNT:   map[prefix] = map.get(prefix,0) + 1
    # LONGEST: if prefix not in map: map[prefix] = i

Problems solved:
→ Subarray Sum Equals K
→ Contiguous Array
→ Product of Array Except Self
```

---

## Common Mistakes You Make ⚠️

```
1. node.left instead of node.right → dry run!
2. arr[n] instead of arr[n-1]      → check bounds!
3. Forgetting dummy node           → always in linked list!
4. Not returning recursive result  → dfs(node) not just calling!
5. Rebuilding Counter every iter   → just add/remove one char!
6. Checking total before leaf      → check AT leaf node!
7. Not propagating False in trees  → check if child returned False!
8. j from 0 in transpose           → start from i+1!
```

---

## Pattern Recognition Cheatsheet 🎯

```
"Find kth largest/smallest"      → Heap
"Subarray with condition"        → Sliding Window
"Sorted array, find target"      → Binary Search
"All combinations/permutations"  → Backtracking
"Next greater element"           → Monotonic Stack
"Linked list middle/cycle"       → Fast/Slow pointers
"Subarray sum = k"               → Prefix Sum + HashMap
"Tree path/depth/structure"      → DFS recursion
"Level by level"                 → BFS with queue
"K sorted sources"               → Min Heap (K-way merge)
"Pair in sorted array"           → Two Pointers
```

---

## Your Progress 📊

```
Topic              Readiness
─────────────────────────────
Two Pointers       █████████░  90%
Sliding Window     █████████░  90%
Stack              █████████░  90%
Heap               ████████░░  80%
Linked List        ████████░░  80%
Arrays             ████████░░  80%
Binary Search      ███████░░░  70%
Backtracking       ███████░░░  70%
Trees              ███████░░░  70%  ← improved!
Prefix Sum         █████░░░░░  50%
Graphs             ░░░░░░░░░░   0%
DP                 ░░░░░░░░░░   0%
─────────────────────────────
Overall Google     █████░░░░░  60%  ← up from 55%!
```

---

You're improving every session! 💪
Ready to push to next level? 🚀