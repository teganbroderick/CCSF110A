#Tegan Broderick
#CS110A Assignment 5, Stock Simulation
# The program simulates performance of a stock at a randomly generated annual interest rate over x years. The user inputs the value of an initial stock investment, an expected minimum rate of return, an expected maximum rate of return, and the total years that the stock will be invested. The program outputs 10 illustrations of how the stock might perform, the average of those illustrations, and the average increase in value.

def accrue_interest(deposit, low, high, years):
  """Returns the balance when deposit is invested for a
 specified number of years at a randomly generated interest rate between two values (rate changes yearly)."""

  balance = deposit
  for i in range(years):
    rate = random.randrange(low, high)
    balance = balance + balance*rate/100

  return balance

#Main part of program
import random

num_examples = 10 #set the number of examples/illustrations you want to run

deposit = float(input("Please enter initial stock investment: $"))

low = int(input("Please enter the lowest rate of return you anticipate in a year (as a percentage, for example enter -5 for 5% annual loss):"))

high = int(input("Please enter the highest rate of return you anticipate in a year (as a percentage, for example enter 10 for 10% annual increase): "))

years = int(input("How many years will you keep the investment in these stocks? "))

print("Here are", num_examples, "examples of how much money you might have after those years have passed:")

def sum_example_calculator(num_examples):
  """Outputs a certain amount of example results/illustrations for the accrue_interest function above, and returns a sum of the example outputs)"""
  sumExamples = 0
  for i in range(num_examples):
    newBalance = accrue_interest(deposit, low, high, years)
    print("Illustration #", (i+1), "You might end up with $", format(newBalance, '.2f'))
    sumExamples = sumExamples + newBalance
  return sumExamples


#Calculation of the average balance and percentage increase
total_sum_examples = sum_example_calculator(num_examples)

averageBalance = float(format((total_sum_examples/num_examples), '.2f'))
percentageIncrease = (((averageBalance - deposit)/deposit)*100)


print ("The average of all", num_examples, "illustrations is $", averageBalance, "which is a", format(percentageIncrease, '.2f'),  "% increase in", years, "years")



'''
Sample output 1:
Please enter initial stock investment: $ 1500
Please enter the lowest rate of return you anticipate in a year (as a percentage, for example enter -5 for 5% annual loss): -12
Please enter the highest rate of return you anticipate in a year (as a percentage, for example enter 10 for 10% annual increase):  25
How many years will you keep the investment in these stocks?  15
Here are 10 examples of how much money you might have after those years have passed:
Illustration # 1 You might end up with $ 2298.67
Illustration # 2 You might end up with $ 2920.72
Illustration # 3 You might end up with $ 1983.25
Illustration # 4 You might end up with $ 2069.69
Illustration # 5 You might end up with $ 2221.42
Illustration # 6 You might end up with $ 3644.03
Illustration # 7 You might end up with $ 2387.29
Illustration # 8 You might end up with $ 2848.61
Illustration # 9 You might end up with $ 3553.95
Illustration # 10 You might end up with $ 3959.94
The average of all 10 illustrations is $ 2788.76 which is a 85.92 % increase in 15 years

Sample output 2:
Please enter initial stock investment: $ 750
Please enter the lowest rate of return you anticipate in a year (as a percentage, for example enter -5 for 5% annual loss): -6
Please enter the highest rate of return you anticipate in a year (as a percentage, for example enter 10 for 10% annual increase):  10
How many years will you keep the investment in these stocks?  8
Here are 10 examples of how much money you might have after those years have passed:
Illustration # 1 You might end up with $ 923.79
Illustration # 2 You might end up with $ 846.37
Illustration # 3 You might end up with $ 780.54
Illustration # 4 You might end up with $ 901.73
Illustration # 5 You might end up with $ 908.35
Illustration # 6 You might end up with $ 790.09
Illustration # 7 You might end up with $ 1033.62
Illustration # 8 You might end up with $ 901.14
Illustration # 9 You might end up with $ 941.69
Illustration # 10 You might end up with $ 941.13
The average of all 10 illustrations is $ 896.84 which is a 19.58 % increase in 8 years

Sample output 3:
Please enter initial stock investment: $ 12000
Please enter the lowest rate of return you anticipate in a year (as a percentage, for example enter -5 for 5% annual loss): -5
Please enter the highest rate of return you anticipate in a year (as a percentage, for example enter 10 for 10% annual increase):  5
How many years will you keep the investment in these stocks?  25
Here are 10 examples of how much money you might have after those years have passed:
Illustration # 1 You might end up with $ 9835.83
Illustration # 2 You might end up with $ 11199.02
Illustration # 3 You might end up with $ 8458.71
Illustration # 4 You might end up with $ 8600.18
Illustration # 5 You might end up with $ 10418.93
Illustration # 6 You might end up with $ 11062.21
Illustration # 7 You might end up with $ 13543.37
Illustration # 8 You might end up with $ 9543.69
Illustration # 9 You might end up with $ 9314.67
Illustration # 10 You might end up with $ 7195.19
The average of all 10 illustrations is $ 9917.18 which is a -17.36 % increase in 25 years
'''
