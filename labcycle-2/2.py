# -*- coding: utf-8 -*-
"""labcycle2: 2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gXXIgwhNsjwO1dDMtjdzFtzkCtr2cG9b
"""

#2 Write a program to read a string containing numbers separated by a space and convert it as a list of integers. Perform the following 
# Perform the following operations on it:
#     1. Rotate elements in a list by 'k' position to the right
#     2. Convert the list into a tuple using list comprehension
#     3. Remove all duplicates from the tuple and convert them into a list again.
#     4. Create another list by putting the results of the evaluation of the function 𝑓(𝑥) = 𝑥2 – 𝑥 with each element in the final list
#     5. After sorting them individually, merge the two lists to  create a single sorted list.

#converting string to list of characters
data= str(input("Enter a set of numbers separated by space : "))
array1=list(data)
n1=len(array1)

#converting characters to int and storing in list
array2=[]
for i in range (0,n1,2):
 temp1=int(array1[i])
 array2.append(temp1)
#to check the list of numbers
print(" ")
print("List made of numbers : ",array2) 

#creating copy of list
n2=len(array2)
array3=[]
for i in range (0,n2):
  array3.insert(i,array2[i])

array4=[]
for i in range (0,n2):
  array4.insert(i,array2[i])

n3=len(array3)
print(" ")
k=int(input("Enter the value of k to rotate the list of numbers : "))
l=0
while l!=k:
  for i in range (0,n2-1,):
    array2[i+1]=array3[i]
  array2[0]=array3[n3-1]
  for i in range (0,n2):
    array3.insert(i,array2[i])
  l=l+1
#to check the rotated list of numbers
print(" ")
print("List after rotation : ",array2) 



t1=tuple([x for x in array4])
#to check the tuple made by list comprehension
print(" ")
print("The tuple made of list comprehension : ",t1)

#removing duplicates 
s1=set(t1)
#converting to list 
array5=list(s1)
#to check new list
print(" ") 
print("The list made after removing duplicates : ",array5)
#list with out put from the function 𝑓(𝑥) = 𝑥2 – 𝑥
array6=[x**2-x for x in array5]
#to check new list 
print(" ")
print("The list made of output of the function 𝑓(𝑥) = 𝑥2 – 𝑥  : ",array6)

#sorting 2 list
array5.sort()
array6.sort()
array7= array5 + array6
array7.sort()

#to check final list
print(" ")
print("The final list : ",array7)