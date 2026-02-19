# Grading Rubric: Chapter 2, Exercise 8
## Light-Year Distance Calculator 💫

---

## 📋 What You're Building

A program that calculates how far light travels in a given number of years.

**Given:**
- Light speed: 3 × 10⁸ meters/second
- 1 year = 365 days × 24 hours × 60 minutes × 60 seconds

---

## 🎯 Point Breakdown (100 Total)

| Category | Points | What's Graded |
|----------|--------|---------------|
| **Numeric Correctness** | 80 | Distance calculation is accurate |
| **Labels & Output** | 20 | Output includes the word "meters" |

---

## 📐 The Formula

```python
LIGHT_SPEED = 3.0e8  # or 3 * 10**8 or 300000000

seconds_per_year = 365 * 24 * 60 * 60
total_seconds = years * seconds_per_year
distance_meters = total_seconds * LIGHT_SPEED
```

**Simplified:**
```python
distance = years * 365 * 24 * 60 * 60 * 3.0e8
```

---

## ✅ Expected Output Format

Your program should:
- Prompt for number of years
- Display output containing "meters"
- Show the calculated distance

**Example:**
```
Enter the number of years: 12
In 12 years, Light travels 113529600000000000 meters. 

**Note:** The result is HUGE (15+ digits for 12 years)
--The years must come before the number of meters.
**--This is not the same order as in the output requested by cengage**

---

## 📊 How Grading Works

The grader runs your program with test inputs and checks:

✓ **Calculation accuracy** - Result within 0.1% tolerance  
✓ **Label presence** - Output contains "meters"  
✓ **Execution** - Program completes within 2 seconds  

---

## ❌ Common Mistakes

| Mistake | Points Lost | Example |
|---------|-------------|---------|
| Missing "meters" label | -20 | Just printing the number |
| Wrong light speed | -80 | Using 3e9 or other values |
| Missing conversion | -80 | Forgetting days→seconds steps |
| Using wrong notation | -80 | `3 * 10 * 8` instead of `3e8` |
| Code crashes | -100 | Runtime errors |

---

## 💡 Tips for Success

1. **Use scientific notation**: `3.0e8` means 3.0 × 10⁸ = 300,000,000
2. **Convert years to seconds**: years × 365 × 24 × 60 × 60
3. **Include the label**: Output must contain "meters"
4. **Test with example**: 12 years ≈ 1.135 × 10¹⁷ meters
5. **Expect big numbers**: Results will be 15+ digits

### Scientific Notation in Python:
```python
# All equivalent ways to write 300,000,000
light_speed = 3.0e8
light_speed = 3 * 10**8
light_speed = 300000000

# Recommended: scientific notation
light_speed = 3.0e8  # Clearest for large numbers
```

### Common Errors:
```python
# Correct
distance = years * 365 * 24 * 60 * 60 * 3.0e8

# Wrong - bad scientific notation
distance = years * 365 * 24 * 60 * 60 * 3 * 10 * 8  # = 240, way too small!

# Wrong - light speed in km/s instead of m/s
distance = years * 365 * 24 * 60 * 60 * 300000  # Off by 1000x
```

---

## 🧪 Test Your Code

From the `student/` directory:
```bash
../../tools/grade.sh
```

Check your report in `../report_ex08/report.txt`

**Quick check:** 1 year should give about 9.46 × 10¹⁵ meters

---

## 📚 Key Concepts

This exercise practices:
- Scientific notation (`3.0e8`)
- Multiple unit conversions
- Working with very large numbers
- Exponentiation (`10**8`)
- Chained calculations
