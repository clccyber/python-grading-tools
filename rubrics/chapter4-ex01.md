# Grading Rubric: Chapter 4, Exercise 1
## Caesar Cipher Encryption 🔐

---

## 📋 What You're Building

A program that encrypts text using the Caesar cipher:
- Shifts each character by a distance value
- Works on ALL printable characters (not just letters!)
- Wraps around when reaching end of character set

**Example:**
```
Enter a message: Hello World!
Enter the distance value: 3
Khoor#Zruog$
```

---

## 🎯 Point Breakdown (100 Total)

| Category | Points | What's Graded |
|----------|--------|---------------|
| **Correct Encryption** | 80 | Output matches expected encrypted text |
| **Output Format** | 20 | Displays encrypted result |

---

## 📐 How Caesar Cipher Works

**Basic concept:**
```python
# For each character:
ascii_value = ord(character)      # Get numeric value
shifted = ascii_value + distance   # Add distance
encrypted_char = chr(shifted)      # Convert back to character
```

**The wrap-around issue:**
- ASCII printable characters: space (32) through ~ (126)
- If you shift past 126, wrap back to 32
- If you shift below 32, wrap to 126

**Proper algorithm:**
```python
def caesar_encrypt(text, distance):
    result = ""
    for char in text:
        # Get ASCII value
        code = ord(char)
        
        # Shift it
        shifted = code + distance
        
        # Wrap around if needed (printable ASCII: 32-126, range of 95)
        # Note: Different implementations work, key is wrapping correctly
        encrypted_char = chr(shifted)
        
        result += encrypted_char
    
    return result
```

---

## ✅ Expected Behavior

**Test Case 1: Basic shift**
```
Input: "ABC"
Distance: 1
Output: "BCD"
```

**Test Case 2: Wrap around**
```
Input: "XYZ"
Distance: 5
Output: "]^_"  # Wraps into special characters
```

**Test Case 3: Negative distance**
```
Input: "DEF"
Distance: -2
Output: "BCD"
```

**Test Case 4: Numbers and special chars**
```
Input: "Test123!"
Distance: 4
Output: "Xiwx567%"
```

---

## ❌ Common Mistakes

| Mistake | Points Lost | Why |
|---------|-------------|-----|
| Only encrypts letters | -80 | Must work on ALL printable chars |
| Doesn't wrap around | -40 | Characters past 126 should wrap |
| Wrong distance applied | -80 | Each char should shift by distance |
| Case-sensitive issues | -20 | Shouldn't matter - shifts ASCII values |
| Output formatting wrong | -20 | Should just print encrypted text |

---

## 💡 Tips for Success

### 1. Use ord() and chr()
```python
char = 'A'
code = ord(char)      # 65
shifted = code + 3     # 68
result = chr(shifted)  # 'D'
```

### 2. Loop Through Each Character
```python
message = input("Enter a message: ")
distance = int(input("Enter the distance value: "))

encrypted = ""
for char in message:
    # Encrypt this character
    encrypted += encrypt_char(char, distance)

print(encrypted)
```

### 3. Handle Wrap-Around
Different approaches work:
```python
# Approach 1: Let Python handle it naturally
shifted_code = ord(char) + distance
encrypted_char = chr(shifted_code)

# Approach 2: Explicit wrapping for printable range (32-126)
MIN_ASCII = 32
MAX_ASCII = 126
RANGE = MAX_ASCII - MIN_ASCII + 1

code = ord(char) - MIN_ASCII  # Normalize to 0-94
shifted = (code + distance) % RANGE  # Wrap with modulo
encrypted_char = chr(shifted + MIN_ASCII)  # Convert back
```

### 4. Test Edge Cases
```python
# Test with:
print(caesar_encrypt("ABC", 1))      # Should be "BCD"
print(caesar_encrypt("xyz", -1))     # Should shift backwards
print(caesar_encrypt("123", 5))      # Numbers shift too!
print(caesar_encrypt("   ", 1))      # Spaces shift too!
```

---

## 🧪 Test Your Code

From the `student/` directory:
```bash
python ../../tools/grade.py
```

**Manual testing:**
```bash
python encrypt.py
# Try the example from instructions
# Try negative numbers
# Try large shifts
# Try special characters
```

---

## 📚 Key Concepts

This exercise practices:
- String iteration (`for char in string`)
- Character encoding (`ord()` and `chr()`)
- Arithmetic on ASCII values
- Modulo operator for wrapping (`%`)
- Building strings character by character
- Understanding Caesar cipher algorithm

---

## 🔍 Debugging Tips

**If your output is wrong:**
1. Print the ASCII value of each character: `print(ord(char))`
2. Print the shifted value: `print(shifted_code)`
3. Print the result character: `print(chr(shifted_code))`
4. Check if you're handling ALL characters (not just letters)

**Common issues:**
```python
# Wrong - only handles letters
if char.isalpha():
    # encrypt
# Should encrypt EVERYTHING

# Wrong - doesn't shift numbers/special chars
if char.isdigit():
    result += char  # Don't skip it, shift it!
```

---

## 🎓 Understanding Caesar Cipher

**Historical context:**
- Named after Julius Caesar
- Used in military communications
- Very simple, very breakable
- Foundation for understanding encryption

**Why it's weak:**
- Only 95 possible keys (for printable ASCII)
- Easy to brute force
- Pattern analysis breaks it quickly
- But great for learning encryption basics!
