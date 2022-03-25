#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Q1 Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them
firstname=input("Enter First Name:")
lastname=input("Enter Last Name:")
print(lastname+" "+firstname)


# In[2]:


#Q2 Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn
#Sample value of n is 5 
#Expected Result : 615 (5+55+555)
x=int(input("Enter a number:"))
x1=x
x2=x*11
x3=x*111
print(x1+x2+x3)


# In[3]:


#Q3 Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user.
x=int(input("enter a number"))
f=x%2
if f==0:
    print(f,"This is an even number")
else:
    print(f,"This is an odd number")


# In[4]:


#Q6Write a program to remove the characters which have odd index values of a given string.
#for example: string ="hello team"
#the result should be: hlota
string="hello team"
print(string[0],string[2],string[4],string[6],string[8])


# In[5]:


#Q7 In this challenge, you must discount a price according to its value.

#- If the price is 500 or above, there will be a 50% discount.
#- If the price is between 200 and 500 (200 inclusive), there will be a 30% discount.
#- If the price is less than 200, there will be a 10% discount.
x=int(input())
if x>=500:
    print("there will be a 50% discount")
elif x>=200 and x<500:
    print("there will be a 30% discount")
elif x<200:
    print("there will be a 10% discount")


# In[ ]:




