# Grading Rubric: Chapter 5, Exercise 5
## Any Base to Decimal Conversion 🔢

---

## 📋 What You're Building

Function `repToDecimal(string, base)` that converts any base to decimal:
- Support bases 2-16
- Use lookup table (dictionary) for digits
- Handle A-F for hex (values 10-15)

**Examples:**
```python
repToDecimal("10", 8)   → 8
repToDecimal("10", 16)  → 16
repToDecimal("FF", 16)  → 255
repToDecimal("1010", 2) → 10
```

---

## 🎯 Point Breakdown (100 Total)

| Category | Points |
|----------|--------|
| **Lookup Table** | 20 |
| **Conversion Logic** | 50 |
| **Case Handling** | 15 |
| **Main Function** | 15 |

---

## 💻 Implementation

```python
# Lookup table (dictionary)
DIGIT_VALUES = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
    '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13,
    'E': 14, 'F': 15
}

def repToDecimal(rep, base):
    """Convert representation in given base to decimal"""
    decimal = 0
    power = 0
    
    # Process right to left
    for digit in reversed(rep.upper()):
        value = DIGIT_VALUES[digit]
        decimal += value * (base ** power)
        power += 1
    
    return decimal

def main():
    print(repToDecimal("10", 8))    # 8
    print(repToDecimal("10", 16))   # 16
    print(repToDecimal("FF", 16))   # 255
    print(repToDecimal("1010", 2))  # 10
```

---

## ✅ Test Cases

| Input | Base | Output |
|-------|------|--------|
| "10" | 8 | 8 |
| "10" | 16 | 16 |
| "FF" | 16 | 255 |
| "1010" | 2 | 10 |
| "1A" | 16 | 26 |

---

## Key Concepts

- Dictionaries as lookup tables
- Positional notation
- Powers of base
- Case conversion (`.upper()`)
- Generalized base conversion
