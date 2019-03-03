#Tegan Broderick
#CS110A Homework 13
#Program generates system login names for students

def main():
  firstName = input("Please enter the student's first name: ")
  lastName = input("Please enter the student's last name: ")
  idNumber = input("Please enter the student's ID number: ")

  login = get_login_name(firstName, lastName, idNumber)

  print("The student's login name is: ", login)

def get_login_name(Name1, Name2, ID):
  '''Generates a login name from the first three letters of the student's first name, first three letters of the student's last name, and the last three characters of the student ID number'''

  studentLogin = Name1[0:3] + Name2[0:3] + ID[-3:]

  return studentLogin


if __name__ == "__main__":
  main()
