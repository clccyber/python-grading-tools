# Grading Rubric: Chapter 1, Exercise 4
## Circle Area

---

## 📋 What You're Building

Compute the area of a circle:
- **File:** `circle.py`
- **Formula:** `area = 3.14 × radius²`
- **Concept:** Using exponentiation operator `**`

**Example:**
```
Enter the radius: 5
The area is 78.5 square units.
```

---

## 🎯 Point Breakdown (100 Total)

| Category | Points |
|----------|--------|
| **Prompts for Radius** | 25 |
| **Uses Correct Formula** | 40 |
| **Uses `**` Operator** | 15 |
| **Output with Label** | 20 |

---

## 💻 Implementation

```python
# circle.py
radius = float(input("Enter the radius: "))
area = 3.14 * radius ** 2
print("The area is", area, "square units.")
```

---

## ✅ What to Check

### Input (25 pts)
- ✓ Prompts for radius
- ✓ Converts to float
- ✓ Clear prompt message

### Formula (55 pts)
- ✓ Uses `3.14 * radius ** 2` (40 pts)
- ✓ Uses exponentiation `**` operator (15 pts)
- ✓ Correct order: square first, then multiply
- ✓ Gets correct answer

### Output (20 pts)
- ✓ Displays result
- ✓ Includes label (e.g., "The area is...")
- ✓ Includes "square units"

---

## Testing

**Test case 1:**
```
Input: radius = 5
Expected: 78.5 square units
```

**Test case 2:**
```
Input: radius = 10
Expected: 314.0 square units
```

**Test case 3:**
```
Input: radius = 2.5
Expected: 19.625 square units
```

---

## Common Mistakes

❌ **Wrong operator for squaring:**
```python
area = 3.14 * radius * 2  # Multiply by 2, not square!
area = 3.14 * radius ^ 2  # ^ is XOR, not exponentiation
```

✅ **Correct:**
```python
area = 3.14 * radius ** 2  # ** is exponentiation
```

❌ **Order of operations:**
```python
area = (3.14 * radius) ** 2  # Squares the product instead of just radius
```

❌ **Using math.pi instead of 3.14:**
```python
import math
area = math.pi * radius ** 2  # Correct math, but instructions say use 3.14
```
*Note: Using `math.pi` is better in real code, but follow assignment instructions!*

---

## Alternative Solutions

**All acceptable:**
```python
# Parentheses for clarity (not required)
area = 3.14 * (radius ** 2)

# Compute directly in print
print("The area is", 3.14 * radius ** 2, "square units.")

# Store intermediate result
radius_squared = radius ** 2
area = 3.14 * radius_squared
```

**Not acceptable (doesn't follow instructions):**
```python
area = 3.14 * radius * radius  # Should use ** operator
```

---

## Key Concepts

- **Exponentiation operator `**`** - `x ** 2` means x²
- **Order of operations** - Exponentiation before multiplication
- **Using constants** - 3.14 as approximation of π
- **Mathematical notation** - Translating formulas to code

---

## Python Operators Comparison

| Math | Python | Example |
|------|--------|---------|
| x² | `x ** 2` | `5 ** 2` = 25 |
| x³ | `x ** 3` | `2 ** 3` = 8 |
| √x | `x ** 0.5` | `16 ** 0.5` = 4.0 |

---

## Notes

- **Instructions specifically say use `3.14`** (not `math.pi`)
- **Must use `**` operator** for exponentiation
- First exposure to the exponentiation operator
- Practice translating mathematical formulas

**Full credit if:** Program uses `3.14 * radius ** 2` and displays result with label.
