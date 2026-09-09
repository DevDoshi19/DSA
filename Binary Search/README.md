# 🔎 Binary Search — Concepts & Patterns

Binary Search is not only about searching for a target in a sorted array. The real idea is:

> **Use a property to eliminate half of the possible search space.**

At every step, we look at `mid`, understand what it tells us, and remove the half that **cannot contain the answer**.

---

## 1. Normal Binary Search

In normal binary search, we have a sorted array and a `target`.

Example:

```text
[1, 3, 5, 7, 9]
         ↑
        mid
```

We compare `nums[mid]` with the target.

* If they are equal → we found the answer.
* If `nums[mid] < target` → target must be on the right.
* If `nums[mid] > target` → target must be on the left.

The important question is:

> **Which half can I prove does not contain the target?**

A common implementation is:

```python
low, high = 0, len(nums) - 1

while low <= high:
    mid = (low + high) // 2

    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        low = mid + 1
    else:
        high = mid - 1

return -1
```

Here, `low <= high` means there can still be at least one candidate that needs to be checked.

---

# 2. Lower Bound

Lower Bound means:

> **Find the first index where `nums[i] >= target`.**

Example:

```text
nums = [1, 2, 4, 4, 4, 7, 9]
target = 4

             ↓
[1, 2, 4, 4, 4, 7, 9]
       ↑
      first >= 4
```

The answer is index `2`.

The important condition is:

```python
nums[mid] >= target
```

Why `>=`?

Because both of these are valid for a lower bound:

```text
nums[mid] == target
nums[mid] > target
```

When the condition is true, `mid` could be the answer, but there might be an earlier valid position.

Therefore:

```python
high = mid - 1
```

If:

```python
nums[mid] < target
```

then `mid` and everything before it are too small:

```python
low = mid + 1
```

At the end, `low` points to the first position where `nums[i] >= target`.

### Remember:

```text
Lower Bound → first >= target
```

---

# 3. Upper Bound

Upper Bound means:

> **Find the first index where `nums[i] > target`.**

Example:

```text
nums = [1, 2, 4, 4, 4, 7, 9]
target = 4

                  ↓
[1, 2, 4, 4, 4, 7, 9]
                  first > 4
```

The answer is index `5`.

The important condition is:

```python
nums[mid] > target
```

Notice the difference:

```text
Lower Bound → >= target
Upper Bound → > target
```

If:

```python
nums[mid] > target
```

then `mid` could be the answer, but there may be an earlier one:

```python
high = mid - 1
```

Otherwise:

```python
low = mid + 1
```

At the end, `low` is the first position where `nums[i] > target`.

### Remember:

```text
Upper Bound → first > target
```

---

# 4. First and Last Occurrence

Lower and Upper Bound are extremely useful for finding repeated values.

Suppose:

```text
nums = [1, 2, 4, 4, 4, 7, 9]
target = 4
```

The first occurrence is:

```text
lower_bound(target)
```

because lower bound gives the first position where:

```text
nums[i] >= target
```

Since `4` exists, that is the first `4`.

The upper bound gives:

```text
first position > target
```

So the last occurrence is:

```text
upper_bound(target) - 1
```

Therefore:

```text
First occurrence → Lower Bound
Last occurrence  → Upper Bound - 1
```

Always remember to check whether the target actually exists before returning the result.

---

# 5. `mid` — Should We Keep It or Remove It?

This is one of the most important Binary Search concepts.

Whenever you decide where to move `low` or `high`, ask:

> **Can `mid` itself still be the answer?**

### If `mid` cannot be the answer

Remove it:

```python
low = mid + 1
```

or:

```python
high = mid - 1
```

### If `mid` can still be the answer

Keep it:

```python
high = mid
```

This is why different binary searches use different updates.

For example, in Find Minimum:

```python
high = mid
```

because `mid` itself could be the minimum.

In Peak:

```python
high = mid
```

because `mid` itself could be the peak.

But when we know `mid` definitely cannot be the answer:

```python
low = mid + 1
```

we remove it.

---

# 6. `low < high` vs `low <= high`

Don't memorize this as a random rule.

Instead, ask:

> **Am I checking individual candidates, or am I shrinking the range until one candidate remains?**

### `low <= high`

Use this when the remaining elements are candidates that still need to be checked.

Eventually:

```text
low > high
```

means there are no candidates left.

This is common in normal binary search.

---

### `low < high`

Use this when you want to keep shrinking the search range until only **one possible answer** remains.

Eventually:

```text
low == high
```

That remaining position is the answer.

This is common in problems like:

* Find Minimum
* Find Peak
* Peak Index

So think:

```text
low <= high → search until nothing remains

low < high → search until one answer remains
```

---

# 7. Search in Rotated Sorted Array

A rotated sorted array might look like:

```text
[4, 5, 6, 7, 0, 1, 2]
```

It is no longer completely sorted, but **one half is always sorted**.

At every iteration, first determine which half is sorted.

```python
if nums[low] <= nums[mid]:
```

Then the left half is sorted.

Now ask:

> Is the target inside that sorted range?

If yes → search left.

Otherwise → search right.

If the left half isn't sorted, the right half must be sorted.

Then ask:

> Is the target inside the sorted right range?

The important mental process is:

```text
1. Which half is sorted?
2. Is target inside that sorted half?
3. Keep that half or eliminate it.
```

Don't start by asking only whether the target lies between `low` and `mid`.

First identify the **sorted half**.

---

# 8. Find Minimum in Rotated Sorted Array

Example:

```text
[4, 5, 6, 7, 0, 1, 2]
```

We want the minimum.

The useful comparison is:

```python
nums[mid] > nums[high]
```

If this is true:

```text
nums[mid] > nums[high]
```

