# Financial function written in python

'''
Return on Equity (ROE) is a financial metric that measures a company'sprofitability
relative to its shareholders' equity. It shows how effectively a company is using its equity to generate profits.
------------------------------------------------------------------------------------------------------------------
Return on Equity (ROE):<br>
- The ROE calculated per a given period
function argumets:<br>
  * **ni**: The Net Income.
  * **she**: Shareholders' Equity.
### EXAMPLE:
Let's consider Company ABC, which reported a net income of $500,000 and shareholders' equity of $2,000,000 in a given period.
'''

def roe(ni, she):
  roe = (ni / she) * 100
  return str(format(roe, '.2f')) + "%"

print(roe(520000, 2300000))