# Grading Rubric: Chapter 4, Exercise 5a
## Shift Bits Left ⬅️

---

## 📋 What You're Building

Shift a bit string one position to the left with wrap-around:
- Prompt for a bit string
- Move all bits left by one position
- Leftmost bit wraps to rightmost position
- Display result

**Example:**
```
Enter a string of bits: 0001
0010
```

---

## 🎯 Point Breakdown (100 Total)

| Category | Points |
|----------|--------|
| **Correct Shift** | 80 |
| **Output Format** | 20 |

---

## 📐 Shift Logic

**Shift left = take first char, move it to end:**

```python
def shift_left(bits):
    # Take everything except first char, add first char at end
    return bits[1:] + bits[0]
```

**Visual:**
```
0001 → 0010  (0 moves to end, 001 shifts left)
1000 → 0001  (1 wraps around to end)
1011 → 0111  (1 wraps to end)
```

---

## ✅ Expected Behavior

| Input | Output |
|-------|--------|
| 0001 | 0010 |
| 1000 | 0001 |
| 1011 | 0111 |
| 1111 | 1111 |
| 1010 | 0101 |

---

## 💡 Code Pattern

```python
bits = input("Enter a string of bits: ")

# Shift left: remove first, add to end
shifted = bits[1:] + bits[0]

print(shifted)
```

---

## Key Concepts

- String slicing (`[1:]`)
- String concatenation
- Circular shift / rotation
- Bit manipulation concepts
