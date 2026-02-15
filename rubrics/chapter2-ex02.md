# Grading Rubric: Chapter 2, Exercise 2
## Cube Surface Area Calculator

---

## 📋 What You're Building

A program that calculates the surface area of a cube given the length of one edge.

---

## 🎯 Point Breakdown (100 Total)

| Category | Points | What's Graded |
|----------|--------|---------------|
| **Numeric Correctness** | 80 | Surface area calculation is accurate |
| **Labels & Output** | 20 | Output includes the phrase "surface area" |

---

## 📐 The Formula

```python
surface_area = 6 * edge * edge
```

A cube has 6 faces, each with area = edge²

---

## ✅ Expected Output Format

Your program should:
- Prompt for the cube's edge length
- Display output containing "surface area"
- Show the calculated value

**Example:**
```
Enter the cube's edge: 5
The surface area is 150.0 square units.
```

---

## 📊 How Grading Works

The grader runs your program with test inputs and checks:

✓ **Calculation accuracy** - Result within 0.1% tolerance  
✓ **Label presence** - Output contains "surface area"  
✓ **Execution** - Program completes within 2 seconds  

---

## ❌ Common Mistakes

| Mistake | Points Lost | Example |
|---------|-------------|---------|
| Missing "surface area" label | -20 | Just printing `150.0` |
| Wrong formula | -80 | Using `edge * 4` or `edge³` |
| Forgetting to multiply by 6 | -80 | Calculating only one face |
| Code crashes | -100 | Runtime errors |

---

## 💡 Tips for Success

1. **Remember all 6 faces**: A cube has 6 identical square faces
2. **Use the formula**: `6 * edge * edge` or `6 * edge**2`
3. **Include the label**: Output must contain "surface area"
4. **Test with example**: Edge of 5 should give 150.0
5. **Run `grade.sh`** to verify before submitting

---

## 🧪 Test Your Code

From the `student/` directory:
```bash
../../tools/grade.sh
```

Check your report in `../report_ex02/report.txt`

---

## 📚 Key Concepts

This exercise practices:
- Getting numeric input
- Squaring numbers (`edge * edge` or `edge**2`)
- Basic multiplication
- Formatting output strings
