# Financial functions written in python

'''
The Monthly Loan Payment concept in finance refers to the fixed amount of money that
a borrower needs to repay each month to the lender in order
to fully repay a loan over a specified period of time.
------------------------------------------------------------------------------------
Monthly Loan Payment(PMT):
- How much should i pay every month to pay my loan value with interest?
function args:
  pv = present loan value
  rt = rate of interest per given period (years)
  pds = number of periods (years)
exa:
  Let's say we want to calculate how much we have to pay monthly to pay back a loan of 100,000 in 5 years.
  The yearly interest rate is 7%, and is calculated monthly.
'''

def monthly_loan_payment(pv, rt, pds):
  rt = rt / 12
  pds = pds * 12
  pmt = (rt * pv) / (1-(1+rt)**-pds)
  return "The Monthly Loan Payment: " + str("{:.2f}".format(pmt))
    
print(monthly_loan_payment(100000, 0.07, 5))