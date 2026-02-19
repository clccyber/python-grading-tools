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

----------------------------------

## 📖 Understanding Loan Amortization: A Complete Example

---

### 🎯 Loan Terms (Example: $200 Purchase)

| Term | Calculation | Value |
|------|-------------|-------|
| **Purchase Price** | User input | $200.00 |
| **Down Payment (10%)** | $200 × 0.10 | $20.00 |
| **Amount Financed** | $200 - $20 | $180.00 |
| **Annual Interest Rate** | Fixed | 12% |
| **Monthly Interest Rate** | 12% ÷ 12 | 1% (0.01) |
| **Monthly Payment (5%)** | $200 × 0.05 | $10.00 |

---

### 🔄 How Each Payment Works

Every month, your $10 payment is split into two parts:

1. **Interest**: What the store charges for lending you money
   - Calculated on your *remaining balance*
   - Formula: `balance × 0.01`

2. **Principal**: What actually reduces your debt
   - Formula: `payment - interest`
   - This is why your balance goes down each month

**Key Insight:** Early on, most of your payment goes to interest. Later, most goes to principal!

---

### 📊 Month-by-Month Breakdown

#### **Month 1: Starting Out**
```
Starting Balance: $180.00  (what you owe at the beginning)
Interest Charge:  $  1.80  ($180 × 0.01 = $1.80)
Principal Paid:   $  8.20  ($10.00 - $1.80 = $8.20)
Payment Made:     $ 10.00  (fixed monthly payment)
Ending Balance:   $171.80  ($180 - $8.20 = $171.80)
                           ↑
                    This becomes next month's starting balance
```

**Notice:** Only $8.20 of your $10 payment reduced the debt!

---

#### **Month 2: Building Momentum**
```
Starting Balance: $171.80  (last month's ending)
Interest Charge:  $  1.72  ($171.80 × 0.01 = $1.72)
Principal Paid:   $  8.28  ($10.00 - $1.72 = $8.28)
Payment Made:     $ 10.00
Ending Balance:   $163.52  ($171.80 - $8.28 = $163.52)
```

**Notice:** Interest went down (from $1.80 to $1.72), so principal went up (from $8.20 to $8.28)!

---

#### **Month 9: Halfway Point**
```
Starting Balance: $ 92.13
Interest Charge:  $  0.92  ($92.13 × 0.01 = $0.92)
Principal Paid:   $  9.08  ($10.00 - $0.92 = $9.08)
Payment Made:     $ 10.00
Ending Balance:   $ 83.05  ($92.13 - $9.08 = $83.05)
```

**Notice:** Now most of your payment ($9.08) goes to principal!

---

#### **Month 18: Final Payment**
```
Starting Balance: $ 10.00  (almost done!)
Interest Charge:  $  0.10  ($10.00 × 0.01 = $0.10)
Principal Paid:   $  9.90  ($10.00 - $0.10 = $9.90)
Payment Made:     $ 10.00
Ending Balance:   $  0.00  (PAID OFF! 🎉)
```

**Notice:** On the last payment, almost everything ($9.90) goes to principal!

---

### 📈 The Big Picture: Complete Amortization Schedule

| Month | Starting Balance | Interest | Principal | Payment | Ending Balance |
|-------|------------------|----------|-----------|---------|----------------|
| 1 | $180.00 | $1.80 | $8.20 | $10.00 | $171.80 |
| 2 | $171.80 | $1.72 | $8.28 | $10.00 | $163.52 |
| 3 | $163.52 | $1.64 | $8.36 | $10.00 | $155.16 |
| 4 | $155.16 | $1.55 | $8.45 | $10.00 | $146.71 |
| 5 | $146.71 | $1.47 | $8.53 | $10.00 | $138.18 |
| 6 | $138.18 | $1.38 | $8.62 | $10.00 | $129.56 |
| 7 | $129.56 | $1.30 | $8.70 | $10.00 | $120.86 |
| 8 | $120.86 | $1.21 | $8.79 | $10.00 | $112.07 |
| 9 | $112.07 | $1.12 | $8.88 | $10.00 | $103.19 |
| 10 | $103.19 | $1.03 | $8.97 | $10.00 | $94.22 |
| 11 | $94.22 | $0.94 | $9.06 | $10.00 | $85.16 |
| 12 | $85.16 | $0.85 | $9.15 | $10.00 | $76.01 |
| 13 | $76.01 | $0.76 | $9.24 | $10.00 | $66.77 |
| 14 | $66.77 | $0.67 | $9.33 | $10.00 | $57.44 |
| 15 | $57.44 | $0.57 | $9.43 | $10.00 | $48.01 |
| 16 | $48.01 | $0.48 | $9.52 | $10.00 | $38.49 |
| 17 | $38.49 | $0.38 | $9.62 | $10.00 | $28.87 |
| 18 | $28.87 | $0.29 | $9.71 | $10.00 | $19.16 |
| 19 | $19.16 | $0.19 | $9.81 | $10.00 | $9.35 |
| 20 | $9.35 | $0.09 | $9.91 | $10.00 | $0.00* |

*Note: Final balance may show small rounding ($0.44 in this case requires adjustment on last payment)

---

### 💡 Key Observations

**Interest Trends:**
- Month 1: $1.80 interest (18% of payment)
- Month 10: $1.03 interest (10.3% of payment)
- Month 20: $0.09 interest (0.9% of payment)

**Principal Trends:**
- Month 1: $8.20 principal (82% of payment)
- Month 10: $8.97 principal (89.7% of payment)
- Month 20: $9.91 principal (99.1% of payment)

**Total Interest Paid:** Sum of all interest = $19.16  
**Total Principal Paid:** $180.00 (the original loan)  
**Total Paid:** $199.16 ($180 + $19.16 interest)

---

### 🧮 Why This Happens

1. **Interest is always calculated on remaining balance**
   - As balance decreases, interest decreases
   - Since payment is fixed, principal increases

2. **Early payments are mostly interest**
   - When you owe $180, 1% interest = $1.80
   - Only $8.20 of your $10 goes to reducing debt

3. **Later payments are mostly principal**
   - When you owe $10, 1% interest = $0.10
   - Now $9.90 of your $10 goes to reducing debt

4. **This is called "amortization"**
   - The gradual payoff of a loan through regular payments
   - Each payment splits between interest and principal
   - Balance steadily decreases to zero

---

### ✅ Verify Your Code

Your program should produce this exact table for a $200 purchase. Check:

- ✓ Exactly 20 months to pay off
- ✓ Each month's ending = next month's starting
- ✓ Interest = previous ending × 0.01
- ✓ Principal = 10.00 - interest
- ✓ All money values have exactly 2 decimals
- ✓ Final balance reaches $0.00 (or very close with rounding)

**If your numbers don't match:**
- Check: Are you using 0.01 (monthly) not 0.12 (annual)?
- Check: Is balance updating each month?
- Check: Is principal = payment - interest (not balance × rate)?

---

