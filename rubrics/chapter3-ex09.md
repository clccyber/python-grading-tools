# Grading Rubric: Chapter 3, Exercise 9
## Sum and Average with Variable Input 🔢

---

## 📋 What You're Building

A program that:
- Accepts numbers from the user (one per line)
- Keeps reading until user presses Enter on a blank line
- Outputs the sum and average of all entered numbers

**Key concept:** Loop that continues until a specific condition (blank input).

---

## 🎯 Point Breakdown (100 Total)

| Category | Points | What's Graded |
|----------|--------|---------------|
| **Numeric Correctness** | 80 | Sum and average calculated correctly |
| **Labels & Output** | 20 | Output includes "sum" and "average" |

---

## 📐 The Logic

```python
# Keep reading numbers until blank line
numbers = []
while True:
    user_input = input("Enter a number or press Enter to quit: ")
    if user_input == "":
        break  # Stop on blank line
    numbers.append(float(user_input))

# Calculate sum and average
total = sum(numbers)
average = total / len(numbers)
```

---

## ✅ Expected Output Format

Your program should:
- Prompt for numbers repeatedly
- Stop when user enters blank line (just presses Enter)
- Display sum and average

**Example:**
```
Enter a number or press Enter to quit: 1
Enter a number or press Enter to quit: 2
Enter a number or press Enter to quit: 3
Enter a number or press Enter to quit: 

The sum is 6.0
The average is 2.0
```

---

## 📊 How Grading Works

The grader sends multiple numbers followed by a blank line:
```
1
2
3
[blank line]
```

Then checks:
✓ **Sum is correct** - 1 + 2 + 3 = 6.0  
✓ **Average is correct** - 6.0 / 3 = 2.0  
✓ **Labels present** - Output contains "sum" and "average"  

**Test cases:**
- 3 numbers (1, 2, 3)
- 5 numbers (10, 20, 30, 40, 50)
- 1 number (42)

---

## ❌ Common Mistakes

| Mistake | Points Lost | Why |
|---------|-------------|-----|
| Missing labels | -20 | Must include "sum" and "average" |
| Wrong sum | -40 | Basic addition error |
| Wrong average | -40 | Divide sum by count |
| Dividing by 0 | -100 | If no numbers entered (edge case) |
| Not stopping on blank | -100 | Loop never ends |
| Using fixed count | -100 | Must loop until blank, not ask "how many?" |

---

## 💡 Tips for Success

1. **Blank line detection**: `if user_input == ""`
2. **Accumulate in a list**: Easier than tracking sum during input
3. **Use sum() function**: `total = sum(numbers)`
4. **Average = sum / count**: `average = total / len(numbers)`
5. **Check for empty list**: Avoid division by zero

### Code Pattern:
```python
numbers = []

while True:
    user_input = input("Enter a number or press Enter to quit: ")
    
    if user_input == "":
        break
    
    numbers.append(float(user_input))

# Calculate results
total = sum(numbers)
average = total / len(numbers) if len(numbers) > 0 else 0

print(f"\nThe sum is {total}")
print(f"The average is {average}")
```

### Alternative (Without List):
```python
count = 0
total = 0.0

while True:
    user_input = input("Enter a number or press Enter to quit: ")
    
    if user_input == "":
        break
    
    total += float(user_input)
    count += 1

average = total / count if count > 0 else 0

print(f"\nThe sum is {total}")
print(f"The average is {average}")
```

### Common Logic Errors:
```python
# Wrong - checking wrong condition
if user_input == "quit":  # Should be == ""

# Wrong - asking for count first
n = int(input("How many numbers? "))  # Exercise says "press Enter to quit"

# Wrong - division by zero
average = total / len(numbers)  # Crashes if numbers is empty

# Wrong - not converting to float
numbers.append(user_input)  # Should be float(user_input)
```

---

## 🧪 Test Your Code

From the `student/` directory:
```bash
../../tools/grade.sh
```

**Manual testing:**
```
$ python sum.py
Enter a number: 5
Enter a number: 10
Enter a number: 15
Enter a number: [press Enter]

The sum is 30.0
The average is 10.0
```

Try:
- Multiple numbers
- Single number
- Edge case: Just press Enter (no numbers) - should handle gracefully

---

## 📚 Key Concepts

This exercise practices:
- `while True:` with `break` condition
- Checking for empty string (`""`)
- Accumulating values in a list
- `sum()` function
- `len()` function
- Division (average calculation)
- Handling edge cases (empty list)
- Variable-length input (unknown count ahead of time)

---

## 🎓 The Pattern

**This is a fundamental programming pattern:**
```python
# Sentinel-controlled loop (blank line is the "sentinel")
while True:
    value = get_input()
    if value == SENTINEL:  # Stop condition
        break
    process(value)
```

You'll use this pattern for:
- Reading files line by line
- Processing user input
- Menu systems ("enter 0 to quit")
- Data validation loops
