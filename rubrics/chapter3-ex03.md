# Grading Rubric: Chapter 3, Exercise 3
## Computer Guessing Game with Cheating Detection 🎯

---

## 📋 What You're Building

A program where **the computer guesses your number** using binary search:
- User thinks of a number in a range
- Computer guesses using optimal strategy (binary search)
- User responds with `<` (lower), `>` (higher), or `=` (correct)
- Computer must find it in minimum guesses
- **Bonus:** Detect if user is cheating (contradictory hints)

**Key concepts:** Binary search algorithm, loop with user interaction, cheating detection logic.

---

## 🎯 Point Breakdown (100 Total)

| Category | Points | What's Graded |
|----------|--------|---------------|
| **Finds Number** | 70 | Successfully finds the secret number |
| **Optimal Strategy** | 10 | Uses binary search (finds in ≤ log₂ guesses) |
| **Detects Cheating** | 20 | Catches contradictory user hints |

---

## 📐 The Strategy: Binary Search

**Algorithm:**
1. Guess the midpoint of current range
2. User says `<`, `>`, or `=`
3. Narrow the range based on response
4. Repeat until found

**Optimal guesses:** ⌈log₂(range)⌉
- Range 0-10 (11 numbers) → max 4 guesses
- Range 0-50 (51 numbers) → max 6 guesses
- Range 0-100 (101 numbers) → max 7 guesses

**Example (0-10, secret=5):**
```
Guess 1: (0+10)/2 = 5 → User says "=" → FOUND in 1 guess!
```

**Example (0-10, secret=8):**
```
Guess 1: (0+10)/2 = 5 → User says ">" (higher)
  Range now: 6-10
Guess 2: (6+10)/2 = 8 → User says "=" → FOUND in 2 guesses!
```

---

## ✅ Expected Behavior

Your program should:
- Prompt for lower and upper bounds
- Display current range and guess
- Wait for user input (`<`, `>`, or `=`)
- Update range based on response
- Find number in optimal guesses OR detect cheating

**Example (Honest User):**
```
Enter the smaller number: 0
Enter the larger number: 10

0 10
Your number is 5
Enter =, <, or >: <
0 4
Your number is 2
Enter =, <, or >: >
3 4
Your number is 3
Enter =, <, or >: =
Hooray, I've got it in 3 tries!
```

**Example (Cheating User):**
```
Enter the smaller number: 0
Enter the larger number: 10
0 10
Your number is 5
Enter =, <, or >: <
0 4
Your number is 2
Enter =, <, or >: <
0 1
Your number is 0
Enter =, <, or >: >
1 1
Your number is 1
Enter =, <, or >: >
I'm out of guesses, and you cheated!
```

---

## 📊 How Grading Works

The grader plays as the user (thinks of a secret number) and checks:

✓ **Finds the number** - Correctly identifies when guess equals secret  
✓ **Uses binary search** - Each guess is at the midpoint ±1  
✓ **Optimal guesses** - Finds in ≤ ⌈log₂(range)⌉ guesses  
✓ **Detects cheating** - Catches contradictory hints  

**Test cases:**
- Honest user with various ranges and secret numbers
- User who gives contradictory hints after several guesses

---

## ❌ Common Mistakes

| Mistake | Points Lost | Why |
|---------|-------------|-----|
| Not using binary search | Up to -80 | Linear search takes too many guesses |
| Guessing randomly | Up to -80 | Must guess at midpoint |
| Never finding number | -70 | Core functionality broken |
| No cheating detection | -20 | Required feature missing |
| Wrong range updates | Up to -70 | If `>`, range becomes [guess+1, upper] |
| Off-by-one errors | Up to -10 | Range boundaries wrong |

---

## 💡 Tips for Success

1. **Always guess midpoint**: `guess = (lower + upper) // 2`
2. **Update range correctly**:
   - If user says `>`: `lower = guess + 1`
   - If user says `<`: `upper = guess - 1`
   - If user says `=`: You win!
3. **Track number of guesses**: Compare to `math.log(upper-lower+1, 2)`
4. **Detect cheating**: If range becomes impossible (lower > upper), user cheated

### Code Pattern:
```python
import math

lower = int(input("Enter the smaller number: "))
upper = int(input("Enter the larger number: "))

# Calculate optimal max guesses
max_guesses = math.ceil(math.log(upper - lower + 1, 2))
guesses = 0

while lower <= upper:
    guess = (lower + upper) // 2
    guesses += 1
    
    print(f"{lower} {upper}")
    print(f"Your number is {guess}")
    
    response = input("Enter =, <, or >: ")
    
    if response == '=':
        print(f"Hooray, I've got it in {guesses} tries!")
        break
    elif response == '>':
        lower = guess + 1
    elif response == '<':
        upper = guess - 1
    
    # Check for cheating
    if lower > upper:
        print("I'm out of guesses, and you cheated!")
        break

# Also check if we used all guesses without finding it
if guesses >= max_guesses and lower > upper:
    print("I'm out of guesses, and you cheated!")
```

### Common Logic Errors:
```python
# Wrong - not updating range
while True:
    guess = (lower + upper) // 2  # lower and upper never change!

# Wrong - updating range incorrectly
if response == '>':
    lower = guess  # Should be guess + 1

# Wrong - linear search
guess = lower
while guess <= upper:
    guess += 1  # Not binary search!

# Wrong - no cheating detection
# If lower > upper, that means user gave contradictory hints
```

### Cheating Detection:
```python
# User cheats when range becomes impossible
# Example: Secret is 5
#   You guess 5, user says "<" → upper becomes 4
#   You guess 2, user says ">" → lower becomes 3
#   Now lower(3) < upper(4), but you've run out of guesses
#   User said 5 is too high AND 2 is too low - contradiction!

if lower > upper or guesses > max_guesses:
    print("I'm out of guesses, and you cheated!")
```

---

## 🧪 Test Your Code

From the `student/` directory:
```bash
../../tools/grade.sh
```

The grader will automatically play as the user with various test cases.

**Manual testing:**
- Range 0-10, think of 5
  - Computer should guess 5 first
- Range 0-10, think of 1
  - Computer should find in ≤4 guesses
- Try giving contradictory hints
  - Computer should detect cheating

---

## 📚 Key Concepts

This exercise practices:
- Binary search algorithm
- Integer division (`//`) for midpoint
- `while` loops with range updates
- User input in loops
- `math.log()` and `math.ceil()`
- Logic to detect impossible conditions
- Loop termination conditions
