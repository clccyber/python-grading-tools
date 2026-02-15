# Grading Rubric: Chapter 6, Exercise 1
## Newton's Method for Square Roots 🔢

---

## 📋 What You're Building

Package Newton's method in a function:
- Function `newton(x)` returns square root estimate
- Interactive `main()` allows repeated calculations
- Compare your estimate to Python's `math.sqrt()`

**Example:**
```
Enter a positive number or enter/return to quit: 2
The program's estimate is 1.4142135623746899
Python's estimate is      1.4142135623730951
```

---

## 🎯 Point Breakdown (100 Total)

| Category | Points |
|----------|--------|
| **newton() Function** | 70 |
| **Accuracy** | 20 |
| **main() Function** | 10 |

---

## 💻 Newton's Method Algorithm

```python
def newton(x):
    """Estimate the square root of x"""
    TOLERANCE = 0.000001
    estimate = 1.0
    
    while True:
        estimate = (estimate + x / estimate) / 2
        difference = abs(x - estimate ** 2)
        if difference <= TOLERANCE:
            break
    
    return estimate

def main():
    import math
    while True:
        x = input("Enter a positive number or enter/return to quit: ")
        if x == "":
            break
        x = float(x)
        print(f"The program's estimate is {newton(x)}")
        print(f"Python's estimate is      {math.sqrt(x)}")
```

---

## ✅ Test Cases

| Input | Expected Output (approx) |
|-------|-------------------------|
| 2 | 1.414214 |
| 4 | 2.0 |
| 9 | 3.0 |
| 16 | 4.0 |
| 25 | 5.0 |

---

## Key Concepts

- Function encapsulation
- Newton's method iteration
- Tolerance-based convergence
- Interactive loops (quit on empty)
