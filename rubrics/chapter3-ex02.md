# Grading Rubric: Chapter 3, Exercise 2
## Right Triangle Checker (Pythagorean Theorem) 📐

---

## 📋 What You're Building

A program that determines if a triangle is a right triangle using the Pythagorean theorem.

**The Rule:** In a right triangle, the square of one side equals the sum of the squares of the other two sides.

---

## 🎯 Point Breakdown (100 Total)

| Category | Points | What's Graded |
|----------|--------|---------------|
| **Decision Correctness** | 80 | Correctly identifies right triangles using Pythagorean theorem |
| **Output Presence** | 20 | Program produces output for each test |

---

## 📐 The Pythagorean Theorem

**For a right triangle:** a² + b² = c²

Where **c** is the longest side (hypotenuse).

```python
# You need to check if any arrangement satisfies:
side1² + side2² == side3²  OR
side1² + side3² == side2²  OR
side2² + side3² == side1²
```

**Important:** You don't know which side is the hypotenuse! The user can enter them in any order.

---

## ✅ Expected Output Format

Your program should:
- Prompt for three sides
- Apply the Pythagorean theorem
- Output whether it's a right triangle

**Example outputs:**
```
Enter the first side: 3
Enter the second side: 4
Enter the third side: 5

The triangle is a right triangle.
```

```
Enter the first side: 5
Enter the second side: 5
Enter the third side: 5

The triangle is not a right triangle.
```

---

## 📊 How Grading Works

The grader tests with various triangles:

✓ **3-4-5 triangle** → "is a right triangle"  
✓ **6-8-10 triangle** (scaled 3-4-5) → "is a right triangle"  
✓ **5-5-5 triangle** → "not a right triangle"  
✓ **Sides in different order** (5,3,4) → still detects right triangle  

---

## ❌ Common Mistakes

| Mistake | Points Lost | Why |
|---------|-------------|-----|
| Assumes side order | -80 | User can enter hypotenuse first, second, or third! |
| Only checks one combo | -80 | Must check all three possible arrangements |
| Exact equality (==) | Risky | Floating point! Use tolerance or sort sides |
| Wrong formula | -80 | Not squaring, or wrong sides |
| No output | -100 | Can't grade nothing |

---

## 💡 Tips for Success

1. **Don't assume which side is longest**: Check all three combinations OR sort the sides first
2. **Square the sides**: a² means `a * a` or `a**2`
3. **The classic example**: 3² + 4² = 9 + 16 = 25 = 5²
4. **Test the examples**:
   - 3, 4, 5 → right triangle
   - 6, 8, 10 → right triangle (scaled version)
   - 5, 5, 5 → NOT a right triangle

### Recommended Approach - Sort First:
```python
side1 = float(input("Enter the first side: "))
side2 = float(input("Enter the second side: "))
side3 = float(input("Enter the third side: "))

# Sort so we know which is longest
sides = sorted([side1, side2, side3])
a, b, c = sides[0], sides[1], sides[2]

# Now c is definitely the longest (potential hypotenuse)
if a**2 + b**2 == c**2:
    print("\nThe triangle is a right triangle.")
else:
    print("\nThe triangle is not a right triangle.")
```

### Alternative - Check All Three:
```python
if (side1**2 + side2**2 == side3**2 or
    side1**2 + side3**2 == side2**2 or
    side2**2 + side3**2 == side1**2):
    print("\nThe triangle is a right triangle.")
else:
    print("\nThe triangle is not a right triangle.")
```

### Common Logic Errors:
```python
# Wrong - assumes side3 is always the hypotenuse
if side1**2 + side2**2 == side3**2:  # Fails if user enters 5,3,4

# Wrong - not squaring
if side1 + side2 == side3:  # This is NOT the Pythagorean theorem

# Wrong - comparing sides not squares
if side1 + side2 > side3:  # This checks triangle inequality, not right angle
```

---

## 🧪 Test Your Code

From the `student/` directory:
```bash
../../tools/grade.sh
```

Check your report in `../report_ex02/report.txt`

**Test cases to try manually:**
- 3, 4, 5 → should say "is a right triangle"
- 6, 8, 10 → should say "is a right triangle"
- 5, 5, 5 → should say "not a right triangle"
- 5, 3, 4 → should say "is a right triangle" (tests order independence)

---

## 📚 Key Concepts

This exercise practices:
- Conditional statements (`if`/`else`)
- The Pythagorean theorem (a² + b² = c²)
- Exponentiation (`**2`)
- Handling unknown input order
- Sorting values (`sorted()`)
- Boolean logic with `or`
