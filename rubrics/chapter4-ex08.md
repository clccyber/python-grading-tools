# Grading Rubric: Chapter 4, Exercise 8
## Copy File 📋

---

## 📋 What You're Building

Copy contents from one file to another:
- Prompt for input filename
- Prompt for output filename  
- Read all content from input file
- Write it to output file

---

## 🎯 Point Breakdown (100 Total)

| Category | Points |
|----------|--------|
| **File Correctness** | 80 |
| **File Creation** | 20 |

---

## 💻 Code Pattern

```python
# Get filenames from user
input_name = input("Enter the input file name: ")
output_name = input("Enter the output file name: ")

# Read input file
with open(input_name, 'r') as infile:
    content = infile.read()

# Write to output file
with open(output_name, 'w') as outfile:
    outfile.write(content)
```

---

## ✅ Test Your Code

```bash
# Create test file
echo "Hello World" > test.txt

# Run your program
python copyfile.py
# Enter: test.txt
# Enter: copy.txt

# Verify
cat copy.txt  # Should match test.txt
```

---

## ❌ Common Mistakes

- Not creating output file (-80)
- Missing content (-80)
- Extra/missing lines (-40)
- Not closing files properly (-20)

---

## 💡 Tips

1. Use `read()` not `readlines()` (preserves formatting)
2. Use `with` statement (auto-closes files)
3. Test with multi-line files
4. Output should be EXACT copy

---

## Key Concepts

- File reading (`open`, `read`)
- File writing (`write`)
- Context managers (`with`)
- Text file handling
