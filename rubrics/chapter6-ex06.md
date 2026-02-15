# Grading Rubric: Chapter 6, Exercise 6
## myRange Function 🔢

---

## 📋 What You're Building

Replicate Python's `range()` but return a list:
- `myRange(stop)` → [0, 1, ..., stop-1]
- `myRange(start, stop)` → [start, ..., stop-1]
- `myRange(start, stop, step)` → with step

**Cannot use built-in `range()`!**

---

## 🎯 Point Breakdown (100 Total)

| Category | Points |
|----------|--------|
| **Single Argument** | 25 |
| **Two Arguments** | 25 |
| **Three Arguments** | 30 |
| **Edge Cases** | 20 |

---

## 💻 Implementation

```python
def myRange(start, stop=None, step=None):
    """Return list like range(), without using range()"""
    
    # Handle parameter defaults
    if stop is None:
        # myRange(10) → start=0, stop=10, step=1
        stop = start
        start = 0
        step = 1
    elif step is None:
        # myRange(1, 10) → step=1
        step = 1
    
    # Handle edge cases
    if step == 0:
        return []
    if step > 0 and start >= stop:
        return []
    if step < 0 and start <= stop:
        return []
    
    # Build list
    result = []
    current = start
    
    if step > 0:
        while current < stop:
            result.append(current)
            current += step
    else:
        while current > stop:
            result.append(current)
            current += step
    
    return result
```

---

## ✅ Test Cases

| Call | Output |
|------|--------|
| myRange(5) | [0, 1, 2, 3, 4] |
| myRange(1, 5) | [1, 2, 3, 4] |
| myRange(0, 10, 2) | [0, 2, 4, 6, 8] |
| myRange(10, 0, -1) | [10, 9, ..., 1] |
| myRange(0, 10, 0) | [] |

---

## Key Concepts

- Default parameters
- Parameter logic
- Loop construction
- Edge case handling
