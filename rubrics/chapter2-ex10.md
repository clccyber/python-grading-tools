# Grading Rubric: Chapter 2, Exercise 10
## Weekly Pay Calculator with Overtime 💰

---

## 📋 What You're Building

A program that calculates total weekly pay including overtime:
- Regular hours paid at hourly wage
- Overtime hours paid at 1.5× hourly wage

**This exercise requires proper money formatting!**

---

## 🎯 Point Breakdown (100 Total)

| Category | Points | What's Graded |
|----------|--------|---------------|
| **Numeric Correctness** | 60 | Pay calculation is accurate |
| **Labels & Output** | 20 | Output includes "total weekly pay" or similar |
| **Money Formatting** | 20 | Dollar amount has exactly 2 decimal places |

---

## 📐 The Formula

```python
regular_pay = hourly_wage * regular_hours
overtime_pay = hourly_wage * 1.5 * overtime_hours
total_weekly_pay = regular_pay + overtime_pay
```

**Key point:** Overtime hours are paid at **1.5 times** the regular wage.

---

## ✅ Expected Output Format

Your program should:
- Prompt for hourly wage
- Prompt for regular hours
- Prompt for overtime hours
- Display output containing "weekly pay" or "total weekly pay"
- Show the amount with **exactly 2 decimal places**

**Example:**
```
Enter the wage: $2000
Enter the regular hours: 8
Enter the overtime hours: 2
The total weekly pay is $22000.00
```

**Note:** The example shows an unusual wage ($2000/hour!), but your code should handle any valid input.

---

## 📊 How Grading Works

The grader runs your program with test inputs and checks:

✓ **Calculation accuracy** - Pay within 0.1% tolerance  
✓ **Label presence** - Output contains "weekly pay" or "total weekly pay"  
✓ **Money formatting** - Exactly 2 decimals (not 1, not 3+)  
✓ **Execution** - Program completes within 2 seconds  

---

## ❌ Common Mistakes

| Mistake | Points Lost | Example |
|---------|-------------|---------|
| Missing pay label | -20 | Just printing `22000.00` |
| Wrong overtime rate | -60 | Using 2.0× instead of 1.5× |
| Forgetting overtime | -60 | Only calculating regular hours |
| Wrong decimal places | Up to -20 | `22000.0` or `22000.000` |
| Code crashes | -100 | Runtime errors |

---

## 💡 Tips for Success

1. **Overtime is 1.5× wage**: Not 0.5× extra, but the full 1.5× rate
2. **Format to 2 decimals**: Use `{:.2f}` in f-strings
3. **Include the label**: "weekly pay" or "total weekly pay"
4. **Three separate inputs**: wage, regular hours, overtime hours
5. **Test the calculation**: 
   - Regular: $2000 × 8 = $16,000
   - Overtime: $2000 × 1.5 × 2 = $6,000
   - Total: $22,000.00

### Calculation Examples:
```python
# Correct
regular_pay = wage * regular_hours
overtime_pay = wage * 1.5 * overtime_hours
total = regular_pay + overtime_pay

# Also correct - combined
total = wage * regular_hours + wage * 1.5 * overtime_hours

# Wrong - overtime is only the extra 0.5
overtime_pay = wage * 0.5 * overtime_hours  # Too small!

# Wrong - forgot to multiply by 1.5
total = wage * (regular_hours + overtime_hours)  # No overtime premium
```

### Formatting Examples:
```python
# Good - exactly 2 decimals
print(f"The total weekly pay is ${total:.2f}")

# Also good
print("The total weekly pay is $" + format(total, ".2f"))

# Bad - might show wrong decimals
print(f"The total weekly pay is ${total}")  # Could be 22000.0
```

---

## 🧪 Test Your Code

From the `student/` directory:
```bash
../../tools/grade.sh
```

Check your report in `../report_ex10/report.txt`

If you see formatting issues, check `formatting_issues.md` for hints.

---

## 📚 Key Concepts

This exercise practices:
- Multiple numeric inputs
- Arithmetic with rate multipliers (1.5×)
- Adding regular and overtime components
- **Money formatting**: `{:.2f}`
- Real-world payroll calculations
