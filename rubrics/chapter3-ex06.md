# Grading Rubric: Chapter 3, Exercise 6
## Leibniz π Approximation 🥧

---

## 📋 What You're Building

A program that approximates π using Leibniz's formula:

**π/4 = 1 - 1/3 + 1/5 - 1/7 + 1/9 - ...**

The more iterations, the closer to π!

**Key concept:** Using loops to sum an alternating series.

---

## 🎯 Point Breakdown (100 Total)

| Category | Points | What's Graded |
|----------|--------|---------------|
| **Numeric Correctness** | 80 | π approximation matches expected value |
| **Labels & Output** | 20 | Output includes "approximation" or "pi" |

---

## 📐 The Formula

**Series:** 1/1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 + ...

**Pattern:**
- Denominators: 1, 3, 5, 7, 9, ... (odd numbers = 2i + 1)
- Signs: +, -, +, -, +, ... (alternating)

**To get π:** Multiply the sum by 4

**Example (5 iterations):**
```
i=0: +1/1 = +1.0
i=1: -1/3 = -0.333...
i=2: +1/5 = +0.2
i=3: -1/7 = -0.142...
i=4: +1/9 = +0.111...
Sum ≈ 0.8349...
π ≈ 0.8349... × 4 ≈ 3.3396...
```

---

## ✅ Expected Output Format

Your program should:
- Prompt for number of iterations
- Calculate the series sum
- Multiply by 4 to get π approximation
- Display the result

**Example:**
```
Enter the number of iterations: 5

The approximation of pi is 3.3396825396825403
```

---

## 📊 How Grading Works

The grader runs your program with test inputs and checks:

✓ **Calculation accuracy** - π value within 0.1% tolerance  
✓ **Label presence** - Output contains "approximation" or "pi"  
✓ **Execution** - Program completes within 2 seconds  

The grader tests with:
- 5 iterations
- 10 iterations  
- 100 iterations (better approximation)

---

## ❌ Common Mistakes

| Mistake | Points Lost | Why |
|---------|-------------|-----|
| Missing "pi" or "approximation" | -20 | Output needs these words |
| Wrong denominators | -80 | Must be odd numbers: 2i+1 |
| Not alternating signs | -80 | Pattern is +, -, +, -, ... |
| Forgetting to multiply by 4 | -80 | Formula gives π/4, not π |
| Starting at i=1 instead of i=0 | -80 | First term should be 1/1 |

---

## 💡 Tips for Success

1. **Loop from 0 to iterations-1**: Use `range(iterations)`
2. **Odd denominators**: `2*i + 1` gives 1, 3, 5, 7, ...
3. **Alternate signs**: Use `if i % 2 == 0` (even indices are positive)
4. **Accumulate the sum**: Add each term to a running total
5. **Multiply by 4 at the end**: Result is π/4, so multiply to get π

### Code Pattern:
```python
iterations = int(input("Enter the number of iterations: "))

sum_total = 0.0

for i in range(iterations):
    denominator = 2 * i + 1
    term = 1.0 / denominator
    
    if i % 2 == 0:  # Even index = positive
        sum_total += term
    else:           # Odd index = negative
        sum_total -= term

pi_approx = sum_total * 4
print(f"\nThe approximation of pi is {pi_approx}")
```

### Alternative (Using Powers):
```python
for i in range(iterations):
    term = ((-1) ** i) / (2 * i + 1)
    sum_total += term
```

### Common Logic Errors:
```python
# Wrong - even denominators
denominator = 2 * i  # Gives 0, 2, 4, 6... not 1, 3, 5, 7

# Wrong - signs backwards
if i % 2 == 0:
    sum_total -= term  # Should be adding!

# Wrong - forgot to multiply by 4
print(sum_total)  # This is π/4, not π

# Wrong - starting at 1
for i in range(1, iterations + 1):  # Skips the 1/1 term
```

---

## 🧪 Test Your Code

From the `student/` directory:
```bash
../../tools/grade.sh
```

Check your report in `../report_ex06/report.txt`

**Verify with example:**
- 5 iterations ≈ 3.3397
- 100 iterations ≈ 3.1316 (closer to real π ≈ 3.14159)

---

## 📚 Key Concepts

This exercise practices:
- `for` loops with `range()`
- Accumulator pattern (sum)
- Alternating series (changing signs)
- Modulo operator (`%`) for even/odd
- Generating sequences (odd numbers)
- Mathematical approximations
