# ============================================================
# Kth Missing Positive Number - Binary Search
# LeetCode 1539
# ============================================================

# Problem:
# Given a sorted array of distinct positive integers, find the
# k-th positive integer that is missing from the array.
#
# Example:
# arr = [2, 3, 4, 7, 11], k = 5
# Missing = [1, 5, 6, 8, 9, ...]
# Answer = 9


# ------------------------------------------------------------
# KEY OBSERVATION
# ------------------------------------------------------------

# If NO numbers were missing, then at index i the value should be:
#
#     i + 1
#
# Example:
# index:       0   1   2   3   4
# expected:    1   2   3   4   5
#
# But our array is:
#              2   3   4   7  11
#
# The difference between actual and expected tells us how many
# positive numbers are missing before arr[i].
#
#     missing = arr[i] - (i + 1)
#
# Example at index 3:
#     arr[3] = 7
#     expected = 3 + 1 = 4
#     missing = 7 - 4 = 3
#
# The 3 missing numbers before 7 are:
#     1, 5, 6


# ------------------------------------------------------------
# WHY CAN WE USE BINARY SEARCH?
# ------------------------------------------------------------

# As we move from left to right, the number of missing elements
# never decreases.
#
# Example:
#     arr = [2, 3, 4, 7, 11]
#
#     missing = [1, 1, 1, 3, 6]
#
# This gives a monotonic pattern:
#
#     1  1  1  3  6
#                 ↑
#
# We need to find the boundary where:
#
#     missing >= k
#
# Therefore:
#
#     missing < k
#         -> not enough missing numbers
#         -> answer must be on the RIGHT
#         -> low = mid + 1
#
#     missing >= k
#         -> we have reached enough missing numbers
#         -> answer is at or before this position
#         -> high = mid - 1


# ------------------------------------------------------------
# BINARY SEARCH
# ------------------------------------------------------------

# We search over ARRAY INDICES, not over the answer itself.
#
# low = 0
# high = len(arr) - 1
#
# Find the first index where:
#
#     arr[mid] - (mid + 1) >= k


# ------------------------------------------------------------
# AFTER BINARY SEARCH
# ------------------------------------------------------------

# When the loop finishes:
#
#     high = last index where missing < k
#     low  = first index where missing >= k
#
# There are high + 1 elements before that position.
#
# The answer can be calculated as:
#
#     answer = k + (high + 1)
#
# Therefore:
#
#     return high + 1 + k


# ------------------------------------------------------------
# COMPLETE CODE
# ------------------------------------------------------------

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        low, high = 0, len(arr) - 1

        while low <= high:
            mid = (low + high) // 2

            # Number of missing positive integers before arr[mid]
            missing = arr[mid] - (mid + 1)

            if missing < k:
                # Not enough missing numbers yet.
                # Search on the right.
                low = mid + 1
            else:
                # We already have k or more missing numbers.
                # Search for an earlier position.
                high = mid - 1

        return high + 1 + k


# ------------------------------------------------------------
# DRY RUN
# ------------------------------------------------------------

# arr = [2, 3, 4, 7, 11]
# k = 5
#
# Initial:
# low = 0, high = 4
#
# mid = 2
# arr[mid] = 4
# missing = 4 - 3 = 1
#
# 1 < 5
# -> not enough missing numbers
# -> low = 3
#
# mid = 3
# arr[mid] = 7
# missing = 7 - 4 = 3
#
# 3 < 5
# -> not enough missing numbers
# -> low = 4
#
# mid = 4
# arr[mid] = 11
# missing = 11 - 5 = 6
#
# 6 >= 5
# -> enough missing numbers
# -> high = 3
#
# Now:
# low = 4
# high = 3
#
# Search ends.
#
# answer = high + 1 + k
#        = 3 + 1 + 5
#        = 9


# ------------------------------------------------------------
# CORE INTUITION TO REMEMBER
# ------------------------------------------------------------

# 1. At index i, the expected value is i + 1.
# 2. Actual - expected = number of missing values before it.
# 3. Missing count increases as we move right.
# 4. Binary search for the first position where missing >= k.
# 5. If missing < k -> go RIGHT.
# 6. If missing >= k -> go LEFT.
# 7. After search, answer = high + 1 + k.