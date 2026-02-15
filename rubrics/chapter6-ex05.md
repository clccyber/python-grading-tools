# Grading Rubric: Chapter 6, Exercise 5
## Command Interpreter Menu 🖥️

---

## 📋 What You're Building

Text-based menu system with four functions:
- `printMenu(menu)` - Display numbered options
- `acceptCommand(menuLength)` - Get valid input
- `performCommand(number, menu)` - Execute command
- `main()` - Loop until Quit

**Example:**
```
1 Open
2 Save
3 Compile
4 Run
5 Quit
Enter a number: 2
Command = Save
```

---

## 🎯 Point Breakdown (100 Total)

| Category | Points |
|----------|--------|
| **printMenu()** | 25 |
| **acceptCommand()** | 25 |
| **performCommand()** | 25 |
| **main() Loop** | 25 |

---

## 💻 Implementation Pattern

```python
def printMenu(menu):
    """Display menu with numbers"""
    for i, option in enumerate(menu, 1):
        print(f"{i} {option}")

def acceptCommand(menuLength):
    """Get valid menu choice"""
    while True:
        try:
            choice = int(input("Enter a number: "))
            if 1 <= choice <= menuLength:
                return choice
            else:
                print("Error: invalid choice")
        except ValueError:
            print("Error: must enter a number")

def performCommand(number, menu):
    """Execute selected command"""
    print(f"Command = {menu[number - 1]}")

def main():
    menu = ["Open", "Save", "Compile", "Run", "Quit"]
    while True:
        printMenu(menu)
        choice = acceptCommand(len(menu))
        performCommand(choice, menu)
        if menu[choice - 1] == "Quit":
            break
```

---

## Key Concepts

- Menu-driven programs
- Input validation loops
- Function decomposition
- Error handling
