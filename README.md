# Financial Functions written in pure python

## The Future Value

The future value (FV) concept in finance refers to the value of
an investment or asset at a specified future point in time,
based on a certain interest rate or rate of return.

Future Value (FV):<br>
How much will my investment worth in a given period in the future?<br>
function arguments:
  * **cv**: Current Value
  * **rt**: Rate of return (Percentage 10% => 0.10)
  * **pds**: Period
### EXAMPLE:
  * if you're trying to calculate the future value of a $500 investment with a 5% compounding annual interest rate over a period of 10 years

```python
def future_value(cv, rt, pds):
    fv = cv * (1 + rt) ** pds
    return "The Future Value(FV): " + str("{:.2f}".format(fv))
```

---

## The Present Value

The Present Value (PV) concept in finance is the current value of a future sum of money or cash flow, discounted to reflect its worth in today's terms.

Present Value (PV):<br>
How much should i invest now to get a specific investment value in a given period in the future?<br>
function args:
  * **fv**: Future Value
  * **rt**: Rate of return (Percentage 10% => 0.10)
  * **pds**: Period
### EXAMPLE:
Let's say you have the choice of being paid $2,000 today earning 3% annually 
or $2,200 one year from now. Which is the best option?

```python
def get_present_value(fv, rt, pds):
    pv = fv / (1 + rt) ** pds
    return "The Present Value(PV): " + str("{:.2f}".format(pv))
```

---

## The Monthly Loan Payment

The Monthly Loan Payment concept in finance refers to the fixed amount of money that
a borrower needs to repay each month to the lender in order
to fully repay a loan over a specified period of time.

Monthly Loan Payment(PMT):<br>
How much should i pay every month to pay my loan value with interest?
function args:<br>
  * **pv**L: present loan value
  * **rt**L: rate of interest per given period (years)
  * **pds**L: number of periods (years)
### EXAMPLE:
Let's say we want to calculate how much we have to pay monthly to pay back a loan of 100,000 in 5 years.
The yearly interest rate is 7%, and is calculated monthly.

```python
def monthly_loan_payment(pv, rt, pds):
  rt = rt / 12
  pds = pds * 12
  pmt = (rt * pv) / (1-(1+rt)**-pds)
  return "The Monthly Loan Payment: " + str("{:.2f}".format(pmt))
```

--- 

## The Financial Goal

The Financial Goal is typically refers to a specific objective or target related to an individual's or organization's finances that they aim to achieve within a certain timeframe.

The Financial Goal<br>
How much should i save each month to reach a financial goal?
function args:<br>
  * **rt**: Rate Of Interest
  * **fg**: Financial Goal
  * **pa**: Present Amount (if there is amount already saved, if not then its 0)
  * **pds**: Period in years
### EXAMPLE:
The monthly deposits needed to achieve 50000 in 5 years with 10% annual interest.

```python
def financial_goal(rt, fg, pa, pds):
   fp = (rt / 12) * (fg - pa * (1 + (rt/12)**(pds*12)))
   sp = (1 + (rt/12))**(pds * 12) - 1
   return "Monthly deposit: " + str("{:.2f}".format(fp / sp))
```

---

## The Net Present Value

Net Present Value (NPV) is a financial metric used to evaluate the profitability of
an investment or project by comparing the present value of its expected cash inflows
(such as revenues, dividends, or savings) to the present value of its expected cash
outflows (such as initial investment costs or ongoing expenses).

Net Present Value(NPV):<br>
Helps to know if a project or an investment is worthwhile
if npv is positive value then the project is profitable and managers should accept it,
if negative then the project has a net loss and should not be accepted.
function arguments:<br>
  * **cf**: CashFlow
  * **rt**: Discount Rate (percentage)
  * **pds**: Period
  * **iv**: Initial Investment
### NOTE: 
  if we have more than one cashflow then we sum the npv of each year then subtract it from the initial investment.
### EXAMPLE:
Project X requires an initial investment of $100,000 but is expected to generate revenues of
$10,000 for the first year.
The target rate of return is 20%. Since the cash inflows are uneven, 
the NPV Value is ?

```python
def npv(cf, rt, pds, iv):
    npv = cf / (1 + rt)**pds - iv
    return "Net Present Value=> " + str("{:.2f}".format(npv))
```

---

## The Return On Investment

Return on Investment (ROI) is a financial metric used to evaluate the profitability
or efficiency of an investment relative to its cost.

Return On Investment(ROI):<br>
- We calculate the roi with formula below, ROI calculated per year
function argumets:<br>
  * **bv**: Buying Value
  * **sv**: Selling Value
  * **pd**: period
  * **rntv**: Rental Value (if any)
### EXAMPLE_1:
Client bought an apartment with 2,000,000 after 4 years he sold it with 2,900,000, What is the ROI?
### EXAMPLE_2:
I bought a store with 1,000,000 i was renting it with 1,000 per mon for 5 years and i sold after the 5 
years with 2,000,000, What is the ROI?

```python
def roi(bv, sv, pd, rntv):
  net_profit_1 = sv - bv
  net_profit_2 = rntv * 12 * pd
  net_profit = net_profit_1 + net_profit_2
  roi = (net_profit / bv) * 100
  y_roi = roi / pd
  return "Yearly ROI: " + str(y_roi) + "%"
```

---

## The Return on Equity

Return on Equity (ROE) is a financial metric that measures a company's profitability relative to its shareholders' equity. It shows how effectively a company is using its equity to generate profits.

Return on Equity (ROE):<br>
- The ROE calculated per a given period
function argumets:<br>
  * **ni**: The Net Income.
  * **she**: Shareholders' Equity.
### EXAMPLE:
Let's consider Company ABC, which reported a net income of $500,000 and shareholders' equity of $2,000,000 in a given period.

```python
def roe(ni, she):
  roe = (ni / she) * 100
  return str(format(roe, '.2f')) + "%"
```
