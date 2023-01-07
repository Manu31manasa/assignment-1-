#!/usr/bin/env python
# coding: utf-8

# # write a python program to count the number of even and odd numbers from a series of numbers

# In[1]:


x = eval(input("enter a series of numbers: "))
count_even = 0
count_odd = 0
for i in x:
    if i % 2 == 0:
        count_even = count_even + 1
    else:
        count_odd = count_odd + 1
print("number of even number in given series is: ", count_even)
print("number of odd numbers in given series is: ", count_odd)

            


# In[ ]:




