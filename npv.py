# Financial function written in python

'''
Net Present Value (NPV) is a financial metric used to evaluate the profitability of
an investment or project by comparing the present value of its expected cash inflows
(such as revenues, dividends, or savings) to the present value of its expected cash
outflows (such as initial investment costs or ongoing expenses).
--------------------------------------------------------------------------------------
Net Present Value(NPV):
- Helps to know if a project or an investment is worthwhile
  if npv is positive value then the project is profitable and managers should accept it,
  if negative then the project has a net loss and should not be accepted.
function args:
  cf: CashFlow
  rt: Discount Rate (percentage)
  pds: Period
  iv: Initial Investment
note: 
  if we have more than one cashflow then we sum the npv of each year then subtract it from the initial investment.
exa:
  Project X requires an initial investment of $100,000 but is expected to generate revenues of
  $10,000 for the first year.
  The target rate of return is 20%. Since the cash inflows are uneven, 
  the NPV Value is ?
'''

def npv(cf, rt, pds, iv):
    npv = cf / (1 + rt)**pds - iv
    return "Net Present Value=> " + str("{:.2f}".format(npv))

print (npv(10000, 0.20, 1, 100000))