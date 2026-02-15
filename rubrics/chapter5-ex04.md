# Grading Rubric: Chapter 5, Exercise 4
## Enhanced Sentence Generator 🎲

---

## 📋 What You're Building

Add optional parts to sentence generator:
1. Prepositional phrase is optional (probability-based)
2. Conjunction + second clause optional
3. Adjectives optional

**Example:**
```
Enter the number of sentences: 2
THE RED BALL LIKED THE RED GIRL AND THE RED BAT LIKED THE LITTLE BAT
THE RED BAT HIT THE GIRL
```

---

## 🎯 Point Breakdown (100 Total)

| Category | Points |
|----------|--------|
| **Optional Prepositional** | 25 |
| **Optional Conjunction** | 25 |
| **Optional Adjectives** | 25 |
| **Grammar Correctness** | 25 |

---

## 💻 Optional Logic

```python
import random

# Optionally add adjective (50% chance)
if random.randint(0, 1) == 1:
    sentence += random.choice(adjectives) + " "

# Optionally add prepositional phrase
if random.randint(0, 1) == 1:
    sentence += random.choice(prepositions) + " "
    sentence += random.choice(articles) + " "
    sentence += random.choice(nouns)

# Optionally add conjunction and second clause
if random.randint(0, 1) == 1:
    sentence += " " + random.choice(conjunctions) + " "
    # ... second independent clause
```

---

## ✅ Expected Features

- Sentences vary in length
- Some have adjectives, some don't
- Some have prepositional phrases
- Some have conjunctions with second clause
- All grammatically correct

---

## Key Concepts

- Probability with `random`
- Optional grammar structures
- Building complex strings
- Expanding vocabulary sets
