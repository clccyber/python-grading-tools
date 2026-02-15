# Grading Rubric: Chapter 5, Exercise 7
## Unique Words from File 📝

---

## 📋 What You're Building

Program that finds unique words in a text file:
- Prompt for filename
- Read all words
- Remove duplicates
- Sort alphabetically
- Print one word per line

**Example:**
```
Enter the input file name: text.txt
apple
banana
cherry
date
elderberry
```

---

## 🎯 Point Breakdown (100 Total)

| Category | Points |
|----------|--------|
| **File Reading** | 20 |
| **Duplicate Removal** | 40 |
| **Sorting** | 20 |
| **Output Format** | 20 |

---

## 💻 Implementation

```python
filename = input("Enter the input file name: ")

# Read all words
with open(filename, 'r') as f:
    text = f.read()
    words = text.split()

# Get unique words using set
unique_words = set(words)

# Sort alphabetically
sorted_words = sorted(unique_words)

# Print one per line
for word in sorted_words:
    print(word)
```

---

## ✅ Expected Behavior

- Case-sensitive (unless specified otherwise)
- Alphabetical order
- No duplicates
- One word per line

---

## Key Concepts

- Sets for uniqueness
- File reading
- `sorted()` function
- String splitting
