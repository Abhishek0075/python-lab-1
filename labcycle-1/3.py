# -*- coding: utf-8 -*-
"""labcycle1: 3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_fuH4ndvGbEnqmZnn8H5uyHBsFzdqJ1l
"""

# 3 Develop a program to read the employee's name, code, and basic pay
# and calculate the gross salary, deduction, and net salary according to
# the following conditions. Define a function to find each of the
# components. Finally, generate a payslip.
name= str(input("enter the name of the employee: "))# taking details of employee
code= int(input("enter the code of the employee: "))
BP= float(input("enter the basic pay of the employee: "))
def calc():# calculating net salary
  if(BP>50000):
    GS= BP+BP*(25/100)+BP*(11/100)+7000# using elsif to calculate salary for different cases
    D= 80+BP*(12/100)+BP*(20/100)
    NS= GS-D
  elif(50000>BP and BP>30000):
    GS= BP+BP*(11/100)+BP*(7.5/100)+5000
    D= 60+BP*(11/100)+BP*(11/100)
    NS= GS-D
  elif(30000>BP and BP>10000):
    GS= BP+BP*(7.5/100)+BP*(5/100)+2500
    D= 60+BP*(8/100)
    NS= GS-D
  else:
    GS= BP+BP*(5/100)+BP*(2.5/100)+500
    D= 20+BP*(8/100)
    NS= GS-D
  return NS
  
print("payslip")# printing payslip
print("Name= ",name)
print("Code= ",code)
print("Net salary= ",calc())