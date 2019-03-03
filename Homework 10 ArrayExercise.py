#Tegan Broderick
#CS110A Homework 10
#Array exercise

def double():
  '''Creates a list of  numbers by taking user input, then doubles them '''

  number_list = []

  size = int(input("How many numbers do you want to enter? "))

  for i in range(size):
    number = int(input("Please enter a number: "))
    number_list.append(number)
  print(number_list)

  for i in range(size):
    number = int(number_list[i])*2
    number_list[i] = number
  print(number_list)

def multiples():
  '''Function creates a list of numbers. The list stores n multiples of a number x. The numbers n and x are input from the user.'''

  number_list = []

  x = int(input("Please enter the number you want multiplied: "))
  n = int(input("Please enter the number of times you want to multiply the number: "))

  for i in range(1, n+1):
    number = x*i
    number_list.append(number)
  print(number_list)

def main():
  double()
  multiples()

if __name__ == "__main__":
  main()
