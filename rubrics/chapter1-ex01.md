# Grading Rubric: Chapter 1, Exercise 1
## Personal Information Display

---

## 📋 What You're Building

A Python program that displays your personal information:
- **File:** `myinfo.py`
- **Output:** Name, address, phone number (each on separate line)
- **Concept:** Basic `print()` statements

**Example output:**
```
Jane Doe
Virginia
555-0150
```

---

## 🎯 Point Breakdown (100 Total)

| Category | Points |
|----------|--------|
| **File Named Correctly** | 10 |
| **Program Runs** | 20 |
| **Name Displayed** | 25 |
| **Address Displayed** | 25 |
| **Phone Displayed** | 20 |

---

## 💻 Implementation

```python
# myinfo.py
print("Your Name")
print("Your Address")
print("555-1234")
```

**Key points:**
- Three separate `print()` statements
- Each on its own line
- Order matters: name, address, phone

---

## ✅ What to Check

### File Name (10 pts)
- ✓ Named `myinfo.py` (case-sensitive)
- ✗ `myInfo.py`, `MyInfo.py`, `info.py` are wrong

### Program Runs (20 pts)
- ✓ No syntax errors
- ✓ Executes without crashing
- ✗ `SyntaxError`, `NameError`, etc.

### Output Content (70 pts)
- ✓ Name on first line (25 pts)
- ✓ Address on second line (25 pts)
- ✓ Phone on third line (20 pts)
- ✓ Each on separate line (included in above)

---

## Common Mistakes

❌ **Quotes issues:**
```python
print(Jane Doe)  # Missing quotes - NameError
```
✅ **Correct:**
```python
print("Jane Doe")
```

❌ **Everything on one line:**
```python
print("Jane Doe Virginia 555-0150")
```
✅ **Correct - separate lines:**
```python
print("Jane Doe")
print("Virginia")
print("555-0150")
```

❌ **Wrong file name:**
```python
# Saved as info.py instead of myinfo.py
```

---

## Key Concepts

- **`print()` function** - Displays output
- **String literals** - Text in quotes
- **Multiple statements** - One per line
- **File naming** - Exact names matter

---

## Notes

- This is Chapter 1 - very basic!
- Main goal: Get comfortable with Python syntax
- Practice running programs
- Understanding print statements

**Full credit if:** Program runs and displays three pieces of info on separate lines.
