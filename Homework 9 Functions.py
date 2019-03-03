#Tegan Broderick
#CS110A Homework 9
# Function exercises

def numberDisplay():
  '''displays all numbers between 1 and n, where n is input by the user'''

  n = int(input("Please enter a number:"))
  for i in range(1, n+1):
    print(i)

def numberReverse():
  '''displays the reverse of a number n, where n is input by the user'''

  n = int(input("Please enter a number:"))
  newnum = 0
  while n>0:
    digit = n%10
    newnum = (newnum*10) + digit
    n = n//10
  print("The reverse of your number is ", newnum)

def pattern():
  '''displays a defined pattern for n rows, where n is input by the user'''

  n = int(input("Please enter a number:"))

  for i in range(1, n+1):
    print("$"*i)

def main():
  numberDisplay()
  numberReverse()
  pattern()

if __name__ == "__main__":
  main()
