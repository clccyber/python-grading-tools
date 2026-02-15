# Grading Rubric: Chapter 4, Exercise 2
## Caesar Cipher Decryption 🔓

---

## 📋 What You're Building

A program that decrypts Caesar cipher text:
- Reverses the encryption by shifting backwards
- Works on ALL printable characters
- Wraps around correctly

**Example:**
```
Enter the coded text: Khoor#Zruog$
Enter the distance value: 3
Hello World!
```

---

## 🎯 Point Breakdown (100 Total)

| Category | Points | What's Graded |
|----------|--------|---------------|
| **Correct Decryption** | 80 | Output matches expected plaintext |
| **Output Format** | 20 | Displays decrypted result |

---

## 📐 Decryption Logic

**Key insight:** Decryption is just encryption with negative distance!

```python
# If encryption adds:
encrypted = chr(ord(char) + distance)

# Then decryption subtracts:
decrypted = chr(ord(char) - distance)
```

**Even simpler approach:**
```python
# Reuse your encrypt function!
def decrypt(text, distance):
    return encrypt(text, -distance)
```

---

## ✅ Expected Behavior

**Test Case 1: Basic decrypt**
```
Input: "BCD"
Distance: 1
Output: "ABC"
```

**Test Case 2: Wrap around backwards**
```
Input: "]^_"
Distance: 5
Output: "XYZ"
```

**Test Case 3: Negative distance (encrypts!)**
```
Input: "BCD"
Distance: -2
Output: "DEF"  # Negative shift = forward
```

**Test Case 4: Numbers and special**
```
Input: "Xiwx567%"
Distance: 4
Output: "Test123!"
```

---

## ❌ Common Mistakes

| Mistake | Points Lost | Why |
|---------|-------------|-----|
| Only decrypts letters | -80 | Must work on ALL printable chars |
| Wrong direction | -80 | Should shift backwards (subtract) |
| Doesn't wrap around | -40 | Must handle going below ASCII 32 |
| Forgot negative distance | -40 | Negative shift should encrypt |

---

## 💡 Tips for Success

### 1. Simplest Solution - Reuse Encryption!
```python
def encrypt(text, distance):
    # Your encryption code from ex01
    result = ""
    for char in text:
        shifted = ord(char) + distance
        result += chr(shifted)
    return result

def decrypt(text, distance):
    # Just encrypt with negative distance!
    return encrypt(text, -distance)
```

### 2. Or Write Explicit Decryption
```python
def decrypt(text, distance):
    result = ""
    for char in text:
        code = ord(char)
        shifted = code - distance  # Subtract instead of add
        result += chr(shifted)
    return result
```

### 3. Handle Wrap-Around
```python
# With modulo for printable ASCII range
MIN_ASCII = 32
MAX_ASCII = 126
RANGE = 95  # MAX - MIN + 1

def decrypt_char(char, distance):
    code = ord(char) - MIN_ASCII
    shifted = (code - distance) % RANGE
    return chr(shifted + MIN_ASCII)
```

### 4. Test Symmetry
```python
# These should match:
original = "Hello World!"
encrypted = encrypt(original, 5)
decrypted = decrypt(encrypted, 5)
assert original == decrypted  # Should be True!
```

---

## 🧪 Test Your Code

From the `student/` directory:
```bash
python ../../tools/grade.py
```

**Verify encryption/decryption symmetry:**
```python
# Test that encrypt → decrypt = original
text = "Test message 123!"
distance = 7

encrypted = encrypt(text, distance)
decrypted = decrypt(encrypted, distance)

print(f"Original:  {text}")
print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")
print(f"Match: {text == decrypted}")  # Should be True
```

---

## 📚 Key Concepts

This exercise practices:
- Inverse operations (encryption ↔ decryption)
- Code reuse (decrypt can use encrypt!)
- Negative arithmetic
- Understanding symmetric ciphers
- DRY principle (Don't Repeat Yourself)

---

## 🔍 Debugging Tips

**If decryption doesn't work:**
1. Test encryption first - does it work correctly?
2. Verify: `decrypt(encrypt(text, n), n) == text`
3. Check wrap-around with characters near boundaries
4. Try negative distances - should encrypt instead!

**Testing strategy:**
```python
# Test each case individually
test_cases = [
    ("BCD", 1, "ABC"),
    ("ABC", -1, "BCD"),  # Negative = encrypt
    ("]^_", 5, "XYZ"),   # Wrap around
]

for encrypted, dist, expected in test_cases:
    result = decrypt(encrypted, dist)
    status = "✓" if result == expected else "✗"
    print(f"{status} decrypt('{encrypted}', {dist}) = '{result}' (expected '{expected}')")
```

---

## 🎓 The Beauty of Symmetric Ciphers

**Caesar cipher is symmetric:**
- Same key encrypts and decrypts
- Decryption is just encryption backwards
- Simple but demonstrates core concept

**Real-world symmetric ciphers:**
- AES (Advanced Encryption Standard)
- DES (Data Encryption Standard)
- Same principle: one key, two directions
- Much more complex algorithms

**Your Caesar cipher teaches:**
- How encryption reverses
- Why key management matters
- Foundation for understanding cryptography