the minimum must be on the **right**.

So:

```python
low = mid + 1
```

Otherwise:

```text
nums[mid] <= nums[high]
```

the minimum can be at `mid` or somewhere to the left.

So we keep `mid`:

```python
high = mid
```

We continue until:

```text
low == high
```

and return:

```python
nums[low]
```

The important lesson is:

> **If `mid` can be the minimum, don't throw it away.**

---

# 9. Peak Problems

For a mountain/peak problem, compare:

```python
nums[mid]
nums[mid + 1]
```

If:

```python
nums[mid] < nums[mid + 1]
```

we are going uphill.

The peak must be on the right:

```python
low = mid + 1
```

If:

```python
nums[mid] > nums[mid + 1]
```

we are going downhill.

The peak can be `mid` or somewhere on the left:

```python
high = mid
```

Eventually:

```text
low == high
```

and that index is the peak.

The important question is:

> **Am I going uphill or downhill?**

---

# 10. Single Element in Sorted Array

Suppose every number appears twice except one:

```text
[1, 1, 2, 3, 3, 4, 4]
```

The pairs normally line up like:

```text
[0,1] [2,3] [4,5]
```

Before the single element, pairs start at even indexes.

After the single element, this pattern shifts.

We can make `mid` even and compare:

```python
nums[mid] == nums[mid + 1]
```

If they are a valid pair:

```python
low = mid + 2
```

The single element must be after that pair.

If they are not a pair:

```python
high = mid
```

The single element is at `mid` or before it.

Again, the same principle appears:

> **Can `mid` still be the answer?**

If yes, keep it.

---

# 11. Binary Search on Answer

This is a very important pattern.

Sometimes there isn't a sorted array to search.

Instead, the **possible answers themselves are ordered**.

Example: Koko Eating Bananas.

Possible eating speeds:

```text
1, 2, 3, 4, 5, 6, 7, ...
```

We can test whether a speed works.

For example:

```text
1  2  3  4  5  6  7  8
❌ ❌ ❌ ✅ ✅ ✅ ✅ ✅
```

Once a speed works, every larger speed also works.

This gives us a monotonic pattern:

```text
NOT POSSIBLE | POSSIBLE
```

We want the **first possible answer**.

So we can binary search the answer space.

For Koko:

```python
low = 1
high = max(piles)
```

For each candidate `k`, calculate how many hours are needed.

If:

```text
hours <= h
```

the speed works, so try a smaller speed:

```python
high = k
```

If:

```text
hours > h
```

the speed is too slow, so try a larger speed:

```python
low = k + 1
```

Finally:

```text
low
```

is the minimum valid speed.

The complexity is:

```text
O(n log(max(piles)))
```

because each candidate speed requires checking all `n` piles.

---

# 12. The Most Important Binary Search Mindset

Whenever you see a Binary Search problem, **don't immediately write code.**

First ask these questions:

### 1. What exactly am I searching for?

Is it:

* An exact value?
* First occurrence?
* Last occurrence?
* Minimum?
* Maximum?
* A boundary?
* A feasible answer?

### 2. What property changes around the answer?

For example:

```text
< target | >= target
```

or:

```text
<= target | > target
```

or:

```text
NOT POSSIBLE | POSSIBLE
```

### 3. What does `mid` tell me?

Find the one useful observation you can make from `mid`.

### 4. Which half can I PROVE cannot contain the answer?

Don't choose a side because it "looks right."

You should be able to explain why the other half is impossible.

### 5. Can `mid` itself still be the answer?

If yes:

```text
KEEP mid
```

If no:

```text
REMOVE mid
```

This single question prevents many off-by-one errors.

---

# 13. Avoiding Over-Complicated Binary Search

A common mistake is adding too many variables and conditions.

For example, you might think:

```text
mini
peak
mid - 1
mid + 1
extra checks
special cases
```

before identifying the actual property.

Instead, stop and ask:

> **"What is the ONE property that lets me eliminate half the search space?"**

For Peak:

```text
nums[mid] vs nums[mid + 1]
```

For Find Minimum:

```text
nums[mid] vs nums[high]
```

For Rotated Search:

```text
Which half is sorted?
```

For Koko:

```text
Does this speed work?
```

The goal is not to create more conditions.

The goal is to find the **minimum sufficient condition**.

---

# 14. Binary Search Cheat Sheet

```text
Normal Search
→ Find exact target
→ while low <= high

Lower Bound
→ First >= target
→ condition: nums[mid] >= target

Upper Bound
→ First > target
→ condition: nums[mid] > target

First Occurrence
→ Lower Bound

Last Occurrence
→ Upper Bound - 1

Rotated Search
→ Find which half is sorted
→ Check whether target belongs to that half

Find Minimum
→ nums[mid] > nums[high] → go right
→ otherwise → keep mid and go left

Peak
→ nums[mid] < nums[mid+1] → go right
→ otherwise → keep mid and go left

Single Element
→ Use even/odd pair pattern

Binary Search on Answer
→ Search possible answers
→ Test whether mid works
→ NOT POSSIBLE | POSSIBLE
→ Find first possible answer
```

---

# 🧠 Final Rule

Don't memorize 20 different Binary Search solutions.

Instead remember:

```text
                 BINARY SEARCH
                      │
                      ↓
             Find the property
                      │
                      ↓
              Look at mid
                      │
                      ↓
        Which half can be eliminated?
                      │
                      ↓
          Can mid still be answer?
                 /           \
               YES            NO
                │              │
             KEEP it       REMOVE it
                │              │
                └──────┬───────┘
                       ↓
                 Shrink search
                       ↓
                  Find answer
```

> **Binary Search is fundamentally about eliminating half of the search space using a property.**

Once you can identify that property, the code is usually the easy part.
