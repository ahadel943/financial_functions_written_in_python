# Financial functions written in python

'''
The Financial Goal is typically refers to a specific objective or target related
to an individual's ororganization's finances that they aim to achieve within
a certain timeframe.
---------------------------------------------------------------------------------
Get Financial Goal
- How much should i save each month to reach a financial goal?
function args:
  rt: Rate Of Interest
  fg: Financial Goal
  pa: Present Amount (if there is amount already saved, if not then its 0)
  pds: Period in years
exa:
  the monthly deposits needed to achieve 50000 in 5 years with 10% annual interest.
'''

def financial_goal(rt, fg, pa, pds):
   fp = (rt / 12) * (fg - pa * (1 + (rt/12)**(pds*12)))
   sp = (1 + (rt/12))**(pds * 12) - 1
   return "Monthly deposit: " + str("{:.2f}".format(fp / sp))

print (financial_goal(0.10, 50000, 0, 5))
