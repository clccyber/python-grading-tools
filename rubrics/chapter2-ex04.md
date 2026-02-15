# Grading Rubric: Chapter 2, Exercise 4
## Sphere Properties Calculator 🌐

---

## 📋 What You're Building

A program that calculates multiple properties of a sphere given its radius:
- Diameter
- Circumference
- Surface area
- Volume

---

## 🎯 Point Breakdown (100 Total)

| Category | Points | What's Graded |
|----------|--------|---------------|
| **Numeric Correctness** | 80 | All 4 calculations are accurate |
| **Labels & Output** | 20 | Output includes all 4 property labels |

**Note:** Each property is worth equal points within its category.

---

## 📐 The Formulas

```python
import math

diameter = 2 * radius
circumference = 2 * math.pi * radius
surface_area = 4 * math.pi * radius**2
volume = (4.0 / 3.0) * math.pi * radius**3
```

---

## ✅ Expected Output Format

Your program should:
- Prompt for the sphere's radius
- Display all 4 properties with their labels
- Each property clearly labeled

**Example:**
```
Enter the sphere's radius: 12
Diameter     : 24.0
Circumference: 75.39822368615503
Surface area : 1809.5573684677208
Volume       : 7238.229473870883
```

**Required labels (case-insensitive):**
- "diameter"
- "circumference"
- "surface area"
- "volume"

---

## 📊 How Grading Works

The grader runs your program with test inputs and checks:

✓ **Calculation accuracy** - Each value within 0.1% tolerance  
✓ **Label presence** - All 4 labels appear in output  
✓ **Execution** - Program completes within 2 seconds  

---

## ❌ Common Mistakes

| Mistake | Points Lost | Why |
|---------|-------------|-----|
| Missing any label | -5 per label | Each of 4 labels worth ~5 points |
| Wrong formula | -20 per value | Each calculation worth ~20 points |
| Forgetting `math.pi` | -60 | Affects 3 of 4 calculations |
| Using wrong exponents | -20 to -60 | r² vs r³ matters! |
| Code crashes | -100 | Runtime errors |

---

## 💡 Tips for Success

1. **Import math**: You need `import math` at the top for `math.pi`
2. **Use correct formulas**:
   - Diameter = 2r (no π needed)
   - Circumference = 2πr
   - Surface area = 4πr²
   - Volume = (4/3)πr³
3. **Include all 4 labels**: diameter, circumference, surface area, volume
4. **Watch the exponents**: r² for surface area, r³ for volume
5. **Use `**` for powers**: `radius**2` for r²

### Formula Examples:
```python
import math

# Correct
surface_area = 4 * math.pi * radius**2

# Also correct
surface_area = 4 * math.pi * radius * radius

# Wrong - missing pi
surface_area = 4 * radius**2

# Wrong - wrong exponent
volume = (4/3) * math.pi * radius**2  # Should be **3
```

---

## 🧪 Test Your Code

From the `student/` directory:
```bash
../../tools/grade.sh
```

Check your report in `../report_ex04/report.txt`

**Test with radius = 12:**
- Diameter should be 24.0
- Circumference should be ~75.4
- Surface area should be ~1809.6
- Volume should be ~7238.2

---

## 📚 Key Concepts

This exercise practices:
- Importing modules (`import math`)
- Using constants (`math.pi`)
- Exponentiation operator (`**`)
- Multiple calculations in one program
- Organizing output clearly
