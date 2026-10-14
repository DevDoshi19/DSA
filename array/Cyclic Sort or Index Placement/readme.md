You're actually understanding more of this than you think! 🔥 You've already identified the two biggest ideas:

1. We only care about numbers from `1` to `n`.
2. Each number has a correct index: number `x` belongs at index `x - 1`.

Now let's connect those ideas so you understand why the algorithm works, not just what each line does.

## 1. What is this pattern called?

The pattern is commonly called Cyclic Sort or Index Placement.

It is useful when a problem gives you an array of numbers in a known range and asks you to find missing numbers, duplicates, or misplaced values.

The core idea is:

> Instead of sorting the array using comparisons, put each value directly into the index where it belongs.

For First Missing Positive, the correct arrangement is:

Index

## 0 · 1 · 2 · 3

Expected values

## 1 · 2 · 3 · 4

The relationship is always:

\\[ \text{correct index}=\text{value}-1 \\]

For example, `3` belongs at index `2`.

One subtle point: this is not necessarily sorting into ascending order by comparing adjacent elements. We're placing each valid number at its designated index. That distinction is what makes the technique powerful.

## 2. Why can we ignore numbers outside `1` to `n`?

Suppose an array has four elements:

```
nums = [3, 100, -2, 1]
```

Its length is `n = 4`.

The smallest missing positive must be one of:

`1, 2, 3, 4, 5`

Why? Because if `1, 2, 3, 4` all exist, then `5` is definitely the answer.

Therefore:

- `-2` cannot be the answer because it isn't positive.
- `100` cannot be the answer because `1` through `5` are the only candidates we need to distinguish.

We can ignore values outside `1` through `n` during placement. They don't need their own correct index.

## 3. Let's dry-run your exact code

We'll use:

```
nums = [3, 4, -1, 1]
```

Your rearrangement loop is:

```
for i in range(n):    while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:        nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
```

The most important thing to understand is that `i` stays fixed while the `while` loop keeps swapping. We don't move to the next index until the current position contains a value that doesn't need a useful swap.

### Placement walkthrough

Step 7 of 7

Index 0

# 1

Index 1

# -1

Index 2

# 3

Index 3

# 4

nums[3] == nums[4 - 1]

The value is 4, and its correct index is 3. It is already in place, so no swap is needed.

PreviousNext step&#x20;

Placement complete!

The array is `[1, -1, 3, 4]`. Notice that `2` is missing from its correct index, index `1`.

## 4. Why does the `while` condition have two checks?

Let's break down this line:

```
while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
```

Check A: Is the value in the valid range?

```
1 <= nums[i] <= n
```

If the current value is `-1`, `0`, or `100`, don't try to place it.

Check B: Is the destination holding a different value?

```
nums[nums[i] - 1] != nums[i]
```

If the destination already contains the same value, swapping would accomplish nothing.

For example, with `[1, 1]`, the first `1` belongs at index `0`, but index `0` already contains `1`. The condition is false, so we avoid repeatedly swapping identical values.

Python evaluates `and` from left to right and short-circuits. That means it checks the range first, so an invalid value isn't used to calculate an array index.

## 5. Why do we scan the array again?

After rearrangement:

```
for i in range(n):    if nums[i] != i + 1:        return i + 1return n + 1
```

Every index `i` is expected to contain `i + 1`.

For `[1, -1, 3, 4]`:

| Index | Expected | Actual | Result          |
| ----- | -------- | ------ | --------------- |
| 0     | 1        | 1      | Correct         |
| 1     | 2        | -1     | First mismatch! |

The first mismatch tells us that `2` is missing. If there is no mismatch, all numbers from `1` through `n` are present, so the answer is `n + 1`.

## 6. Complexity — why isn't this \\(O(n^2)\\)?

Even though there's a `while` loop inside a `for` loop, the total number of successful swaps is at most \\(O(n)\\).

Each successful swap puts a valid number into its correct position. Once a position contains its correct value, that value won't need to be moved again. So we perform at most \\(n\\) useful placements, plus the final scan.

- Time: \\(O(n)\\)
- Auxiliary space: \\(O(1)\\)

## 7. The pattern to remember

When you see an array problem involving numbers in the range `1..n`, ask yourself:

1. Can each number tell me its correct index?
2. Can I place values directly into those positions?
3. After placement, can a mismatch reveal the missing or incorrect value?

That's the reusable cyclic sort / index-placement pattern. You don't need to memorise this particular solution; understand why each swap makes progress, and you'll be able to rebuild it in another problem.