# Grading Rubric: Chapter 6, Exercise 2
## Decomposed Newton's Method 🧩

---

## 📋 What You're Building

Decompose Newton's method into three cooperating functions:
- `improveEstimate(x, estimate)` - Compute new approximation
- `limitReached(x, estimate)` - Test if close enough
- `newton(x)` - Main function using above helpers

**Required signatures:**
```python
newton(x): Returns the square root of x
improveEstimate(x, estimate): Returns (estimate + x / estimate) / 2
limitReached(x, estimate): Returns True if |x - estimate²| <= TOLERANCE
```

---

## 🎯 Point Breakdown (100 Total)

| Category | Points |
|----------|--------|
| **improveEstimate()** | 30 |
| **limitReached()** | 30 |
| **newton()** | 40 |

---

## 💻 Implementation

```python
TOLERANCE = 0.000001

def improveEstimate(x, estimate):
    """Return improved estimate using Newton's formula"""
    return (estimate + x / estimate) / 2

def limitReached(x, estimate):
    """Return True if estimate is close enough"""
    return abs(x - estimate ** 2) <= TOLERANCE

def newton(x):
    """Return square root estimate using helper functions"""
    estimate = 1.0
    while not limitReached(x, estimate):
        estimate = improveEstimate(x, estimate)
    return estimate
```

---

## Key Concepts

- Function decomposition
- Helper functions
- Separation of concerns
- Code reusability
