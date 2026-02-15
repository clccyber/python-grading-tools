# Grading Rubric: Chapter 5, Exercise 6
## Decimal to Any Base Conversion 🔢

---

## 📋 What You're Building

Function `decimalToRep(decimal, base)` - inverse of ex05:
- Convert decimal to any base (2-16)
- Use lookup table for digits
- Return string representation

**Examples:**
```python
decimalToRep(8, 8)    → "10"
decimalToRep(16, 16)  → "10"
decimalToRep(255, 16) → "FF"
decimalToRep(10, 2)   → "1010"
```

---

## 🎯 Point Breakdown (100 Total)

| Category | Points |
|----------|--------|
| **Lookup Table** | 20 |
| **Conversion Logic** | 50 |
| **String Building** | 15 |
| **Main Function** | 15 |

---

## 💻 Implementation

```python
# Reverse lookup table
DIGITS = {
    0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
    5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
    10: 'A', 11: 'B', 12: 'C', 13: 'D',
    14: 'E', 15: 'F'
}

def decimalToRep(decimal, base):
    """Convert decimal to representation in given base"""
    if decimal == 0:
        return "0"
    
    result = ""
    while decimal > 0:
        remainder = decimal % base
        result = DIGITS[remainder] + result  # Prepend
        decimal //= base
    
    return result

def main():
    print(decimalToRep(8, 8))     # "10"
    print(decimalToRep(16, 16))   # "10"
    print(decimalToRep(255, 16))  # "FF"
    print(decimalToRep(10, 2))    # "1010"
```

---

## ✅ Test Cases

| Input | Base | Output |
|-------|------|--------|
| 8 | 8 | "10" |
| 16 | 16 | "10" |
| 255 | 16 | "FF" |
| 10 | 2 | "1010" |
| 26 | 16 | "1A" |

---

## Key Concepts

- Repeated division algorithm
- Reverse lookup tables
- String building (prepend)
- Inverse operations
- Hexadecimal representation
