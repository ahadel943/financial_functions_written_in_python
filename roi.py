# Financial function written in python

'''
Return on Investment (ROI) is a financial metric used to evaluate the profitability
or efficiency of an investment relative to its cost.
------------------------------------------------------------------------------------
Return On Investment(ROI):
- We calculate the roi with formula below, ROI calculated per year
function args:
  bv: Buying Value
  sv: Selling Value
  pd: period
  rntv: Rental Value (if any)
exa_1:
  client bought an apartment with 2,000,000 after 4 years he sold it with 2,900,000, What is the ROI?
exa_2:
  i bought a store with 1,000,000 i was renting it with 1,000 per mon for 5 years and i sold after the 5 
  years with 2,000,000, What is the ROI?
'''

def roi(bv, sv, pd, rntv):
  net_profit_1 = sv - bv
  net_profit_2 = rntv * 12 * pd
  net_profit = net_profit_1 + net_profit_2
  roi = (net_profit / bv) * 100
  y_roi = roi / pd
  return "Yearly ROI: " + str(y_roi) + "%"

print (roi(2000000, 2900000, 4, 0)) # With rental value
print (roi(1000000, 2000000, 5, 1000)) # No rental Value