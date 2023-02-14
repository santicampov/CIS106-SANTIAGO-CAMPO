#input phase
FIXEDCOST = float(input("Please enter the business fixed costs."))
PPU = float(input("Please enter the price per unit."))
CPU = float(input("Please enter the cost per unit."))

#Process Phase
BEPOINT = (FIXEDCOST) / (PPU - CPU)

#Output Phase
print("The amount of units you must sell to reach the break even point is: ", BEPOINT, " units.")