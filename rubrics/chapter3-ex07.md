# Grading Rubric: Chapter 3, Exercise 7
## Teacher Salary Schedule Table 👨‍🏫

---

## 📋 What You're Building

A program that displays a salary schedule showing how a teacher's salary increases each year based on:
- Starting salary
- Annual percentage increase
- Number of years

**Output:** A formatted table with years and salaries.

**Key concept:** Using loops to generate and display multiple rows of calculated data.

---

## 🎯 Point Breakdown (100 Total)

| Category | Points | What's Graded |
|----------|--------|---------------|
| **Row Values** | 60 | Salary calculations for each year are correct |
| **Formatting** | 20 | Salaries displayed with exactly 2 decimal places |
| **Table Structure** | 20 | Headers and separator lines present |

---

## 📐 The Formula

**For each year N:**
```python
salary_year_N = starting_salary * (1 + percent_increase)^(N-1)
```

**Example:** Starting=$30,000, Increase=2%, Year 3
```
salary = 30000 * (1.02)^2 = 30000 * 1.0404 = $31,212.00
```

---

## ✅ Expected Output Format

Your program should:
- Prompt for starting salary
- Prompt for annual % increase (enter as whole number, e.g., "2" for 2%)
- Prompt for number of years
- Display a table with headers
- Include a separator line
- Show each year with its salary

**Example:**
```
Enter the starting salary: $30000
Enter the annual % increase: 2
Enter the number of years: 10

Year   Salary
-------------
 1    30000.00
 2    30600.00
 3    31212.00
 4    31836.24
 5    32472.96
 6    33122.42
 7    33784.87
 8    34460.57
 9    35149.78
10    35852.78
```

---

## 📊 How Grading Works

The grader checks:

✓ **Each row's salary** - Calculated correctly for that year  
✓ **2 decimal places** - Every salary formatted as money (XX.XX)  
✓ **Table headers** - "Year" and "Salary" present  
✓ **Separator line** - Dashes between header and data  

**Partial credit:** Points awarded per row, so getting some years right earns some points.

---

## ❌ Common Mistakes

| Mistake | Points Lost | Why |
|---------|-------------|-----|
| Wrong formula | Up to -60 | Each incorrect row loses points |
| Not 2 decimals | Up to -20 | Money must show .XX |
| Missing headers | -10 | Table needs "Year   Salary" |
| Missing separator | -10 | Table needs "-------" line |
| Starting at year 0 | -60 | Should start at year 1 |
| Wrong exponent | -60 | Year 1 is (1.02)^0, Year 2 is (1.02)^1 |

---

## 💡 Tips for Success

1. **Convert percent to decimal**: If user enters "2", divide by 100 → 0.02
2. **Year 1 gets starting salary**: (1 + rate)^0 = 1.0
3. **Use a loop**: `for year in range(1, num_years + 1)`
4. **Format with 2 decimals**: `{salary:.2f}`
5. **Compound growth**: Each year multiplies by (1 + rate) again

### Code Pattern:
```python
starting = float(input("Enter starting salary: $"))
percent = float(input("Enter annual % increase: "))
years = int(input("Enter number of years: "))

rate = percent / 100  # Convert to decimal

print("\nYear   Salary")
print("-------------")

for year in range(1, years + 1):
    salary = starting * ((1 + rate) ** (year - 1))
    print(f"{year:2d}    {salary:.2f}")
```

### Common Logic Errors:
```python
# Wrong - linear growth
salary = starting + (starting * rate * year)  # Should be exponential

# Wrong - using year instead of (year-1)
salary = starting * ((1 + rate) ** year)  # Year 1 would be rate^1, not rate^0

# Wrong - wrong decimals
print(f"{year}  {salary}")  # Might show 30000.0 instead of 30000.00

# Wrong - adding instead of multiplying
salary = starting
for y in range(year):
    salary = salary + rate  # Should multiply, not add
```

---

## 🧪 Test Your Code

From the `student/` directory:
```bash
../../tools/grade.sh
```

Check your report in `../report_ex07/report.txt`

**Verify with example:**
- Starting: $30,000
- Increase: 2%
- Years: 10
- Year 5 should be: $32,472.96
- Year 10 should be: $35,852.78

---

## 📚 Key Concepts

This exercise practices:
- `for` loops with `range()`
- Compound growth (exponential)
- Exponentiation (`**`)
- Money formatting (`{:.2f}`)
- Table output with headers
- Converting percentages to decimals
