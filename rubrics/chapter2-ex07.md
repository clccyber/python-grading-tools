# Grading Rubric: Chapter 2, Exercise 7
## Years to Minutes Converter ⏰

---

## 📋 What You're Building

A program that converts years into total minutes.

**Conversions needed:**
- 1 year = 365 days
- 1 day = 24 hours
- 1 hour = 60 minutes

---

## 🎯 Point Breakdown (100 Total)

| Category | Points | What's Graded |
|----------|--------|---------------|
| **Numeric Correctness** | 80 | Minutes calculation is accurate |
| **Labels & Output** | 20 | Output includes the word "minutes" |

---

## 📐 The Formula

```python
minutes = years * 365 * 24 * 60
```

Breaking it down:
- years × 365 = days
- days × 24 = hours
- hours × 60 = minutes

**Result: years × 525,600**

---

## ✅ Expected Output Format

Your program should:
- Prompt for number of years
- Display output containing "minutes"
- Show the calculated total

**Example:**
```
Enter the number of years: 23
The number of minutes in 23 years is 12088800
```

---

## 📊 How Grading Works

The grader runs your program with test inputs and checks:

✓ **Calculation accuracy** - Result within 0.1% tolerance  
✓ **Label presence** - Output contains "minutes"  
✓ **Execution** - Program completes within 2 seconds  

---

## ❌ Common Mistakes

| Mistake | Points Lost | Example |
|---------|-------------|---------|
| Missing "minutes" label | -20 | Just printing `12088800` |
| Wrong conversion | -80 | Using 360 days or 30 days/month |
| Missing a factor | -80 | Forgetting ×24 or ×60 |
| Calculating hours/days instead | -80 | Not converting all the way to minutes |
| Code crashes | -100 | Runtime errors |

---

## 💡 Tips for Success

1. **Use 365 days per year**: Standard conversion (ignore leap years)
2. **Chain the conversions**: years → days → hours → minutes
3. **Include the label**: Output must contain "minutes"
4. **Test with example**: 23 years = 12,088,800 minutes
5. **The result is large**: For 23 years you get over 12 million minutes

### Calculation Examples:
```python
# Correct - all in one line
minutes = years * 365 * 24 * 60

# Also correct - step by step
days = years * 365
hours = days * 24
minutes = hours * 60

# Wrong - missing conversions
minutes = years * 365 * 60  # Forgot to multiply by 24

# Wrong - using months
minutes = years * 12 * 30 * 24 * 60  # Unnecessarily complex
```

---

## 🧪 Test Your Code

From the `student/` directory:
```bash
../../tools/grade.sh
```

Check your report in `../report_ex07/report.txt`

**Quick check:** 1 year should give 525,600 minutes

---

## 📚 Key Concepts

This exercise practices:
- Unit conversions
- Chained multiplication
- Working with large numbers
- Integer calculations
