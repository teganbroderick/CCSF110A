#Avi Horowitz & Tegan Broderick
#CS110A Homework 12 Project
#Two dimensional lists for class score inputs, returning highest scores for each class, lowest scores for each class, and highest average scores


def getmaxIndex(classScores): #returns the index of the student with the highest score in classScores
	highestScore = max(classScores)
	i = classScores.index(highestScore)
	return i

def getminIndex(classScores): #returns the index of the student with the lowest score in classScores
	lowestScore = min(classScores)
  	i = classScores.index(lowestScore)
	return i

def getscoreslist(A): #creating scores list for each class
	ClassA = []
	ClassB = []
	ClassC = []
	ClassD = []
	for i in range (len(A)):
		ClassA.append(A[i][1])
		ClassB.append(A[i][2])
		ClassC.append(A[i][3])
		ClassD.append(A[i][4])
	return [ClassA, ClassB, ClassC, ClassD]

def maxStudent(A): #printing max score function
	scoreslist = getscoreslist(A)
	ClassA = scoreslist[0]
	ClassB = scoreslist[1]
	ClassC = scoreslist[2]
	ClassD = scoreslist[3]
	print ("Student with highest score in Class A: ",A[getmaxIndex(ClassA)])
	print ("Student with highest score in Class B: ",A[getmaxIndex(ClassB)])
	print ("Student with highest score in Class C: ",A[getmaxIndex(ClassC)])
	print ("Student with highest score in Class D: ",A[getmaxIndex(ClassD)])
	print()

def minStudent(A): #printing min score function
	scoreslist = getscoreslist(A)
	ClassA = scoreslist[0]
	ClassB = scoreslist[1]
	ClassC = scoreslist[2]
	ClassD = scoreslist[3]
	print ("Student with lowest score in Class A: ",A[getminIndex(ClassA)])
	print ("Student with lowest score in Class B: ",A[getminIndex(ClassB)])
	print ("Student with lowest score in Class C: ",A[getminIndex(ClassC)])
	print ("Student with lowest score in Class D: ",A[getminIndex(ClassD)])
	print()

def getaveragescore(studentrecord): #average score of each student
	return sum(studentrecord[1:len(studentrecord)])/(len(studentrecord)-1)

def highestaverage(A): #compares highest average scores
	averagelist = []
	for studentrecord in A:
		averagelist.append(getaveragescore(studentrecord))
	print ("Student with the highest average score: ",A[getmaxIndex(averagelist)])
	return getmaxIndex(averagelist)

def main():
	A = [] #each student record

	numStudents = int(input("How many students do you want to record scores for? "))
	print()

	for i in range (numStudents): #student score inputs
		name = input("Please enter a name: ")
		scoreA = int(input("Score for Class A: "))
		scoreB = int(input("Score for Class B: "))
		scoreC = int(input("Score for Class C: "))
		scoreD = int(input("Score for Class D: "))
		A.append([name, scoreA, scoreB, scoreC, scoreD])
		print()
	print(A)
	print()

	#calling all necessary functions
	maxStudent(A)
	minStudent(A)
	highestaverage(A)

main()
