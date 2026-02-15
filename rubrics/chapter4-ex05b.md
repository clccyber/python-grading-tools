# Grading Rubric: Chapter 4, Exercise 5b
## Shift Bits Right ➡️

---

## 📋 What You're Building

Shift a bit string one position to the right with wrap-around:
- Prompt for a bit string
- Move all bits right by one position
- Rightmost bit wraps to leftmost position
- Display result

**Example:**
```
Enter a string of bits: 0010
0001
```

---

## 🎯 Point Breakdown (100 Total)

| Category | Points |
|----------|--------|
| **Correct Shift** | 80 |
| **Output Format** | 20 |

---

## 📐 Shift Logic

**Shift right = take last char, move it to beginning:**

```python
def shift_right(bits):
    # Take last char, add everything except last
    return bits[-1] + bits[:-1]
```

**Visual:**
```
0010 → 0001  (0 moves to front, 001 shifts right)
0001 → 1000  (1 wraps around to front)
0111 → 1011  (1 wraps to front)
```

---

## ✅ Expected Behavior

| Input | Output |
|-------|--------|
| 0010 | 0001 |
| 0001 | 1000 |
| 0111 | 1011 |
| 1111 | 1111 |
| 0101 | 1010 |

---

## 💡 Code Pattern

```python
bits = input("Enter a string of bits: ")

# Shift right: take last, add to beginning
shifted = bits[-1] + bits[:-1]

print(shifted)
```

---

## Key Concepts

- String slicing (`[-1]`, `[:-1]`)
- String concatenation
- Circular shift / rotation
- Inverse operation of shift left
