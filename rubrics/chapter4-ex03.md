# Grading Rubric: Chapter 4, Exercise 3
## File Encryption/Decryption 📁🔐

---

## 📋 What You're Building

Modify your Caesar cipher programs to work with FILES instead of console input:
- Read plaintext from input file
- Encrypt/decrypt it
- Write result to output file
- Use command-line arguments for filenames

**Usage:**
```bash
python encrypt.py input.txt output.txt 3
python decrypt.py encrypted.txt decrypted.txt 3
```

---

## 🎯 Point Breakdown (100 Total)

| Category | Points | What's Graded |
|----------|--------|---------------|
| **File Correctness** | 80 | Output file has correctly encrypted/decrypted content |
| **File Handling** | 20 | Creates output file, handles file I/O properly |

---

## 📐 Command-Line Arguments

**Your program receives 3 arguments:**
```python
import sys

# sys.argv[0] is the script name
input_file = sys.argv[1]   # First argument: input filename
output_file = sys.argv[2]  # Second argument: output filename
distance = int(sys.argv[3]) # Third argument: shift distance
```

**Example usage:**
```bash
python encrypt.py plain.txt cipher.txt 5
# sys.argv = ['encrypt.py', 'plain.txt', 'cipher.txt', '5']
```

---

## 💻 Code Pattern

### encrypt.py
```python
import sys

def caesar_encrypt(text, distance):
    """Your encryption function from ex01"""
    result = ""
    for char in text:
        result += chr(ord(char) + distance)
    return result

# Get command-line arguments
input_filename = sys.argv[1]
output_filename = sys.argv[2]
distance = int(sys.argv[3])

# Read input file
with open(input_filename, 'r') as infile:
    plaintext = infile.read()

# Encrypt it
encrypted = caesar_encrypt(plaintext, distance)

# Write output file
with open(output_filename, 'w') as outfile:
    outfile.write(encrypted)
```

### decrypt.py
```python
import sys

def caesar_decrypt(text, distance):
    """Your decryption function from ex02"""
    result = ""
    for char in text:
        result += chr(ord(char) - distance)
    return result

# Get command-line arguments
input_filename = sys.argv[1]
output_filename = sys.argv[2]
distance = int(sys.argv[3])

# Read encrypted file
with open(input_filename, 'r') as infile:
    encrypted = infile.read()

# Decrypt it
plaintext = caesar_decrypt(encrypted, distance)

# Write output file
with open(output_filename, 'w') as outfile:
    outfile.write(plaintext)
```

---

## ✅ Expected Behavior

**Test encrypt:**
```bash
# Create input file
echo "Hello World!" > test.txt

# Run encryption
python encrypt.py test.txt encrypted.txt 3

# Check output
cat encrypted.txt
# Should show: Khoor#Zruog$
```

**Test decrypt:**
```bash
# Use encrypted file
python decrypt.py encrypted.txt decrypted.txt 3

# Check output
cat decrypted.txt
# Should show: Hello World!
```

**Test with multi-line file:**
```bash
# Input file with multiple lines
python encrypt.py book.txt coded.txt 5
# Each line should be encrypted
```

---

## ❌ Common Mistakes

| Mistake | Points Lost | Why |
|---------|-------------|-----|
| Output file not created | -80 | Must write to output file |
| Wrong encryption | -80 | Should match ex01/ex02 logic |
| Doesn't handle newlines | -40 | Newlines are characters too! |
| Hardcoded filenames | -60 | Must use command-line args |
| Wrong argument order | -40 | input, output, distance |
| File not closed properly | -20 | Use `with` statement |

---

## 💡 Tips for Success

### 1. Reuse Your Ex01/Ex02 Code
```python
# Copy your encrypt/decrypt functions
# Just add file I/O around them
```

### 2. Use Command-Line Arguments
```python
import sys

# Check if enough arguments
if len(sys.argv) != 4:
    print("Usage: python encrypt.py input.txt output.txt distance")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]
distance = int(sys.argv[3])
```

### 3. Use 'with' for File Operations
```python
# Good - automatically closes file
with open('file.txt', 'r') as f:
    content = f.read()

# Bad - have to remember to close
f = open('file.txt', 'r')
content = f.read()
f.close()  # Easy to forget!
```

### 4. Read Entire File at Once
```python
# Read all content (including newlines)
with open(input_file, 'r') as f:
    text = f.read()  # Reads everything

# Encrypt the whole text (including \n)
encrypted = caesar_encrypt(text, distance)

# Write everything back
with open(output_file, 'w') as f:
    f.write(encrypted)
```

### 5. Test Symmetry
```bash
# Original → Encrypt → Decrypt → Should match original
python encrypt.py original.txt encrypted.txt 7
python decrypt.py encrypted.txt restored.txt 7
diff original.txt restored.txt  # Should be identical
```

---

## 🧪 Test Your Code

**From command line:**
```bash
# Create test file
echo "Test message" > input.txt

# Test encryption
python encrypt.py input.txt output.txt 5
cat output.txt

# Test decryption
python decrypt.py output.txt restored.txt 5
cat restored.txt  # Should match original
```

**Using grader:**
```bash
cd student/
python ../../tools/grade.py
```

---

## 📚 Key Concepts

This exercise practices:
- File I/O (`open()`, `read()`, `write()`)
- Command-line arguments (`sys.argv`)
- Context managers (`with` statement)
- Code reuse (building on ex01/ex02)
- Text file handling
- Preserving file structure (newlines, etc.)

---

## 🔍 Debugging Tips

**If files aren't created:**
```python
# Check if arguments are correct
print(f"Input: {sys.argv[1]}")
print(f"Output: {sys.argv[2]}")
print(f"Distance: {sys.argv[3]}")
```

**If content is wrong:**
```python
# Debug step by step
print(f"Read {len(text)} characters")
print(f"First 50 chars: {text[:50]}")
print(f"Encrypted first 50: {encrypted[:50]}")
```

**If newlines disappear:**
```python
# DON'T strip newlines
text = f.read()  # Good - keeps \n

# Common mistake:
lines = f.readlines()  # Splits into list - harder to work with
```

---

## 🎓 Real-World Applications

**File encryption is everywhere:**
- Password managers (encrypt password files)
- Disk encryption (encrypt entire drives)
- Secure file transfer (encrypt before sending)
- Backup systems (encrypt before cloud storage)

**Your Caesar file encryptor:**
- Same principle as real encryption
- Shows how files stay encrypted at rest
- Demonstrates key-based decryption
- Foundation for understanding file security
