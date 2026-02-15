# Grading Rubric: Chapter 3, Exercise 10
## Credit Plan Payment Schedule 💳

---

## 📋 What You're Building

A program for TidBit Computer Store that displays a payment schedule for a purchase on credit:
- 10% down payment
- 12% annual interest rate (1% per month)
- Monthly payment = 5% of purchase price
- Table showing each month until paid off

**Key concept:** Using loops with stateful calculations (each month depends on previous month's balance).

---

## 🎯 Point Breakdown (100 Total)

| Category | Points | What's Graded |
|----------|--------|---------------|
| **Row Values** | 60 | All calculations (balance, interest, principal, payment) correct |
| **Formatting** | 20 | All money values displayed with exactly 2 decimal places |
| **Table Structure** | 10 | Column headers present |

**Note:** Each row has 6 values to check - points divided across all cells.

---

## 📐 The Formulas

**Initial values:**
```python
down_payment = purchase_price * 0.10
starting_balance = purchase_price - down_payment
monthly_payment = purchase_price * 0.05
monthly_rate = 0.12 / 12  # 12% annual = 1% per month
```

**For each month:**
```python
interest = balance * monthly_rate
principal = monthly_payment - interest
ending_balance = balance - principal
```

**Example (Month 1 of $200 purchase):**
```
Starting balance: 180.00 (200 - 20 down)
Interest: 180 * 0.01 = 1.80
Principal: 10 - 1.80 = 8.20
Payment: 10.00
Ending: 180 - 8.20 = 170.00
```

---

## ✅ Expected Output Format

Your program should:
- Prompt for purchase price
- Display table with column headers
- Show each month until balance reaches $0
- Each row: month, starting balance, interest, principal, payment, ending balance

**Example:**
```
Enter the purchase price: 200
Month  Starting Balance  Interest to Pay  Principal to Pay  Payment  Ending Balance
 1         180.00           1.80             8.20            10.00           170.00
 2         170.00           1.70             8.30            10.00           160.00
 3         160.00           1.60             8.40            10.00           150.00
...
18          10.00           0.10             9.90            10.00             0.00
```

---

## 📊 How Grading Works

The grader checks **each cell** in the table:

✓ **Month number** - Correct sequence  
✓ **Starting balance** - Matches previous month's ending  
✓ **Interest** - Correct calculation (balance × 0.01)  
✓ **Principal** - Correct (payment - interest)  
✓ **Payment** - Constant (5% of purchase)  
✓ **Ending balance** - Correct (starting - principal)  
✓ **2 decimals** - All money values formatted as XX.XX  

**Partial credit:** Points per cell, so correct values in early rows earn points even if later rows are wrong.

---

## ❌ Common Mistakes

| Mistake | Points Lost | Why |
|---------|-------------|-----|
| Using annual rate instead of monthly | -60 | Interest = balance × (0.12/12), not × 0.12 |
| Not updating balance each month | -60 | Next month uses previous ending balance |
| Wrong principal calculation | Up to -60 | principal = payment - interest |
| Fixed number of months | Variable | Loop should continue until balance = 0 |
| Not 2 decimals | Up to -20 | All money needs .XX format |
| Missing headers | -10 | Table needs column names |

---

## 💡 Tips for Success

1. **Monthly rate is annual/12**: 12% per year = 1% per month = 0.01
2. **Balance updates each iteration**: ending becomes next starting
3. **Loop until balance ≤ 0**: Don't hardcode 18 months
4. **Principal = payment - interest**: NOT balance × something
5. **Format ALL money with 2 decimals**: Every column except month

### Code Pattern:
```python
purchase = float(input("Enter purchase price: "))

down = purchase * 0.10
balance = purchase - down
payment = purchase * 0.05
rate = 0.12 / 12

print("Month  Starting Balance  Interest to Pay  Principal to Pay  Payment  Ending Balance")

month = 1
while balance > 0:
    interest = balance * rate
    principal = payment - interest
    ending = balance - principal
    
    print(f"{month:2d}    {balance:10.2f}       {interest:8.2f}         {principal:8.2f}        {payment:7.2f}       {ending:10.2f}")
    
    balance = ending
    month += 1
```

### Common Logic Errors:
```python
# Wrong - using annual rate
interest = balance * 0.12  # Should be 0.12/12

# Wrong - not updating balance
for month in range(18):
    interest = balance * rate  # balance never changes!

# Wrong - principal calculation
principal = balance * rate  # Should be payment - interest

# Wrong - hardcoded months
for month in range(1, 19):  # Should loop until balance = 0
```

---

## 🧪 Test Your Code

From the `student/` directory:
```bash
../../tools/grade.sh
```

Check your report in `../report_ex10/report.txt`

**Verify with example ($200 purchase):**
- Month 1: Starting $180, Interest $1.80, Principal $8.20, Ending $170
- Month 18: Starting $10, Interest $0.10, Principal $9.90, Ending $0
- Should take exactly 18 months

---

## 📚 Key Concepts

This exercise practices:
- `while` loops (continue until condition met)
- Stateful calculations (each iteration uses previous result)
- Multiple variables updated each iteration
- Money formatting for all values
- Table output with multiple columns
- Annual vs. monthly rates (division by 12)
- Stopping condition (balance reaches 0)
