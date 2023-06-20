totalCost = float(input("Enter the total cost: "))
downPay = 0.25 * totalCost
currentSavings = 0
r = 0.04
annualSalary = float(input("Enter your annual salary: "))
monthlySalary = annualSalary/12
portionSaved = float(input("How much of your salary should be saved? ")) * monthlySalary


m = 0
while currentSavings < totalCost:
    currentSavings += currentSavings*r/12 + portionSaved
    m += 1

months = str(m)

print("It will take " + months + " months to save up for a house")