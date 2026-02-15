# Grading Rubrics: Chapter 8, Exercises 5-10
## PIL Image Processing 🖼️

---

## Exercise 5: Posterize

### What You're Building
Convert image to two-tone using RGB threshold

### Points (100 Total)
- Function signature correct (20 pts)
- Threshold logic (50 pts)
- RGB tuple parameter (20 pts)
- Visual result (10 pts)

### Algorithm
```python
def posterize(image, rgb_tuple):
    """Convert to black or target color"""
    r_target, g_target, b_target = rgb_tuple
    
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            r, g, b = image.getPixel(x, y)
            
            # Average brightness
            avg = (r + g + b) // 3
            
            if avg < 128:
                image.setPixel(x, y, (0, 0, 0))  # Black
            else:
                image.setPixel(x, y, rgb_tuple)  # Target color
```

---

## Exercise 6: Grayscale

### What You're Building
Convert color image to grayscale using average method

### Points (100 Total)
- Function exists (20 pts)
- All pixels R=G=B (60 pts)
- Correct formula (20 pts)

### Algorithm
```python
def grayscale(image):
    """Convert to grayscale by averaging RGB"""
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            r, g, b = image.getPixel(x, y)
            
            # Average the RGB values
            gray = (r + g + b) // 3
            
            image.setPixel(x, y, (gray, gray, gray))
```

**Note:** This is the "crude" method. Proper method uses weighted average:
`gray = int(0.299*r + 0.587*g + 0.114*b)`

---

## Exercise 7: Invert

### What You're Building
Create photographic negative (255 - RGB)

### Points (100 Total)
- Function exists (20 pts)
- Correct inversion (60 pts)
- Works on color/gray/BW (20 pts)

### Algorithm
```python
def invert(image):
    """Invert image colors"""
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            r, g, b = image.getPixel(x, y)
            
            # Invert each component
            image.setPixel(x, y, (255 - r, 255 - g, 255 - b))
```

---

## Exercise 8: Sepia Tone

### What You're Building
Old-fashioned photo effect (brown/gray tones)

### Points (100 Total)
- Calls grayscale first (20 pts)
- Red adjustment (30 pts)
- Blue adjustment (30 pts)
- Green unchanged (20 pts)

### Algorithm
```python
def sepia(image):
    """Convert to sepia tone"""
    # First convert to grayscale
    grayscale(image)
    
    # Then adjust for sepia
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            r, g, b = image.getPixel(x, y)
            
            if r < 63:
                r = int(r * 1.1)
                b = int(b * 0.9)
            elif r < 192:
                r = int(r * 1.15)
                b = int(b * 0.85)
            else:
                r = min(int(r * 1.08), 255)
                b = int(b * 0.93)
            
            image.setPixel(x, y, (r, g, b))
```

---

## Exercise 9: Lighten/Darken/Color Filter

### What You're Building
Three related functions for color adjustment

### Points (100 Total)
- lighten() function (30 pts)
- darken() function (30 pts)
- colorFilter() function (30 pts)
- Bounds checking (10 pts)

### Algorithms
```python
def lighten(image, amount):
    """Increase all RGB by amount"""
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            r, g, b = image.getPixel(x, y)
            
            # Add amount, but don't exceed 255
            r = min(r + amount, 255)
            g = min(g + amount, 255)
            b = min(b + amount, 255)
            
            image.setPixel(x, y, (r, g, b))

def darken(image, amount):
    """Decrease all RGB by amount"""
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            r, g, b = image.getPixel(x, y)
            
            # Subtract amount, but don't go below 0
            r = max(r - amount, 0)
            g = max(g - amount, 0)
            b = max(b - amount, 0)
            
            image.setPixel(x, y, (r, g, b))

def colorFilter(image, rgb_tuple):
    """Adjust RGB by tuple amounts"""
    r_adj, g_adj, b_adj = rgb_tuple
    
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            r, g, b = image.getPixel(x, y)
            
            # Apply adjustments with bounds checking
            r = max(0, min(r + r_adj, 255))
            g = max(0, min(g + g_adj, 255))
            b = max(0, min(b + b_adj, 255))
            
            image.setPixel(x, y, (r, g, b))
```

---

## Exercise 10: Sharpen (Edge Detection)

### What You're Building
Sharpen image by darkening edges

### Points (100 Total)
- Edge detection logic (40 pts)
- Degree parameter (20 pts)
- Threshold parameter (20 pts)
- Visual result (20 pts)

### Concept
```python
def sharpen(image, degree, threshold):
    """Sharpen by darkening edges"""
    # For each pixel, compare to neighbors
    # If difference > threshold, darken by degree
    # This emphasizes edges while keeping colors
```

**Note:** This is advanced - focus on edge detection concept

---

## Automated Grading

**Exercises 5-7 have automated graders:**
- Tests function exists
- Validates pixel transformations
- Samples 100 random pixels

**Exercises 8-10:**
- Function testing only
- Manual verification recommended

---

## Key Concepts (All PIL Exercises)

- Pixel manipulation
- RGB color model
- Image processing algorithms
- Raster graphics vs vector
- Loop optimization (nested loops)
- Bounds checking (0-255)
- PIL/Pillow library usage

---

## Testing Tips

```python
# Load and test
from PIL import Image
img = Image.open('smokey.gif')

# Run function
grayscale(img)

# Save result
img.save('output.gif')

# Visual check
img.show()
```

---

## Common Mistakes

- Forgetting bounds check (RGB must be 0-255)
- Not copying image (modifying original)
- Wrong loop order (x/y vs y/x)
- Integer division issues (`//` vs `/`)
- Not converting float to int
