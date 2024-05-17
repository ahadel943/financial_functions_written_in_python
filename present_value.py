# Financial functions written in python

'''
The Present Value (PV) concept in finance is the current value
of a future sum of money or cash flow, discounted to
reflect its worth in today's terms.
----------------------------------------------------------------
Present Value (PV):
- How much should i invest now to get a specific investment value in a given period in the future?
function args:
  fv: Future Value
  rt: Rate of return (Percentage 10% => 0.10)
  pds: Period
exp:
  Let's say you have the choice of being paid $2,000 today earning 3% annually 
  or $2,200 one year from now. Which is the best option?
'''

def present_value(fv, rt, pds):
  pv = fv / (1 + rt) ** pds
  print("The Present Value(PV): " + str("{:.2f}".format(pv)))
  
print (present_value(2000, 0.03, 1))
print (present_value(2200, 0.03, 1))