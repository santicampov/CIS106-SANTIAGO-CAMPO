#INPUT PHASE
NAME = input("Please enter your name.")
STEPS = float(input("Please enter the number of steps walked today."))

#PROCESS PHASE
CALORIESBURNED = STEPS * 0.25

#OUTPUT PHASE
print(NAME, " the number of calories burned today are: ", CALORIESBURNED, " calories.")