If the problem is:
Find whether a pattern occurs continuously inside a string.

Think:
Substring
   ↓
Pattern matching
   ↓
KMP / Z-algorithm / rolling hash / etc.

If the problem is:
Can I delete some characters from the text and obtain the pattern?

Think:
Subsequence
   ↓
Two pointers
   ↓
HashMap + positions + binary search

---

| Concept | What are we asking? | Typical technique |
|---|---|---|
| **Substring** | Is pattern continuously inside text? | **KMP** |
| **Subsequence** | Can pattern be obtained while preserving order, allowing gaps? | **Two pointers** |
| **Many subsequence queries** | Check many patterns against same text efficiently | **Positions + Binary Search** |
| **Prefix = Suffix** | Longest border of a string? | **LPS** |
| **Repeated pattern** | Is string made of repeated smaller string? | **LPS** |

# Questions 

When you see a string problem, ask these questions in this order:
**Question 1**
Does the pattern have to be continuous?
YES
 ↓
Substring / pattern matching
 ↓
KMP may be useful

**Question 2**
If not:
Can I skip characters while maintaining order?
YES
 ↓
Subsequence

Then ask:

**Question 3**
One query or MANY queries against the same text?
ONE
 ↓
Two pointers

MANY
 ↓
Preprocess text
 ↓
character → positions
 ↓
Binary Search