# Grading Rubric: Chapter 1, Exercise 5
## Cuboid Volume

---

## 📋 What You're Building

Compute the volume of a cuboid (rectangular prism):
- **File:** `cuboid.py`
- **Formula:** `volume = height × width × depth`
- **Concept:** Multiple inputs, simple multiplication

**Example:**
```
Enter the height: 6
Enter the width: 8
Enter the depth: 9
The volume is 432.0 cubic units.
```

---

## 🎯 Point Breakdown (100 Total)

| Category | Points |
|----------|--------|
| **Prompts for Height** | 15 |
| **Prompts for Width** | 15 |
| **Prompts for Depth** | 15 |
| **Correct Calculation** | 35 |
| **Output with Label** | 20 |

---

## 💻 Implementation

```python
# cuboid.py
height = float(input("Enter the height: "))
width = float(input("Enter the width: "))
depth = float(input("Enter the depth: "))
volume = height * width * depth
print("The volume is", volume, "cubic units.")
```

---

## ✅ What to Check

### Input (45 pts)
- ✓ Prompts for height (15 pts)
- ✓ Prompts for width (15 pts)
- ✓ Prompts for depth (15 pts)
- ✓ All converted to float
- ✓ Clear prompts for each

### Calculation (35 pts)
- ✓ Multiplies all three dimensions
- ✓ Correct formula: `height * width * depth`
- ✓ Gets correct answer

### Output (20 pts)
- ✓ Displays calculated volume
- ✓ Includes label (e.g., "The volume is...")
- ✓ Includes "cubic units"

---

## Testing

**Test case 1:**
```
Input: height = 6, width = 8, depth = 9
Expected: 432.0 cubic units
```

**Test case 2:**
```
Input: height = 5, width = 5, depth = 5
Expected: 125.0 cubic units
```

**Test case 3:**
```
Input: height = 2.5, width = 3.0, depth = 4.0
Expected: 30.0 cubic units
```

---

## Common Mistakes

❌ **Only two dimensions:**
```python
volume = height * width  # Forgot depth!
```

❌ **Addition instead of multiplication:**
```python
volume = height + width + depth  # This is perimeter, not volume
```

❌ **Wrong order (doesn't affect result, but shows confusion):**
```python
# All these work, but height/width/depth is clearest:
volume = depth * height * width
volume = width * depth * height
```

❌ **Missing input conversion:**
```python
height = input("Enter the height: ")  # String, not number
```

❌ **Wrong units:**
```python
print("The volume is", volume, "square units.")  # Should be cubic!
```

✅ **Correct:**
```python
print("The volume is", volume, "cubic units.")
```

---

## Alternative Solutions

**All acceptable:**
```python
# Standard approach
volume = height * width * depth

# Parentheses for clarity (not needed)
volume = (height * width * depth)

# Computing directly in print
print("The volume is", height * width * depth, "cubic units.")

# Step by step
base_area = height * width
volume = base_area * depth
```

---

## Key Concepts

- **Multiple inputs** - Collecting several values
- **Three-dimensional geometry** - Volume vs area
- **Associative property** - Order doesn't matter for multiplication
- **Units matter** - Cubic units for volume

---

## Geometry Reminder

**Cuboid (Rectangular Prism):**
- Like a box or brick
- Six rectangular faces
- Three dimensions: height, width, depth
- Volume = product of all three dimensions

**Similar shapes:**
- Cube: height = width = depth
- Box: any rectangular prism
- Room: height × width × length

---

## Notes

- Three separate inputs required
- Formula is straightforward: multiply all three
- Watch for "cubic units" not "square units"
- Good practice handling multiple variables

**Full credit if:** Program correctly multiplies three dimensions and displays result with "cubic units" label.
