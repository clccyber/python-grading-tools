# Grading Rubric: Chapter 4, Exercise 4a
## Decimal to Octal Conversion 🔢

---

## 📋 What You're Building

Convert decimal (base 10) integers to octal (base 8):
- Prompt for a decimal integer
- Convert to octal representation
- Display the result

**Example:**
```
Enter a decimal integer: 111
The octal representation is 157
```

---

## 🎯 Point Breakdown (100 Total)

| Category | Points |
|----------|--------|
| **Correct Conversion** | 80 |
| **Output Format** | 20 |

---

## 📐 Conversion Logic

**Octal uses digits 0-7 (base 8)**

**Algorithm (like binary conversion but with 8):**
```python
def decimal_to_octal(decimal):
    if decimal == 0:
        return "0"
    
    octal = ""
    while decimal > 0:
        remainder = decimal % 8  # Get next octal digit
        octal = str(remainder) + octal  # Prepend to result
        decimal = decimal // 8  # Remove last digit
    
    return octal
```

**How it works:**
```
111 ÷ 8 = 13 remainder 7  → rightmost digit is 7
 13 ÷ 8 = 1  remainder 5  → next digit is 5
  1 ÷ 8 = 0  remainder 1  → leftmost digit is 1

Result: 157
```

---

## ✅ Expected Behavior

| Input | Output |
|-------|--------|
| 111 | 157 |
| 8 | 10 |
| 0 | 0 |
| 512 | 1000 |
| 64 | 100 |

---

## ❌ Common Mistakes

| Mistake | Points Lost |
|---------|-------------|
| Wrong conversion | -80 |
| Digits reversed | -60 |
| Doesn't handle 0 | -40 |
| Wrong output format | -20 |

---

## 💡 Tips

### 1. Use Repeated Division
```python
decimal = int(input("Enter a decimal integer: "))
octal = ""

while decimal > 0:
    digit = decimal % 8
    octal = str(digit) + octal  # Build right-to-left
    decimal //= 8

print(f"The octal representation is {octal}")
```

### 2. Handle Zero Special Case
```python
if decimal == 0:
    print("The octal representation is 0")
else:
    # conversion logic
```

### 3. Build String Right-to-Left
```python
# Right way - prepend each digit
octal = str(digit) + octal  # "7" + "" = "7", "5" + "7" = "57"

# Wrong way - append
octal = octal + str(digit)  # Would give "751" instead of "157"
```

---

## 🧪 Test Your Code

```bash
python decimaltooctal.py
# Try: 111 → should be 157
# Try: 8 → should be 10
# Try: 0 → should be 0
# Try: 64 → should be 100
```

---

## Key Concepts

- Number base conversion
- Repeated division algorithm
- Modulo operator (`%`)
- Integer division (`//`)
- String building
- Loop patterns
