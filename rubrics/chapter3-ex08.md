# Grading Rubric: Chapter 3, Exercise 8
## Greatest Common Divisor (Euclidean Algorithm) 🔢

---

## 📋 What You're Building

A program that finds the Greatest Common Divisor (GCD) of two numbers using Euclid's algorithm.

**The GCD** is the largest number that divides evenly into both numbers.

**Example:** GCD(15, 5) = 5 (because 5 divides both 15 and 5)

---

## 🎯 Point Breakdown (100 Total)

| Category | Points | What's Graded |
|----------|--------|---------------|
| **Numeric Correctness** | 80 | GCD calculation is accurate |
| **Labels & Output** | 20 | Output includes "greatest common divisor" or "gcd" |

---

## 📐 Euclid's Algorithm

**Steps:**
1. Divide the larger number by the smaller number, get remainder
2. Replace larger with smaller, smaller with remainder
3. Repeat until remainder is 0
4. The last non-zero remainder is the GCD

**Example:** GCD(15, 5)
```
15 ÷ 5 = 3 remainder 0
Remainder is 0, so GCD = 5
```

**Example:** GCD(48, 18)
```
48 ÷ 18 = 2 remainder 12
18 ÷ 12 = 1 remainder 6
12 ÷ 6 = 2 remainder 0
Remainder is 0, so GCD = 6
```

---

## ✅ Expected Output Format

Your program should:
- Prompt for smaller number
- Prompt for larger number
- Calculate GCD using the algorithm
- Display the result

**Example:**
```
Enter the smaller number: 5
Enter the larger number: 15

The greatest common divisor is 5
```

---

## 📊 How Grading Works

The grader runs your program with test inputs and checks:

✓ **Calculation accuracy** - GCD value is correct  
✓ **Label presence** - Output contains "greatest common divisor" or "gcd"  
✓ **Execution** - Program completes within 2 seconds  

Test cases include:
- 5 and 15 → GCD is 5
- 7 and 13 → GCD is 1 (coprime)
- 12 and 12 → GCD is 12 (same number)
- 99 and 100 → GCD is 1 (consecutive)

---

## ❌ Common Mistakes

| Mistake | Points Lost | Why |
|---------|-------------|-----|
| Missing GCD label | -20 | Output needs "greatest common divisor" or "gcd" |
| Not implementing algorithm | -80 | Can't just guess or use trial division |
| Infinite loop | -100 | Algorithm must terminate |
| Wrong remainder calculation | -80 | Use modulo operator `%` |

---

## 💡 Tips for Success

1. **Use the modulo operator**: `a % b` gives the remainder
2. **Loop until remainder is 0**: `while` loop is natural here
3. **Update both variables each iteration**: Shift larger→smaller, remainder→new smaller
4. **Python has `math.gcd()`**: But implement the algorithm yourself for practice!

### Code Pattern (While Loop):
```python
a = int(input("Enter the smaller number: "))
b = int(input("Enter the larger number: "))

# Ensure a <= b
if a > b:
    a, b = b, a

# Euclidean algorithm
while a != 0:
    remainder = b % a
    b = a
    a = remainder

gcd = b
print(f"\nThe greatest common divisor is {gcd}")
```

### Alternative (Using math.gcd):
```python
import math

a = int(input("Enter the smaller number: "))
b = int(input("Enter the larger number: "))

gcd = math.gcd(a, b)
print(f"\nThe greatest common divisor is {gcd}")
```

**Note:** Either approach is fine! The instructions ask you to "print each step," but for grading we just check the final answer.

### Common Logic Errors:
```python
# Wrong - using division instead of modulo
remainder = b / a  # Should be b % a

# Wrong - not updating variables
while a != 0:
    remainder = b % a  # Calculate but don't update!

# Wrong - checking wrong condition
while remainder != 0:  # Should check 'a != 0'
```

---

## 🧪 Test Your Code

From the `student/` directory:
```bash
../../tools/grade.sh
```

Check your report in `../report_ex08/report.txt`

**Test manually:**
- GCD(5, 15) = 5
- GCD(7, 13) = 1 (no common factors)
- GCD(12, 12) = 12
- GCD(48, 18) = 6

---

## 📚 Key Concepts

This exercise practices:
- `while` loops
- Modulo operator (`%`)
- Variable swapping
- Algorithm implementation
- Loop termination conditions
- Using `math.gcd()` (optional)
