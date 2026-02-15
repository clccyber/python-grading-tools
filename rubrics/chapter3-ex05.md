# Grading Rubric: Chapter 3, Exercise 5
## Population Growth Predictor 🦠

---

## 📋 What You're Building

A program that predicts population growth of organisms based on:
- Initial population
- Growth rate (how much it multiplies)
- Time to achieve that growth rate
- Total time to predict

**Example:** 500 organisms, doubles (rate=2) every 6 hours
- After 6 hours: 1000
- After 12 hours: 2000
- After 18 hours: 4000

---

## 🎯 Point Breakdown (100 Total)

| Category | Points | What's Graded |
|----------|--------|---------------|
| **Numeric Correctness** | 80 | Population calculation is accurate |
| **Labels & Output** | 20 | Output includes "population" |

---

## 📐 The Formula

**Number of growth periods:** total_hours ÷ hours_per_period

**Final population:** initial × (rate ^ periods)

**Example:** 10 organisms, rate=2, 2 hours per period, 6 total hours
- Periods: 6 ÷ 2 = 3
- Population: 10 × 2³ = 10 × 8 = **80**

---

## ✅ Expected Output Format

Your program should:
- Prompt for initial number of organisms
- Prompt for growth rate
- Prompt for hours to achieve growth rate
- Prompt for total hours
- Calculate and display final population

**Example:**
```
Enter the initial number of organisms: 10
Enter the rate of growth [a real number > 1]: 2
Enter the number of hours to achieve the rate of growth: 2
Enter the total hours of growth: 6

The total population is 80
```

---

## 📊 How Grading Works

The grader runs your program with test inputs and checks:

✓ **Calculation accuracy** - Population within 0.1% tolerance  
✓ **Label presence** - Output contains "population"  
✓ **Execution** - Program completes within 2 seconds  

---

## ❌ Common Mistakes

| Mistake | Points Lost | Why |
|---------|-------------|-----|
| Missing "population" label | -20 | Output needs the word "population" |
| Wrong exponent | -80 | Must calculate rate^periods |
| Not using integer division | -80 | Partial periods shouldn't count |
| Adding instead of multiplying | -80 | Growth is exponential, not linear |

---

## 💡 Tips for Success

1. **Calculate periods first**: total_hours // hours_per_period (integer division)
2. **Use exponentiation**: `rate ** periods` or `rate**periods`
3. **Can use a loop OR direct calculation**: Both work!
4. **Result is an integer**: Population is whole organisms

### Direct Calculation (Recommended):
```python
initial = int(input("Enter initial organisms: "))
rate = float(input("Enter growth rate: "))
hours_for_rate = int(input("Enter hours for rate: "))
total_hours = int(input("Enter total hours: "))

periods = total_hours // hours_for_rate
population = initial * (rate ** periods)

print(f"The total population is {int(population)}")
```

### Loop Version (Also Valid):
```python
periods = total_hours // hours_for_rate
population = initial

for i in range(periods):
    population = population * rate

print(f"The total population is {int(population)}")
```

### Common Logic Errors:
```python
# Wrong - linear growth
population = initial + (rate * periods)  # Should multiply, not add

# Wrong - not using exponent
population = initial * rate * periods  # Missing exponential growth

# Wrong - including partial periods
periods = total_hours / hours_for_rate  # Should use // not /
```

---

## 🧪 Test Your Code

From the `student/` directory:
```bash
../../tools/grade.sh
```

Check your report in `../report_ex05/report.txt`

**Verify with example:**
- 10 organisms, rate=2, 2 hours/period, 6 total hours = **80**

---

## 📚 Key Concepts

This exercise practices:
- Integer division (`//`) vs regular division (`/`)
- Exponentiation (`**`)
- Understanding exponential growth
- Loop OR direct calculation (your choice!)
- Converting results to integers
