#!/usr/bin/env python
# coding: utf-8

# # write a python program to get the fibonacci series between 0 to 50
# 

# In[3]:


start = int (input("enter the starting number for range: "))
end = int(input("enter the ending number for range: ")) 
a = 0
b = 1
sum = 0
print("fibonacci series between",start, "to", end, "is: ")
while(sum < end):
    a = b
    b = sum
    sum = a + b
    print(b)
print(end = " ")    


# In[ ]:





# In[ ]:





# In[ ]:




