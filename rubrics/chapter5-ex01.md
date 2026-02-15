# Grading Rubric: Chapter 5, Exercise 1
## Statistics Functions 📊

---

## 📋 What You're Building

Create a statistics module (`stats.py`) with three functions:
- **mean()** - Calculate average
- **median()** - Find middle value
- **mode()** - Find most frequent value
- Each function takes a list, returns a number
- Return 0 for empty lists

**Example Output:**
```
List: [8, 2, 5, 3, 9, 6, 2, 7]
Mode: 2
Median: 5.5
Mean: 5.25
```

---

## 🎯 Point Breakdown (100 Total)

| Category | Points | What's Graded |
|----------|--------|---------------|
| **Mean Function** | 25 | Correctly calculates average |
| **Median Function** | 30 | Handles odd/even length lists |
| **Mode Function** | 30 | Finds most frequent value |
| **Edge Cases** | 15 | Empty list returns 0, handles ties |

---

## 📐 Algorithm Details

### Mean (Average)
```python
def mean(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)
```

### Median (Middle Value)
```python
def median(numbers):
    if len(numbers) == 0:
        return 0
    
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    
    if n % 2 == 1:
        # Odd length - return middle
        return sorted_nums[n // 2]
    else:
        # Even length - return average of two middle values
        mid1 = sorted_nums[n // 2 - 1]
        mid2 = sorted_nums[n // 2]
        return (mid1 + mid2) / 2
```

### Mode (Most Frequent)
```python
def mode(numbers):
    if len(numbers) == 0:
        return 0
    
    # Count frequencies
    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1
    
    # Find most frequent
    max_count = max(frequency.values())
    
    # Return first value with max frequency
    for num, count in frequency.items():
        if count == max_count:
            return num
```

---

## ✅ Test Cases

**Example from instructions:**
```python
numbers = [8, 2, 5, 3, 9, 6, 2, 7]
print(f"Mean: {mean(numbers)}")     # 5.25
print(f"Median: {median(numbers)}") # 5.5
print(f"Mode: {mode(numbers)}")     # 2
```

**Edge cases:**
```python
# Empty list
assert mean([]) == 0
assert median([]) == 0
assert mode([]) == 0

# Single element
assert mean([5]) == 5
assert median([5]) == 5
assert mode([5]) == 5

# All same
assert mode([3, 3, 3, 3]) == 3

# No clear mode (tie)
# [1, 2, 3] - each appears once
# Return any of them (typically first found)
```

---

## 💡 Tips for Success

### 1. Module Structure
```python
# stats.py

def mean(numbers):
    """Calculate average of numbers in list"""
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

def median(numbers):
    """Find middle value"""
    # implementation

def mode(numbers):
    """Find most frequent value"""
    # implementation

def main():
    """Test the functions"""
    data = [8, 2, 5, 3, 9, 6, 2, 7]
    print(f"List: {data}")
    print(f"Mode: {mode(data)}")
    print(f"Median: {median(data)}")
    print(f"Mean: {mean(data)}")

if __name__ == '__main__':
    main()
```

### 2. Median - Handle Even vs Odd
```python
# Odd length [1, 2, 3] → median is 2 (index 1)
# Even length [1, 2, 3, 4] → median is (2+3)/2 = 2.5
```

### 3. Mode - Use Dictionary for Counting
```python
# Count frequencies
freq = {}
for num in [2, 5, 2, 3, 5, 2]:
    freq[num] = freq.get(num, 0) + 1
# freq = {2: 3, 5: 2, 3: 1}
# Mode is 2 (appears 3 times)
```

---

## ❌ Common Mistakes

| Mistake | Points Lost | Why |
|---------|-------------|-----|
| Doesn't handle empty list | -15 | Must return 0 for empty |
| Median doesn't sort | -30 | Must sort before finding middle |
| Mean uses integer division | -15 | Use `/` not `//` |
| Mode doesn't count properly | -30 | Need frequency dictionary |
| No main function | -10 | Instructions require it |

---

## 🧪 Manual Testing

```bash
python stats.py
# Should output:
# List: [8, 2, 5, 3, 9, 6, 2, 7]
# Mode: 2
# Median: 5.5
# Mean: 5.25
```

**Test with different lists:**
```python
# Test in Python interpreter
import stats

# All same
print(stats.mode([5, 5, 5]))  # 5

# Sorted vs unsorted
print(stats.median([1, 3, 2]))  # 2 (not 3!)

# Empty
print(stats.mean([]))  # 0
```

---

## 📚 Key Concepts

This exercise practices:
- Function definitions
- List processing
- Dictionary for counting (mode)
- Sorting (median)
- Edge case handling
- Module organization with `main()`
- Statistical algorithms

---

## 🎓 Understanding the Statistics

**Mean** - Average value, affected by outliers  
**Median** - Middle value, resistant to outliers  
**Mode** - Most common value, useful for categorical data  

**Example where they differ:**
```
Data: [1, 2, 2, 3, 100]
Mean: 21.6 (pulled up by 100)
Median: 2 (middle value)
Mode: 2 (appears twice)
```
