# Grading Rubric: Chapter 2, Exercise 6
## Momentum and Kinetic Energy Calculator ⚡🔋

---

## 📋 What You're Building

A program that calculates **both**:
- Momentum = m × v
- Kinetic Energy = ½mv²

Given the object's mass and velocity.

---

## 🎯 Point Breakdown (100 Total)

| Category | Points | What's Graded |
|----------|--------|---------------|
| **Numeric Correctness** | 80 | Both calculations are accurate |
| **Labels & Output** | 20 | Output includes both "momentum" and "kinetic energy" |

**Note:** Each calculation and label is worth equal points.

---

## 📐 The Formulas

```python
momentum = mass * velocity
kinetic_energy = 0.5 * mass * velocity**2
```

**Key difference:**
- Momentum: linear (v)
- Kinetic energy: quadratic (v²)

---

## ✅ Expected Output Format

Your program should:
- Prompt for the object's mass
- Prompt for the object's velocity
- Display **both** momentum and kinetic energy
- Each value clearly labeled

**Example:**
```
Enter the object's mass: 250
Enter the object's velocity: 12
The object's momentum is 3000.0
The object's kinetic energy is 18000.0
```

**Required labels (case-insensitive):**
- "momentum"
- "kinetic energy"

---

## 📊 How Grading Works

The grader runs your program with test inputs and checks:

✓ **Calculation accuracy** - Both values within 0.1% tolerance  
✓ **Label presence** - Both labels appear in output  
✓ **Execution** - Program completes within 2 seconds  

---

## ❌ Common Mistakes

| Mistake | Points Lost | Why |
|---------|-------------|-----|
| Missing either label | -10 per label | Each label worth ~10 points |
| Wrong momentum | -40 | Half of numeric points |
| Wrong kinetic energy | -40 | Half of numeric points |
| Forgetting to square velocity | -40 | KE uses v² not v |
| Forgetting the ½ factor | -40 | KE = ½mv² |
| Code crashes | -100 | Runtime errors |

---

## 💡 Tips for Success

1. **Calculate both values**: This exercise requires momentum AND kinetic energy
2. **Square the velocity** for kinetic energy: `velocity**2` or `velocity * velocity`
3. **Don't forget the ½**: Multiply by 0.5 or divide by 2
4. **Include both labels**: "momentum" and "kinetic energy"
5. **Test with example**: Mass 250, velocity 12:
   - Momentum = 3000.0
   - Kinetic energy = 18000.0

### Formula Examples:
```python
# Momentum (simple)
momentum = mass * velocity

# Kinetic energy (correct)
kinetic_energy = 0.5 * mass * velocity**2

# Also correct
kinetic_energy = (mass * velocity * velocity) / 2

# Wrong - missing square
kinetic_energy = 0.5 * mass * velocity  # Too small!

# Wrong - missing 0.5
kinetic_energy = mass * velocity**2     # Too big!
```

---

## 🧪 Test Your Code

From the `student/` directory:
```bash
../../tools/grade.sh
```

Check your report in `../report_ex06/report.txt`

---

## 📚 Key Concepts

This exercise practices:
- Multiple calculations in one program
- Exponentiation (`**2`)
- Working with decimal multipliers (0.5)
- Organizing related outputs
- Physics formulas
