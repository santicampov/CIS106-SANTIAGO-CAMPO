#input phase
EXAM1 = float(input("Please enter your first exam score."))
EXAM2 = float(input("Please enter your second exam score."))

#process phase
EX1TOTAL = EXAM1 * 0.6
EX2TOTAL = EXAM2 * 0.4
FINALTOTAL = EX1TOTAL + EX2TOTAL

#output phase
print("Your total weighted exam score is ", FINALTOTAL)