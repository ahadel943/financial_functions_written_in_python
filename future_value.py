# Financial functions written in python

'''
The future value (FV) concept in finance refers to the value of
an investment or asset at a specified future point in time,
based on a certain interest rate or rate of return.
--------------------------------------------------------------------
Future Value (FV): 
- How much will my investment worth in a given period in the future?
function args:
  cv: Current Value
  rt: Rate of return (Percentage 10% => 0.10)
  pds: Period
exp:
  if you're trying to calculate the future value of a $500 investment 
  with a 5% compounding annual interest rate over a period of 10 years
'''

def future_value(cv, rt, pds):
    fv = cv * (1 + rt) ** pds
    return"The Future Value(FV): " + str("{:.2f}".format(fv))

print (future_value(500, 0.05, 10))