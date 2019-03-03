#Tegan Broderick
#CS110A Homework 8 - Consumer Loan Program
#Program calculates how long it will take to pay off a loan, the final payment amount, and the total interest paid.

def inputPrinciple():
  ''' User input for principle amount borrowed'''

  print("** Welcome to the Consumer Loan Calculator **")

  principle = float(input("How much do you want to borrow?"))
  
  while principle <=0:
    print("You must enter a positive number!")
    principle = float(input("How much do you want to borrow?"))

  return principle

def inputInterestRate():
  ''' User input for yearly interest rate. Function converts yearly rate to monthly rate.'''

  yearlyInterestRate = float(input("What is the annual interest rate expressed as a percent?"))

  while yearlyInterestRate <=0:
    print("You must enter a positive number!")
    yearlyInterestRate = float(input("What is the annual interest rate expressed as a percent?"))

  monthlyInterestRate = float((yearlyInterestRate / 12) * 1/100)
  #print (monthlyInterestRate) #For checking that the monthly interest rate is being calculated correctly

  return monthlyInterestRate

def inputMonthlyPayment(principle, monthlyInterestRate):
  ''' User input for monthly payment. Function verifies that the input is positive, and greater than the minimum monthly payment amount. If it is not greater than the minimum monthly payment amount, the program quits '''

  monthlyPayment= float(input("What is the monthly payment amount?"))

  while monthlyPayment <= 0:
     print("You must enter a positive number!")
     monthlyPayment= float(input("What is the monthly payment amount?"))

  minPayment = principle * monthlyInterestRate + 1

  minPaymentFormatted = format((principle * monthlyInterestRate + 1), '.2f')

  monthlyInterest = format((principle * monthlyInterestRate), '.2f')

  if monthlyPayment < minPayment:
    print("You must make payments of at least $" + minPaymentFormatted + ", because your monthly interest is $" + monthlyInterest)
    print("** Don't get overwhelmed with debt! **")

    quit()

  return monthlyPayment


def calculation(principle, monthlyInterestRate, monthlyPayment):
  '''Function calculates the total interest paid over the period of the loan, how many months it will take to pay the loan back, and the final payment amount'''

  balance = principle
  x = 0
  totalInterest = 0
  count = 0

  while balance >= x:
    totalInterest = totalInterest + (balance * monthlyInterestRate)
    balance = balance + (balance * monthlyInterestRate) - monthlyPayment
    count = count + 1

    #print ("Month " + str(count) + " balance: " + str(balance) + " , and interest: " + str(totalInterest)) #prints balance and interest for every loop

  finalBalance = format((monthlyPayment +  balance), '.2f')

  truncatedTotalInterest = format((totalInterest), '.2f')

  print("Your debt will be paid off after " + str(count) + " months, with a final payment of just $" + str(finalBalance))

  print ("The total amount of interest you will pay during that time is " + str(truncatedTotalInterest))

  print("** Don't get overwhelmed with debt! **")


def main():

  x = inputPrinciple()
  y = inputInterestRate()
  z = inputMonthlyPayment(x, y)

  calculation(x, y, z)


if __name__ == "__main__":
  main()



'''
Example 1:
** Welcome to the Consumer Loan Calculator **
How much do you want to borrow? 1000
What is the annual interest rate expressed as a percent? 18
What is the monthly payment amount? 50
Your debt will be paid off after 24 months, with a final payment of just $47.83
The total amount of interest you will pay during that time is 197.83
** Don't get overwhelmed with debt! **

Example 2:
** Welcome to the Consumer Loan Calculator **
How much do you want to borrow? 15000
What is the annual interest rate expressed as a percent? 10
What is the monthly payment amount? 100
You must make payments of at least $126.00, because your monthly interest is $125.00
** Don't get overwhelmed with debt! **

Example 3:
** Welcome to the Consumer Loan Calculator **
How much do you want to borrow? -50
You must enter a positive number!
How much do you want to borrow? -200
You must enter a positive number!
How much do you want to borrow? 20000
What is the annual interest rate expressed as a percent? -2.5
You must enter a positive number!
What is the annual interest rate expressed as a percent? 5
What is the monthly payment amount? 0
You must enter a positive number!
What is the monthly payment amount? 200
Your debt will be paid off after 130 months, with a final payment of just $125.79
The total amount of interest you will pay during that time is 5925.79
** Don't get overwhelmed with debt! **
'''
