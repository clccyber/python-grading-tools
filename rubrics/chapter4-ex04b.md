# Grading Rubric: Chapter 4, Exercise 4b
## Octal to Decimal Conversion 🔢

---

## 📋 What You're Building

Convert octal (base 8) to decimal (base 10):
- Prompt for an octal string
- Convert to decimal integer
- Display the result

**Example:**
```
Enter a string of octal digits: 157
The integer value is 111
```

---

## 🎯 Point Breakdown (100 Total)

| Category | Points |
|----------|--------|
| **Correct Conversion** | 80 |
| **Output Format** | 20 |

---

## 📐 Conversion Logic

**Read digits left-to-right, multiply by powers of 8:**

```python
def octal_to_decimal(octal_str):
    decimal = 0
    power = 0
    
    # Process right-to-left
    for digit in reversed(octal_str):
        decimal += int(digit) * (8 ** power)
        power += 1
    
    return decimal
```

**How it works for "157":**
```
Position:  2   1   0  (powers of 8)
Digit:     1   5   7

7 × 8⁰ = 7 × 1   = 7
5 × 8¹ = 5 × 8   = 40
1 × 8² = 1 × 64  = 64
                   ---
Total:             111
```

---

## ✅ Expected Behavior

| Input | Output |
|-------|--------|
| 157 | 111 |
| 10 | 8 |
| 0 | 0 |
| 1000 | 512 |
| 100 | 64 |

---

## 💡 Tips

### Algorithm Pattern
```python
octal = input("Enter a string of octal digits: ")
decimal = 0

for i, digit in enumerate(reversed(octal)):
    decimal += int(digit) * (8 ** i)

print(f"The integer value is {decimal}")
```

### Alternative - Process Left-to-Right
```python
decimal = 0
for digit in octal:
    decimal = decimal * 8 + int(digit)
```

---

## Key Concepts

- Base conversion (octal → decimal)
- Powers of 8
- String iteration
- Positional notation
