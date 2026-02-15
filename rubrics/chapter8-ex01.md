# Grading Rubric: Chapter 8, Exercise 1
## Draw Circle with Turtle 🐢

---

## 📋 What You're Building

Function that draws a circle using turtle graphics:
- `drawCircle(turtle, x, y, radius)`
- Algorithm: Turn 3° and move 120 times
- Distance = 2π × radius / 120

**Example output:** Circle drawing

---

## 🎯 Point Breakdown (100 Total)

| Category | Points |
|----------|--------|
| **Function Exists** | 20 |
| **Correct Parameters** | 20 |
| **Circle Algorithm** | 40 |
| **Visual Result** | 20 |

---

## 💻 Implementation

```python
import turtle
import math

def drawCircle(t, x, y, radius):
    """Draw circle at (x,y) with given radius"""
    t.penup()
    t.goto(x, y - radius)  # Start at bottom of circle
    t.pendown()
    
    # Calculate distance to move each step
    distance = 2.0 * math.pi * radius / 120.0
    
    # Draw circle by turning 3° and moving 120 times
    for _ in range(120):
        t.forward(distance)
        t.left(3)
```

---

## Key Concepts

- Turtle graphics basics
- Approximating curves with line segments
- Circle geometry (circumference formula)
- Vector graphics vs raster
