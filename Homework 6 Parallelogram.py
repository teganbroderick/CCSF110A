#Tegan Broderick
#CS110A Assignment 6 - Parallelogram Program
#Draws a parallelogram made from an input character with an input side length

def repeatCharTop(numRepeats, outputChar):
  for i in range(1, numRepeats-1, 1):
    print(outputChar*i)
  return outputChar*(i+1)

def repeatChar(numRepeats, outputChar):
  """output the outputChar numRepeats times"""
  for colNo in range(numRepeats):
    print(outputChar, end='')
  return ''

def repeatCharBottom(numRepeats, outputChar):
  x = ' '
  """output the outputChar numRepeats times"""
  for j in range((numRepeats-1), 0, -1):
        print((x*(numRepeats-1-j)), (outputChar*j))
  return x

def main():
  """User input for number of repeats and output character, and function calls for the above functions"""
  print("This program will output a parallelogram.")
  numRepeats = int(input("How long do you want each side to be?"))
  outputChar = input("Please enter the character you want it to be made of:")

  drawingTop = repeatCharTop(numRepeats, outputChar)
  print(drawingTop)

  middleLine = repeatChar(numRepeats, outputChar)
  print (middleLine)

  drawingBottom = repeatCharBottom(numRepeats, outputChar)
  print(drawingBottom)

if __name__ == "__main__":
  main()
