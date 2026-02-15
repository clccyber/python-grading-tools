# Grading Rubric: Chapter 4, Exercise 9
## Number Lines in File 🔢

---

## 📋 What You're Building

Add line numbers to a text file:
- Prompt for input and output filenames
- Read input file line by line
- Write each line with right-justified line number
- Format: `   1> line text` (4 columns, right-justified)

---

## 🎯 Point Breakdown (100 Total)

| Category | Points |
|----------|--------|
| **Correct Numbering** | 60 |
| **Format (Right-Justify)** | 20 |
| **File Creation** | 20 |

---

## 💻 Code Pattern

```python
input_name = input("Enter the input file name: ")
output_name = input("Enter the output file name: ")

with open(input_name, 'r') as infile:
    lines = infile.readlines()

with open(output_name, 'w') as outfile:
    for line_num, line in enumerate(lines, 1):
        # Right-justify line number in 4 spaces
        outfile.write(f"{line_num:>4}> {line}")
```

---

## ✅ Expected Format

```
   1> This is line one
   2> This is line two
  10> This is line ten
 100> This is line one hundred
```

**Key formatting rules:**
- Line numbers right-justified in 4 columns
- `>` after the number
- Space after `>`
- Then the original line content

---

## ❌ Common Mistakes

| Mistake | Points Lost |
|---------|-------------|
| Wrong line numbers | -60 |
| Not right-justified | -20 |
| Missing `>` separator | -20 |
| Wrong number of spaces | -20 |
| Line numbers start at 0 | -60 |

---

## 💡 Tips for Success

### 1. Use enumerate() for Line Numbers
```python
for line_num, line in enumerate(lines, 1):  # Start at 1
    # line_num is 1, 2, 3, ...
```

### 2. Right-Justify with Format Strings
```python
# Right-justify in 4 columns:
line_num = 5
formatted = f"{line_num:>4}>"  # "   5>"

line_num = 100
formatted = f"{line_num:>4}>"  # " 100>"
```

### 3. Preserve Original Line Content
```python
# Don't strip newlines!
for line in lines:
    # 'line' already has \n at end
    outfile.write(f"{num:>4}> {line}")
```

### 4. Test Edge Cases
```python
# Single line file
# 10 lines (two digits)
# 100 lines (three digits)
# 1000 lines (four digits - right at limit)
```

---

## 🧪 Test Your Code

```bash
# Create test file
cat > input.txt << 'END'
First line
Second line
Third line
END

# Run program
python numberlines.py
# Enter: input.txt
# Enter: numbered.txt

# Check format
cat numbered.txt
#    1> First line
#    2> Second line
#    3> Third line
```

---

## 🔍 Format String Reference

```python
# Right-justify examples:
f"{5:>4}"    # "   5"
f"{50:>4}"   # "  50"
f"{500:>4}"  # " 500"
f"{5000:>4}" # "5000"

# Full format for this exercise:
f"{line_num:>4}> {line}"
```

---

## Key Concepts

- File I/O (reading and writing)
- String formatting (`:>4` for right-justify)
- `enumerate()` for line numbering
- Preserving line structure
- Text processing line-by-line
