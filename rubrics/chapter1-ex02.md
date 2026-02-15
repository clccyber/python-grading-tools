# Grading Rubric: Chapter 1, Exercise 2
## Rectangle Area (Code Entry from Book)

---

## 📋 What You're Building

Enter and test the program from Figure 1-7 in the textbook:
- **File:** `rectangle.py`
- **Task:** Type the program exactly, run it, fix errors
- **Concept:** input(), calculations, variables

---

## 🎯 Point Breakdown (100 Total)

| Category | Points |
|----------|--------|
| **Program Runs** | 30 |
| **Prompts for Width** | 15 |
| **Prompts for Height** | 15 |
| **Correct Calculation** | 30 |
| **Correct Output Format** | 10 |

---

## 💻 Implementation

**From Figure 1-7:**
```python
# rectangle.py
# Program to compute rectangle area

width = float(input("Enter the width: "))
height = float(input("Enter the height: "))
area = width * height
print("The area is", area, "square units.")
```

---

## ✅ What to Check

### Program Runs (30 pts)
- ✓ No syntax errors
- ✓ Accepts input without crashing
- ✓ Produces output

### Input Prompts (30 pts)
- ✓ Prompts for width (15 pts)
- ✓ Prompts for height (15 pts)
- ✓ Uses meaningful variable names

### Calculation (30 pts)
- ✓ Multiplies width × height
- ✓ Stores result in variable
- ✓ Gets correct answer

### Output Format (10 pts)
- ✓ Displays result
- ✓ Includes "square units" or similar label
- ✓ Clear, readable output

---

## Testing

**Test case 1:**
```
Input: width = 10, height = 5
Expected: 50.0 square units
```

**Test case 2:**
```
Input: width = 3.5, height = 2.0
Expected: 7.0 square units
```

---

## Common Mistakes

❌ **Forgot `float()` conversion:**
```python
width = input("Enter the width: ")  # Returns string!
area = width * height  # Type error
```

❌ **Wrong operator:**
```python
area = width + height  # Addition instead of multiplication
```

❌ **Typos from book:**
```python
heigth = float(input(...))  # Misspelled 'height'
```

✅ **Correct:**
```python
width = float(input("Enter the width: "))
height = float(input("Enter the height: "))
area = width * height
print("The area is", area, "square units.")
```

---

## Key Concepts

- **`input()` function** - Get user input (returns string)
- **`float()` conversion** - Convert string to number
- **Variables** - Store values
- **Arithmetic operators** - `*` for multiplication
- **Multiple arguments to print()** - Comma-separated

---

## Notes

- This exercise is about **accurately typing code from the book**
- Practice debugging syntax errors
- Understanding type conversions
- Testing with different inputs

**Full credit if:** Program accurately reproduces Figure 1-7 and correctly computes area.
