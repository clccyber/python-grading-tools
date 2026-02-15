# Grading Rubric: Chapter 6, Exercise 3
## isSorted Predicate ✓

---

## 📋 What You're Building

Function that checks if a list is sorted in ascending order:
- `isSorted(data)` returns True/False
- Empty list is sorted
- Duplicates allowed (equal values okay)

---

## 🎯 Point Breakdown (100 Total)

| Category | Points |
|----------|--------|
| **Correct Logic** | 80 |
| **Edge Cases** | 20 |

---

## 💻 Implementation

```python
def isSorted(data):
    """Return True if list is sorted ascending"""
    if len(data) <= 1:
        return True
    
    for i in range(len(data) - 1):
        if data[i] > data[i + 1]:
            return False
    
    return True
```

---

## ✅ Test Cases

| Input | Output |
|-------|--------|
| [] | True |
| [5] | True |
| [1, 2, 3, 4, 5] | True |
| [1, 2, 2, 3] | True |
| [5, 4, 3, 2, 1] | False |
| [1, 3, 2, 4] | False |

---

## Key Concepts

- Predicates (boolean functions)
- List traversal
- Pair-wise comparison
- Edge case handling
