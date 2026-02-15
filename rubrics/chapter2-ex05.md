# Grading Rubric: Chapter 2, Exercise 5
## Momentum Calculator ⚡

---

## 📋 What You're Building

A program that calculates an object's momentum using:
- Mass (user input)
- Velocity (user input)

**Formula:** momentum = mass × velocity

---

## 🎯 Point Breakdown (100 Total)

| Category | Points | What's Graded |
|----------|--------|---------------|
| **Numeric Correctness** | 80 | Momentum calculation is accurate |
| **Labels & Output** | 20 | Output includes the phrase "momentum" |

---

## 📐 The Formula

```python
momentum = mass * velocity
```

---

## ✅ Expected Output Format

Your program should:
- Prompt for the object's mass
- Prompt for the object's velocity
- Display output containing "momentum"
- Show the calculated value

**Example:**
```
Enter the object's mass: 250
Enter the object's velocity: 25
The object's momentum is 6250.0
```

---

## 📊 How Grading Works

The grader runs your program with test inputs and checks:

✓ **Calculation accuracy** - Result within 0.1% tolerance  
✓ **Label presence** - Output contains "momentum"  
✓ **Execution** - Program completes within 2 seconds  

---

## ❌ Common Mistakes

| Mistake | Points Lost | Example |
|---------|-------------|---------|
| Missing "momentum" label | -20 | Just printing `6250.0` |
| Wrong formula | -80 | Adding instead of multiplying |
| Using wrong formula | -80 | Kinetic energy formula (½mv²) |
| Code crashes | -100 | Runtime errors |

---

## 💡 Tips for Success

1. **Simple multiplication**: Just mass × velocity
2. **Include the label**: Output must contain "momentum"
3. **Test with example**: Mass 250, velocity 25 = momentum 6250.0
4. **Don't confuse with kinetic energy**: That's a different formula (exercise 6)
5. **Run `grade.sh`** to verify before submitting

---

## 🧪 Test Your Code

From the `student/` directory:
```bash
../../tools/grade.sh
```

Check your report in `../report_ex05/report.txt`

---

## 📚 Key Concepts

This exercise practices:
- Getting multiple numeric inputs
- Simple multiplication
- Physics calculations
- Clear output formatting
