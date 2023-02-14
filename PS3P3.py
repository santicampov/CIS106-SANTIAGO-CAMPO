#input phase
MEALPRICE = float(input("Please enter the total of the meal."))

#process phase
FIFTEEN = (MEALPRICE * 0.15)
EIGHTEEN = (MEALPRICE * 0.18)
TWENTY = MEALPRICE * 0.20
TOTALFIFTEEN = MEALPRICE + FIFTEEN
TOTALEIGHTEEN = MEALPRICE + EIGHTEEN
TOTALTWENTY = MEALPRICE + TWENTY

#output phase
print("Please select one:")
print("With 15% tip, Total: $",MEALPRICE, " Tip: $", FIFTEEN, " TOTAL WITH TIP: $",TOTALFIFTEEN)
print("With 18% tip, Total: $",MEALPRICE, " Tip: $", EIGHTEEN, " TOTAL WITH TIP: $",EIGHTEEN)
print("With 20% tip, Total: $",MEALPRICE, " Tip: $", TWENTY, " TOTAL WITH TIP: $",TOTALTWENTY)