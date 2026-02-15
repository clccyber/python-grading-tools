# Grading Rubrics: Chapter 8, Exercises 2-4
## Turtle Graphics (Fractals & Patterns)

---

## Exercise 2: C-Curve with Random Colors

### What You're Building
Modify c-curve to use random colors for line segments

### Points (100 Total)
- Random color generation (40 pts)
- C-curve algorithm (40 pts)
- Visual result (20 pts)

### Key Code
```python
import turtle, random

def cCurve(t, x1, y1, x2, y2, level):
    def getMidpoint(x1, y1, x2, y2):
        # Calculate perpendicular midpoint
        ...
    
    # Random color for each segment
    t.pencolor(random.random(), random.random(), random.random())
    
    if level == 0:
        t.goto(x2, y2)
    else:
        # Recursive calls
        ...
```

---

## Exercise 3: Koch Snowflake

### What You're Building
Recursive fractal - equilateral triangle with fractal edges

### Points (100 Total)
- drawFractalLine function (50 pts)
- Recursive logic (30 pts)
- Three sides at correct angles (20 pts)

### Key Algorithm
```python
def drawFractalLine(t, distance, angle, level):
    if level == 0:
        t.forward(distance)
    else:
        # Four recursive calls at 1/3 distance
        drawFractalLine(t, distance/3, angle, level-1)
        t.left(60)
        drawFractalLine(t, distance/3, angle+60, level-1)
        t.right(120)
        drawFractalLine(t, distance/3, angle-60, level-1)
        t.left(60)
        drawFractalLine(t, distance/3, angle, level-1)
```

---

## Exercise 4: Mondrian Patterns

### What You're Building
Recursive rectangle subdivision in random colors

### Points (100 Total)
- Recursive subdivision (40 pts)
- Random colors (20 pts)
- Alternating H/V splits (20 pts)
- Stopping condition (20 pts)

### Key Pattern
```python
def mondrian(t, x, y, width, height, level):
    if level == 0:
        # Fill rectangle with random color
        drawRectangle(t, x, y, width, height, randomColor())
    else:
        # Split 1/3 and 2/3
        # Alternate horizontal and vertical
        ...
```

---

## Grading Note

**These are visual/creative assignments:**
- Check that pattern/algorithm is present
- Verify recursion works
- Visual appearance may vary (that's OK!)
- Focus on understanding fractals and recursion

---

## Key Concepts (All Three)

- Recursion
- Fractal geometry
- Base cases and recursive cases
- Vector graphics
- SVG concepts (resolution-independent)
