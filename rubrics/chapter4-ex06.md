# Grading Rubric: Chapter 4, Exercise 6
## Bit-Based Encryption 🔐💾

---

## 📋 What You're Building

Encrypt text using bit operations:
1. Add 1 to each character's ASCII value
2. Convert to binary
3. Shift bits one place left
4. Output space-separated bit strings

**Example:**
```
Enter a message: Hello World!
0010011 1001101 1011011 1011011 1100001 000011 0110001 1100001 1100111 1011011 1001011 000101
```

---

## 🎯 Point Breakdown (100 Total)

| Category | Points |
|----------|--------|
| **Correct Encryption** | 80 |
| **Output Format** | 20 |

---

## 📐 Encryption Algorithm

**For each character:**
1. Get ASCII: `ord(char)`
2. Add 1: `ascii + 1`
3. Convert to binary: `bin(ascii + 1)[2:]`
4. Shift left: `binary[1:] + binary[0]`

```python
def encrypt_char(char):
    # Step 1: ASCII + 1
    code = ord(char) + 1
    
    # Step 2: To binary (remove '0b' prefix)
    binary = bin(code)[2:]
    
    # Step 3: Shift left
    shifted = binary[1:] + binary[0]
    
    return shifted
```

---

## ✅ Expected Output

**For "Hello World!":**
```
H → 72 + 1 = 73 → 1001001 → shift → 0010011
e → 101 + 1 = 102 → 1100110 → shift → 1001101
...
```

Space-separated bit strings on one line.

---

## 💡 Complete Program

```python
message = input("Enter a message: ")
encrypted = []

for char in message:
    # Add 1 to ASCII
    code = ord(char) + 1
    
    # Convert to binary (remove '0b')
    binary = bin(code)[2:]
    
    # Shift left
    shifted = binary[1:] + binary[0]
    
    encrypted.append(shifted)

# Print space-separated
print(' '.join(encrypted))
```

---

## ❌ Common Mistakes

| Mistake | Points Lost |
|---------|-------------|
| Wrong binary conversion | -60 |
| Not shifting bits | -40 |
| Not adding 1 to ASCII | -40 |
| Wrong separator (not space) | -20 |
| Leading zeros lost | -20 |

---

## Key Concepts

- ASCII encoding (`ord()`)
- Binary conversion (`bin()`)
- Bit shifting
- String manipulation
- Combining operations
