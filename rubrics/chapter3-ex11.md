# Grading Rubric: Chapter 3, Exercise 11
## Lucky Sevens Dice Game 🎲

---

## 📋 What You're Building

A simulation that demonstrates why the "Lucky Sevens" casino game is rigged against the player:
- Roll two dice each round
- If sum = 7: Win $4
- Otherwise: Lose $1
- Keep playing until broke
- Report how many rolls it took and when player had maximum money

**Key lesson:** Even though there are 6 ways to make 7 (1+6, 2+5, 3+4, 4+3, 5+2, 6+1), the odds don't favor the player.

---

## 🎯 Point Breakdown (100 Total)

| Category | Points | What's Graded |
|----------|--------|---------------|
| **Game Simulation** | 60 | Correct dice rolling, win/loss logic, tracking |
| **Output Format** | 40 | Reports rolls to broke and max money correctly |

---

## 📐 The Game Rules

```python
# Each roll:
die1 = random.randint(1, 6)
die2 = random.randint(1, 6)
total = die1 + die2

if total == 7:
    money += 4  # Win
else:
    money -= 1  # Lose

# Track maximum
if money > max_money:
    max_money = money
    max_roll = current_roll
```

**The math:** 6 ways to make 7 out of 36 possible rolls = 16.7% chance
- Expected value per roll: (6/36)×$4 + (30/36)×(-$1) = -$0.17
- You LOSE money over time!

---

## ✅ Expected Output Format

Your program should:
- Prompt for starting money
- Simulate dice rolls until money = 0
- Report:
  - Number of rolls to go broke
  - Roll number when money was maximum
  - Maximum amount of money

**Example:**
```
How many dollars do you have? 50

You are broke after 220 rolls.
You should have quit after 6 rolls when you had $59.
```

---

## 📊 How Grading Works

**Here's the clever part:** The grader uses a **seeded random number generator** to make your dice rolls predictable.

This means:
- Same starting money + same seed = same sequence of rolls
- Grader can verify your simulation is correct
- Your code doesn't need any changes!

**What the grader checks:**
✓ **Correct roll count** - With seed X, should take Y rolls to go broke  
✓ **Correct maximum** - Should reach max of $Z at roll N  
✓ **Proper output format** - Messages contain required information  

**Test cases:**
- $10 starting (small pot, quick game)
- $50 starting (medium pot)
- $100 starting (large pot, longer game)

---

## ❌ Common Mistakes

| Mistake | Points Lost | Why |
|---------|-------------|-----|
| Wrong win/loss amounts | -60 | Win $4 on 7, lose $1 otherwise |
| Not tracking maximum | -40 | Must remember highest money AND when |
| Wrong dice range | -60 | Dice are 1-6, not 0-5 or 1-5 |
| Never ending game | -100 | Must stop when money ≤ 0 |
| Not using random | -60 | Must roll dice randomly |

---

## 💡 Tips for Success

1. **Import random**: `import random` at the top
2. **Roll two separate dice**: `random.randint(1, 6)` twice
3. **Track three things**: current money, max money, roll at max
4. **Loop while money > 0**: Game continues until broke
5. **Update max every time**: Check after each roll if current > max

### Code Pattern:
```python
import random

money = int(input("How many dollars do you have? "))

max_money = money
max_roll = 0
rolls = 0

while money > 0:
    rolls += 1
    
    # Roll two dice
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2
    
    # Apply game rules
    if total == 7:
        money += 4
    else:
        money -= 1
    
    # Track maximum
    if money > max_money:
        max_money = money
        max_roll = rolls

# Report results
print(f"\nYou are broke after {rolls} rolls.")
print(f"You should have quit after {max_roll} rolls when you had ${max_money}.")
```

### Common Logic Errors:
```python
# Wrong - dice are 1-6, not 0-5
die1 = random.randint(0, 5)

# Wrong - only rolling once
total = random.randint(2, 12)  # This isn't how dice probabilities work!

# Wrong - wrong win/loss amounts
if total == 7:
    money += 1  # Should be +4

# Wrong - not tracking max correctly
max_money = money  # This should be INSIDE the loop

# Wrong - updating max after game ends
if money > max_money:  # This needs to be DURING the loop
```

### Why Track Maximum?
```python
# The point of the exercise:
# Even if you get lucky early and are up to $60,
# you'll eventually lose it all.
# The output shows "you should have quit when you were ahead!"
```

---

## 🧪 Test Your Code

From the `student/` directory:
```bash
../../tools/grade.sh
```

**Manual testing:**
- Try with $10 - should go broke fairly quickly
- Try with $100 - takes longer but still goes broke
- Run multiple times - different results (random!)
- Check that you report max money and when it occurred

---

## 📚 Key Concepts

This exercise practices:
- `random.randint()` for dice rolls
- `while` loops with condition
- Tracking multiple variables (current, max, roll count)
- Conditional logic (if sum == 7)
- Demonstrating probability through simulation
- Understanding expected value (negative for this game!)

---

## 🎓 The Lesson

**The casino wants you to think:**
- "There are 6 ways to make 7!"
- "That's lots of ways to win!"

**The reality:**
- Win: 6/36 = 16.7% of rolls
- Lose: 30/36 = 83.3% of rolls
- Net: You lose $0.17 per roll on average
- **Conclusion: Don't play this game!**

Your simulation proves this mathematically by showing every player eventually goes broke.
