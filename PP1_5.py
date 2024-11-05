'''
    Lesson: Typecasting
    Author: Mr. Kalisz
    Date Creatd: Sept 23, 2024
    Date Last Modified: Nov 04, 2024
'''

def q1():
  num1= input("Input an integer: ")
  num1=int(num1)
  num2=(num1+3)
  print(num2)

def q2():
  num1= input("Input a number: ")
  num2=(num1+ "4")
  num3= float(num2)
  num4= (num3+2)
  print(num4)

def q3():
  radius= input("Input a radius: ")
  radius1= float(radius)
  print(radius1**2 * 3.14 )

def q4():
import math 
  num1= input("Input a number: ")
  num1= float(num1)
  num2= num1 * 12 
  num2= math.floor(num2)
  print(num2)

def q5():
  num1= input("Input an integer: ")
  num1= int(num1)
  var= (num1 + 5)
  print (f"Your number + 5 is {var}")

#Comment this code out when running tests
#Do not comment this out when running your program normally

#q1()
#q2()
#q3()
#q4()
#q5()
