# Grading Rubric: Chapter 6, Exercise 4
## Enhanced Grammar Checker 📝

---

## 📋 What You're Building

Modify grammar checker to recognize:
1. Verb phrase without prepositional phrase
2. Adjectives modifying nouns
3. Sentences with conjunctions (two clauses)

**Examples:**
```
"The boy saw the girl" → Ok
"The girl hit the red ball with a bat" → Ok
"The boy saw the girl and the girl hit the red ball" → Ok
```

---

## 🎯 Point Breakdown (100 Total)

| Category | Points |
|----------|--------|
| **No Prep Phrase** | 30 |
| **Adjectives** | 30 |
| **Conjunctions** | 30 |
| **Base Grammar** | 10 |

---

## 💻 Key Modifications

```python
# Add new vocabulary
adjectives = ["RED", "LITTLE", "BIG"]
conjunctions = ["AND", "OR", "BUT"]

# Make prepositional phrase optional
def verbPhrase():
    phrase = random.choice(verbs) + " " + nounPhrase()
    # Optional prepositional phrase
    if random.choice([True, False]):
        phrase += " " + prepositionalPhrase()
    return phrase

# Add optional adjective to noun phrase
def nounPhrase():
    phrase = random.choice(articles)
    # Optional adjective
    if random.choice([True, False]):
        phrase += " " + random.choice(adjectives)
    phrase += " " + random.choice(nouns)
    return phrase

# Optional conjunction with second clause
def sentence():
    s = nounPhrase() + " " + verbPhrase()
    # Optional conjunction
    if random.choice([True, False]):
        s += " " + random.choice(conjunctions) + " "
        s += nounPhrase() + " " + verbPhrase()
    return s
```

---

## Key Concepts

- Optional grammar elements
- Recursive sentence structure
- Grammar validation
- Pattern recognition
