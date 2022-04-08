#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Q1Write a Python program to multiplies all the items in a list
list=[2,3,6]
int(list[0])*int(list[1])*int(list[2])


# In[3]:


#Q3Write a Python program to combine two dictionary adding values for common keys.
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
a=int(d1.get("a"))+int(d2.get("a"))
b=int(d1.get("b"))+int(d2.get("b"))
c=int(d1.get("c"))+int(d2.get("d"))
d1["a"]=a
d1["b"]=b
d1["c"]=c
print(d1)


# In[4]:


#Q5Write a program to sort a tuple by its float element.
price = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
print(sorted(price))


# In[15]:


#Q2Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples. lists= [(2,5),(1,2),(4,4),(2,3),(2,1)]
# i donot know what is wrong???
lists= [(2,5),(1,2),(4,4),(2,3),(2,1)]
sorted(lists)


# In[22]:


#Q4With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
x = int(input("Type a number: "))
y = {}
for i in range(1, x+1):
    y[i] = i*i
print(y)


# In[ ]:




