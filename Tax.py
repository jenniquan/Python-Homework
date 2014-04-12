# Then modify this into a function that will compute
# takes a purchase amount and sales tax percentage
# and returns the cost of the item + tax.

purchaseAmount = float (raw_input ("Purchase amount? "))
salesTaxRate = float (raw_input ("Sales tax rate as a decimal? "))
salesTaxAmount = purchaseAmount * salesTaxRate
TotalAmount= round (purchaseAmount + salesTaxAmount, 2)
print "Total amount: ", TotalAmount




