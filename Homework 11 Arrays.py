#Tegan Broderick
#CS110A Homework 11
# Takes user input to create an array of numbers. Finds the unique numbers in the array, the maximum value and the minimum value.

def listfunction():
  '''Takes input from the user to create a list of numbers. Creates a new list of unique numbers from the original number list. Outputs the amount of unique numbers in the list, the minumum value, and the maximum value.'''

  number_list = []
  unique_number_list = []

  print("Please enter some positive integers, hitting return after each one. Enter 'q' to quit:")

  repeat = True
  while repeat == True: #input for number list
    number = input()
    if number.isdigit():
      number_list.append(int(number))
    else:
      repeat = False


  listlength = len(number_list) #length of number list

  for i in range(listlength): #appends unique numbers from number list into unique number list
    num = number_list[i]
    if num not in unique_number_list:
      unique_number_list.append(num)

  listlength2 = len(unique_number_list) #length of unique number list

  print("You entered", listlength2, "unique numbers: ")
  print(unique_number_list)
  print("with a minumum value: ", min(unique_number_list), "and a maximum value:", max(unique_number_list))

def main():
  listfunction()

if __name__ == "__main__":
  main()
