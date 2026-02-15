# Grading Rubric: Chapter 4, Exercise 7
## Bit-Based Decryption 🔓💾

---

## 📋 What You're Building

Decrypt bit-encoded messages:
1. Take space-separated bit strings
2. Shift bits one place right
3. Convert binary to decimal
4. Subtract 1 to get ASCII
5. Convert to character

**Example:**
```
Enter the coded text: 0010011 1001101 1011011 1011011 1100001 000011 0110001 1100001 1100111 1011011 1001011 000101
Hello World!
```

---

## 🎯 Point Breakdown (100 Total)

| Category | Points |
|----------|--------|
| **Correct Decryption** | 80 |
| **Output Format** | 20 |

---

## 📐 Decryption Algorithm

**For each bit string:**
1. Shift right: `bits[-1] + bits[:-1]`
2. Convert to decimal: `int(bits, 2)`
3. Subtract 1: `decimal - 1`
4. Convert to char: `chr(decimal - 1)`

```python
def decrypt_bits(bits):
    # Step 1: Shift right (reverse of encryption)
    shifted = bits[-1] + bits[:-1]
    
    # Step 2: Binary to decimal
    decimal = int(shifted, 2)
    
    # Step 3: Subtract 1 (reverse of +1)
    ascii_code = decimal - 1
    
    # Step 4: To character
    return chr(ascii_code)
```

---

## ✅ Expected Output

**For bit string "0010011":**
```
Shift right: 0010011 → 1001001
To decimal: 1001001 → 73
Subtract 1: 73 - 1 = 72
To char: 72 → 'H'
```

---

## 💡 Complete Program

```python
coded = input("Enter the coded text: ")
bit_strings = coded.split()  # Split by spaces

decrypted = ""
for bits in bit_strings:
    # Shift right
    shifted = bits[-1] + bits[:-1]
    
    # Binary to decimal
    decimal = int(shifted, 2)
    
    # Subtract 1 and convert to char
    char = chr(decimal - 1)
    
    decrypted += char

print(decrypted)
```

---

## ❌ Common Mistakes

| Mistake | Points Lost |
|---------|-------------|
| Wrong shift direction | -60 |
| Not converting binary | -60 |
| Not subtracting 1 | -40 |
| Not splitting by space | -40 |

---

## Key Concepts

- Reverse operations
- Binary to decimal (`int(str, 2)`)
- Bit shifting (right = undo left)
- String splitting
- Character decoding (`chr()`)
