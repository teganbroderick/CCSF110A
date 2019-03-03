#Tegan Broderick
#municalculator.py
#CS110A Homework 3: Muni Ridership Calculator

muniline=input("Which muni line did you survey?")
dayssurveyed=input("How many days did you survey it?")
days=int(dayssurveyed)
ridercount=input("How many riders did you count?")
riders=int(ridercount)


print("Welcome to the Muni Ridership Calculator.")
print("Which Muni line did you survey?", muniline)
print("How many days did you survey it?", dayssurveyed)
print("How many riders did you count?", ridercount)
print("According to your survey, an average of", (riders/days),
"people rode the", muniline, "per day.")




#Sample output
'''
Welcome to the Muni Ridership Calculator.
Which Muni line did you survey? K Ingleside
How many days did you survey it? 5
How many rider did you count? 123456
According to your survey, an average of 24691.2
people rode the K Ingleside per day.
'''
