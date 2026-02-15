# Grading Rubric: Chapter 5, Exercise 8
## Word Concordance (Frequencies) 📊

---

## 📋 What You're Building

File concordance - track unique words and their frequencies:
- Prompt for filename
- Count each word's frequency
- Sort alphabetically
- Display word and count

**Example:**
```
Enter the input file name: text.txt
apple 3
banana 3
cherry 3
date 2
elderberry 2
```

---

## 🎯 Point Breakdown (100 Total)

| Category | Points |
|----------|--------|
| **File Reading** | 20 |
| **Frequency Counting** | 40 |
| **Sorting** | 20 |
| **Output Format** | 20 |

---

## 💻 Implementation

```python
filename = input("Enter the input file name: ")

# Read and count
with open(filename, 'r') as f:
    text = f.read()
    words = text.split()

# Count frequencies
frequency = {}
for word in words:
    frequency[word] = frequency.get(word, 0) + 1

# Sort by word (alphabetically)
for word in sorted(frequency.keys()):
    print(f"{word} {frequency[word]}")
```

---

## ✅ Expected Output Format

```
word1 count1
word2 count2
word3 count3
```

Space-separated, alphabetical order by word.

---

## Key Concepts

- Dictionaries for counting
- `.get()` method with default
- Sorting dictionary keys
- File processing
- Frequency analysis
