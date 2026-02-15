# Grading Rubric: Chapter 1, Exercise 3
## Triangle Area

---

## 📋 What You're Building

Compute the area of a triangle:
- **File:** `triangle.py`
- **Formula:** `area = 0.5 × base × height`
- **Concept:** Write your own program with formula

**Example:**
```
Enter the base: 6
Enter the height: 7
The area is 21.0 square units.
```

---

## 🎯 Point Breakdown (100 Total)

| Category | Points |
|----------|--------|
| **Prompts for Base** | 20 |
| **Prompts for Height** | 20 |
| **Correct Formula** | 40 |
| **Output with Label** | 20 |

---

## 💻 Implementation

```python
# triangle.py
base = float(input("Enter the base: "))
height = float(input("Enter the height: "))
area = 0.5 * base * height
print("The area is", area, "square units.")
```

**Or using `.5` instead of `0.5`:**
```python
area = .5 * base * height
```

---

## ✅ What to Check

### Input (40 pts)
- ✓ Prompts for base (20 pts)
- ✓ Prompts for height (20 pts)
- ✓ Converts to float
- ✓ Clear prompts

### Calculation (40 pts)
- ✓ Uses formula: `0.5 * base * height`
- ✓ Correct order of operations
- ✓ Result stored in variable
- ✓ Gets correct answer

### Output (20 pts)
- ✓ Displays calculated area
- ✓ Includes label (e.g., "The area is...")
- ✓ Includes units ("square units")

---

## Testing

**Test case 1:**
```
Input: base = 6, height = 7
Expected: 21.0 square units
```

**Test case 2:**
```
Input: base = 10, height = 5
Expected: 25.0 square units
```

**Test case 3:**
```
Input: base = 3.5, height = 4.0
Expected: 7.0 square units
```

---

## Common Mistakes

❌ **Wrong formula:**
```python
area = base * height  # Missing the 0.5
area = 0.5 + base + height  # Addition instead of multiplication
```

❌ **Order of operations confusion:**
```python
area = 0.5 * base + height  # Only base is multiplied by 0.5
```
✅ **Correct:**
```python
area = 0.5 * base * height  # All multiplied together
```

❌ **No type conversion:**
```python
base = input("Enter the base: ")  # String, not number
```

❌ **Missing output label:**
```python
print(area)  # Just the number, no context
```

---

## Alternative Solutions

**All acceptable:**
```python
# Using 0.5
area = 0.5 * base * height

# Using .5
area = .5 * base * height

# Using division
area = (base * height) / 2

# Using formula directly in print
print("The area is", 0.5 * base * height, "square units.")
```

---

## Key Concepts

- **Mathematical formulas** - Translating math to code
- **Order of operations** - Multiplication before addition
- **Type conversion** - `float()` for decimal numbers
- **Output formatting** - Including units and labels

---

## Notes

- This is your first "write from scratch" program
- Formula is given in instructions: `.5 * base * height`
- Must handle decimal inputs correctly
- Output must be labeled clearly

**Full credit if:** Program correctly computes triangle area using given formula and displays result with label.
