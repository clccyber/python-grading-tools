# Grading Rubric: Chapter 3, Exercise 1
## Equilateral Triangle Checker 📐

---

## 📋 What You're Building

A program that determines if a triangle is equilateral by checking if all three sides are equal.

**Key concept:** Using conditional logic (if/else) to make decisions.

---

## 🎯 Point Breakdown (100 Total)

| Category | Points | What's Graded |
|----------|--------|---------------|
| **Decision Correctness** | 80 | Correctly identifies equilateral vs. non-equilateral |
| **Output Presence** | 20 | Program produces output for each test |

---

## 📐 The Logic

```python
# Equilateral triangle: all three sides are equal
if side1 == side2 == side3:
    # It's equilateral
else:
    # It's not equilateral
```

---

## ✅ Expected Output Format

Your program should:
- Prompt for three sides
- Determine if all three sides are equal
- Output a statement about whether it's equilateral

**Example outputs:**
```
Enter the first side: 5
Enter the second side: 5
Enter the third side: 5
The triangle is equilateral.
```

```
Enter the first side: 3
Enter the second side: 4
Enter the third side: 5
The triangle is not equilateral.
```

---

## 📊 How Grading Works

The grader runs your program with different triangle inputs and checks:

✓ **When all sides are equal** (5,5,5) → output contains "is equilateral"  
✓ **When sides differ** (3,4,5) → output contains "not" (or doesn't say "is equilateral")  
✓ **Output exists** → program doesn't crash or produce nothing  

---

## ❌ Common Mistakes

| Mistake | Points Lost | Why |
|---------|-------------|-----|
| No output produced | -100 | Can't grade what doesn't exist |
| Logic backwards | -80 | Says "is" when should say "not" |
| Only checks two sides | -80 | Must check all three are equal |
| Missing conditional | -80 | No if/else = no decision making |

---

## 💡 Tips for Success

1. **Check all three sides**: Use `side1 == side2 == side3` or similar
2. **Use if/else**: This is a conditional logic exercise
3. **Include "equilateral"** in your output for full points
4. **Test both cases**:
   - Try with 5, 5, 5 (should say "is equilateral")
   - Try with 3, 4, 5 (should say "not equilateral")

### Code Pattern:
```python
side1 = float(input("Enter the first side: "))
side2 = float(input("Enter the second side: "))
side3 = float(input("Enter the third side: "))

if side1 == side2 == side3:
    print("The triangle is equilateral.")
else:
    print("The triangle is not equilateral.")
```

### Common Logic Errors:
```python
# Wrong - only checks two sides
if side1 == side2:  # What about side3?

# Wrong - checks if any two are equal
if side1 == side2 or side2 == side3:  # Not the same as ALL equal

# Correct - all three must be equal
if side1 == side2 == side3:
```

---

## 🧪 Test Your Code

From the `student/` directory:
```bash
../../tools/grade.sh
```

Check your report in `../report_ex01/report.txt`

**Test cases to try manually:**
- 5, 5, 5 → should say "is equilateral"
- 3, 4, 5 → should say "not equilateral"  
- 7, 7, 8 → should say "not equilateral"

---

## 📚 Key Concepts

This exercise practices:
- Conditional statements (`if`/`else`)
- Equality comparison (`==`)
- Chained comparisons (`a == b == c`)
- Boolean logic
- Decision-making in programs
