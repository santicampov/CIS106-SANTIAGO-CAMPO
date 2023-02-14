#input phase
PURCHASEVALUE = float(input("Please enter the value of the stock at the time it was purchased."))
CURRENTVALUE = float(input("Please enter the current value of the stock."))
QUANTITY = float(input("Please enter the amount of stocks purchased."))

#Process phase
NETGAINLOSS = (CURRENTVALUE - PURCHASEVALUE) * QUANTITY

#output phase
print("The net gain (or loss if negative number) is ", NETGAINLOSS, " dollars.")