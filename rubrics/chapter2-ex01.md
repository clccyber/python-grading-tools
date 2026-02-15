# Grading Rubric: Chapter 2, Exercise 1
## Tax Calculator with Rounding

---

## 📋 What You're Building

A program that calculates income tax based on:
- Gross income (user input)
- Number of dependents (user input)

The program should display the calculated tax with **at most 2 decimal places**.

---

## 🎯 Point Breakdown (100 Total)

| Category | Points | What's Graded |
|----------|--------|---------------|
| **Numeric Correctness** | 80 | Tax calculation matches expected formula |
| **Labels & Output** | 20 | Output includes the phrase "income tax" |

---

## 📐 The Formula

```python
TAX_RATE = 0.20
STANDARD_DEDUCTION = 10000.0
DEPENDENT_DEDUCTION = 3000.0

taxable_income = gross_income - STANDARD_DEDUCTION - (DEPENDENT_DEDUCTION * dependents)
income_tax = taxable_income * TAX_RATE
```

---

## ✅ Expected Output Format

Your program should:
- Prompt for gross income
- Prompt for number of dependents
- Display output containing "income tax" (case-insensitive)
- Show the tax amount

**Example:**
```
Enter the gross income: 50000
Enter the number of dependents: 2
The income tax is $6800.0
```

---

## 📊 How Grading Works

The grader runs your program with test inputs and checks:

✓ **Calculation accuracy** - Tax value within 0.1% tolerance  
✓ **Label presence** - Output contains "income tax" somewhere  
✓ **Execution** - Program completes within 2 seconds  

---

## ❌ Common Mistakes

| Mistake | Points Lost | Example |
|---------|-------------|---------|
| Missing "income tax" label | -20 | Just printing `6800.0` |
| Wrong deduction amounts | -80 | Using different STD or DEP values |
| Not rounding/formatting | 0 | This exercise is forgiving on format |
| Code crashes or hangs | -100 | Runtime errors or infinite loops |

---

## 💡 Tips for Success

1. **Use the exact deduction values**: STD = $10,000, DEP = $3,000 per dependent
2. **Include the phrase** "income tax" in your output (exact case doesn't matter)
3. **Test with the example**: Input 50000 and 2 should give $6800.0
4. **Use `round()` function**: Task asks for at most 2 decimal places
5. **Run `grade.sh`** before submitting to check your score

---

## 🧪 Test Your Code

From the `student/` directory:
```bash
../../tools/grade.sh
```

Check your report in `../report_ex01/report.txt`

---

## 📚 Key Concepts

This exercise practices:
- Getting user input with `input()`
- Converting strings to numbers (`int()`, `float()`)
- Basic arithmetic operations
- Using the `round()` function
- Formatting output with f-strings or concatenation
