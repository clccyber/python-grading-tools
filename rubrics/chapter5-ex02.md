# Grading Rubric: Chapter 5, Exercise 2
## File Navigator 📂

---

## 📋 What You're Building

Interactive program to navigate lines in a text file:
- Prompt for filename
- Load lines into a list
- Display number of lines
- Let user enter line numbers to view
- Enter 0 to quit

**Example:**
```
Enter the input file name: text.txt
The file has 5 lines.
Enter a line number [0 to quit]: 2
2 :  Bob
Enter a line number [0 to quit]: 4
4 :  Alice
Enter a line number [0 to quit]: 0
```

---

## 🎯 Point Breakdown (100 Total)

| Category | Points |
|----------|--------|
| **File Reading** | 20 |
| **Line Display** | 30 |
| **Loop Logic** | 30 |
| **Format & Prompts** | 20 |

---

## 💻 Code Pattern

```python
# Get filename
filename = input("Enter the input file name: ")

# Read all lines into list
with open(filename, 'r') as f:
    lines = f.readlines()

# Display count
print(f"The file has {len(lines)} lines.")

# Navigate loop
while True:
    line_num = int(input("Enter a line number [0 to quit]: "))
    
    if line_num == 0:
        break
    
    # Display line (1-indexed)
    if 1 <= line_num <= len(lines):
        print(f"{line_num} : {lines[line_num - 1]}", end='')
    else:
        print("Invalid line number")
```

---

## ✅ Expected Behavior

- Line numbers start at 1 (not 0)
- Display format: `{number} : {line content}`
- Keep prompting until user enters 0
- Handle invalid line numbers gracefully

---

## ❌ Common Mistakes

- Off-by-one error (0-indexed list vs 1-indexed display)
- Not stripping newlines (double spacing)
- Doesn't loop (only one lookup)
- Crashes on invalid input

---

## Key Concepts

- File I/O with `readlines()`
- Lists for storage
- While loops
- Input validation
- 1-based vs 0-based indexing
