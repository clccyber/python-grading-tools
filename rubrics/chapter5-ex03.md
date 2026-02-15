# Grading Rubric: Chapter 5, Exercise 3
## Sentence Generator with File Input 📝

---

## 📋 What You're Building

Modify sentence generator to read vocabulary from text files:
- Read nouns from `nouns.txt`
- Read verbs from `verbs.txt`
- Read articles from `articles.txt`
- Read prepositions from `prepositions.txt`
- Generate N random sentences

**Example:**
```
Enter the number of sentences: 2
A BAT LIKED A GIRL BY A BALL
A BOY SAW THE BAT WITH THE GIRL
```

---

## 🎯 Point Breakdown (100 Total)

| Category | Points |
|----------|--------|
| **File Reading** | 30 |
| **Sentence Structure** | 40 |
| **Random Selection** | 20 |
| **Output Format** | 10 |

---

## 💻 Key Function

```python
def getWords(filename):
    """Read words from file, return as tuple"""
    with open(filename, 'r') as f:
        words = []
        for line in f:
            word = line.strip()
            if word:  # Skip empty lines
                words.append(word)
        return tuple(words)

# Initialize vocabulary
nouns = getWords("nouns.txt")
verbs = getWords("verbs.txt")
articles = getWords("articles.txt")
prepositions = getWords("prepositions.txt")
```

---

## 📐 Sentence Structure

```
Article + Noun + Verb + Article + Noun + Prep + Article + Noun
   THE  +  BOY + SAW  +   A   + BALL +  BY  +  THE  + GIRL
```

---

## ✅ Expected Behavior

- Reads 4 vocabulary files
- Generates requested number of sentences
- Each sentence follows proper grammar structure
- Random word selection (output varies each run)
- Uppercase words recommended

---

## ❌ Common Mistakes

- Hardcoded vocabulary (doesn't read files)
- Wrong file reading (doesn't strip newlines)
- Returns list instead of tuple
- Missing getWords() function
- Doesn't handle N sentences

---

## Key Concepts

- File I/O for data loading
- Function design (getWords)
- Tuples vs lists
- Random selection (`random.choice()`)
- String formatting
