# Grading Rubric: Chapter 6, Exercise 7
## Robust Float Input 🔢

---

## 📋 What You're Building

Add `inputFloat()` to testinputfunctions module:
- Validates input is valid float
- Allows digits and single decimal point
- Prompts repeatedly until valid
- Returns float value

**Examples:**
```
Please enter an integer or a float: 10.11
10.11

Please enter an integer or a float: 11.12.11
Error: the input cannot have more than one '.'
Please enter an integer or a float: 5
5.0
```

---

## 🎯 Point Breakdown (100 Total)

| Category | Points |
|----------|--------|
| **Valid Input** | 40 |
| **Decimal Validation** | 30 |
| **Error Handling** | 30 |

---

## 💻 Implementation Pattern

```python
def inputFloat(prompt="Please enter an integer or a float: "):
    """Robust float input with validation"""
    while True:
        userInput = input(prompt)
        
        # Check for multiple decimal points
        if userInput.count('.') > 1:
            print("Error: the input cannot have more than one '.'")
            continue
        
        # Check all characters are digits or decimal
        valid = True
        for char in userInput:
            if not (char.isdigit() or char == '.'):
                print("Error: the input must consist only of digits")
                valid = False
                break
        
        if not valid:
            continue
        
        # Convert and return
        return float(userInput)
```

---

## ✅ Test Cases

| Input | Result |
|-------|--------|
| "10.11" | 10.11 |
| "5" | 5.0 |
| "11.12.11" | Error, re-prompt |
| "eight.two" | Error, re-prompt |
| "10" | 10.0 |

---

## Key Concepts

- Input validation loops
- String analysis
- Error messages
- Type conversion
