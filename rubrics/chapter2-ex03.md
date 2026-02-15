# Grading Rubric: Chapter 2, Exercise 3
## Video Rental Cost Calculator 💿

---

## 📋 What You're Building

A program for Five Star Retro Video that calculates rental costs:
- New videos: $3.00 per night
- Oldies: $2.00 per night

**This exercise requires proper money formatting!**

---

## 🎯 Point Breakdown (100 Total)

| Category | Points | What's Graded |
|----------|--------|---------------|
| **Numeric Correctness** | 60 | Total cost calculation is accurate |
| **Labels & Output** | 20 | Output includes the phrase "total cost" |
| **Money Formatting** | 20 | Dollar amount has exactly 2 decimal places |

---

## 📐 The Formula

```python
NEW_PRICE = 3.00
OLDIE_PRICE = 2.00

total_cost = (new_videos * NEW_PRICE) + (oldies * OLDIE_PRICE)
```

---

## ✅ Expected Output Format

Your program should:
- Prompt for number of new videos
- Prompt for number of oldies
- Display output containing "total cost"
- Show the amount with **exactly 2 decimal places**

**Example:**
```
Enter the number of new videos: 4
Enter the number of oldies: 4
The total cost is $20.00
```

---

## 📊 How Grading Works

The grader runs your program with test inputs and checks:

✓ **Calculation accuracy** - Cost within 0.1% tolerance  
✓ **Label presence** - Output contains "total cost"  
✓ **Money formatting** - Exactly 2 decimals (not 1, not 3+)  
✓ **Execution** - Program completes within 2 seconds  

---

## ❌ Common Mistakes

| Mistake | Points Lost | Example |
|---------|-------------|---------|
| Missing "total cost" label | -20 | Just printing `20.00` |
| Wrong prices | -60 | Using $3.50 or $2.50 |
| Wrong decimal places | Up to -20 | `20.0` or `20.000` instead of `20.00` |
| Missing dollar sign | 0 | Optional (grader checks number only) |
| Code crashes | -100 | Runtime errors |

---

## 💡 Tips for Success

1. **Use correct prices**: $3.00 for new, $2.00 for oldies
2. **Format to 2 decimals**: Use `{:.2f}` in f-strings or `round(value, 2)`
3. **Include the label**: Output must contain "total cost"
4. **Test with example**: 4 new + 4 oldies = $20.00
5. **Watch the decimals**: `20.0` loses points, `20.00` is correct

### Formatting Examples:
```python
# Good - exactly 2 decimals
print(f"The total cost is ${total:.2f}")

# Also good
print("The total cost is $" + str(round(total, 2)))

# Bad - might show 1 or 3+ decimals
print(f"The total cost is ${total}")
```

---

## 🧪 Test Your Code

From the `student/` directory:
```bash
../../tools/grade.sh
```

Check your report in `../report_ex03/report.txt`

If you see formatting issues, check `formatting_issues.md` for specific hints.

---

## 📚 Key Concepts

This exercise practices:
- Multiple numeric inputs
- Arithmetic with constants
- **String formatting with f-strings**: `{:.2f}`
- Money handling (always 2 decimal places)
