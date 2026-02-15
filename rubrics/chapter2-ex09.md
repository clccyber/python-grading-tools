# Grading Rubric: Chapter 2, Exercise 9
## Kilometers to Nautical Miles Converter ⛵

---

## 📋 What You're Building

A program that converts kilometers to nautical miles using geographical approximations.

**Given facts:**
- 1 kilometer = 1/10,000 of the distance from North Pole to equator
- 90 degrees from North Pole to equator
- Each degree has 60 minutes of arc
- 1 nautical mile = 1 minute of arc

---

## 🎯 Point Breakdown (100 Total)

| Category | Points | What's Graded |
|----------|--------|---------------|
| **Numeric Correctness** | 80 | Conversion calculation is accurate |
| **Labels & Output** | 20 | Output includes "nautical miles" |

---

## 📐 The Formula

Working through the conversion:
- Total minutes of arc from pole to equator: 90° × 60 = 5,400 minutes
- Distance from pole to equator: 10,000 km
- Therefore: 1 nautical mile = 10,000 km / 5,400 minutes

```python
nautical_miles = kilometers * (90 * 60) / 10000
```

**Simplified:**
```python
nautical_miles = kilometers * 0.54
```

---

## ✅ Expected Output Format

Your program should:
- Prompt for kilometers
- Display output containing "nautical miles"
- Show the converted value

**Example:**
```
Enter the number of kilometers: 1234
The number of nautical miles is 666.36
```

---

## 📊 How Grading Works

The grader runs your program with test inputs and checks:

✓ **Calculation accuracy** - Result within 0.1% tolerance  
✓ **Label presence** - Output contains "nautical miles"  
✓ **Execution** - Program completes within 2 seconds  

---

## ❌ Common Mistakes

| Mistake | Points Lost | Example |
|---------|-------------|---------|
| Missing "nautical miles" label | -20 | Just printing `666.36` |
| Wrong conversion factor | -80 | Using 1.852 (standard conversion) |
| Math error in formula | -80 | `(90 / 60)` instead of `(90 * 60)` |
| Inverted formula | -80 | Dividing instead of multiplying |
| Code crashes | -100 | Runtime errors |

---

## 💡 Tips for Success

1. **Use the approximation given**: Don't use the "real" 1.852 conversion
2. **Calculate the factor**: (90 × 60) / 10000 = 5400 / 10000 = 0.54
3. **Include the label**: Output must contain "nautical miles"
4. **Test with example**: 1234 km = 666.36 nautical miles
5. **This is a geography approximation**: Results differ from standard nautical mile conversion

### Formula Breakdown:
```python
# Method 1: Full calculation
nautical_miles = kilometers * (90 * 60) / 10000

# Method 2: Pre-calculated factor
nautical_miles = kilometers * 0.54

# Wrong - standard conversion (not what exercise asks for)
nautical_miles = kilometers / 1.852
```

### Why this formula?
```
- Equator to pole = 10,000 km
- Equator to pole = 90 degrees
- 1 degree = 60 minutes of arc
- Total arc minutes = 90 * 60 = 5,400
- 1 nautical mile = 10,000 km / 5,400 ≈ 1.85 km
- So: nm = km / 1.85 = km * (5,400/10,000) = km * 0.54
```

---

## 🧪 Test Your Code

From the `student/` directory:
```bash
../../tools/grade.sh
```

Check your report in `../report_ex09/report.txt`

---

## 📚 Key Concepts

This exercise practices:
- Multi-step unit conversions
- Working with approximations
- Fraction arithmetic
- Understanding conversion ratios
- Following specific calculation methods
