#!/usr/bin/env python
# coding: utf-8

# In[1]:


num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))


# In[4]:


celsius = 35

# calculate fahrenheit
fahrenheit = (celsius * 1.8) + 32
print('%0.1f degree Celsius is equal to %0.1f degree Fahrenheit' %(celsius,fahrenheit))


# In[14]:


def recur_factorial(n):
   if n == 1:
       return n
   else:
       return n*recur_factorial(n-1)

num = 25
if num == 0:
   print("The factorial of 0 is 1")
else:
   print("The factorial of", num, "is", recur_factorial(num))


# In[29]:



list1 = [2, 4, 6, 5, 9]
  

list1.sort()
  

print("Largest element is:", list1[-1])


# In[27]:


L1=[1,2,3,4,5,6,7,8,9]
del L1[2]
L1


# In[35]:


score = { 'Ritika': 5,
            'Sam': 7, 
            'John': 10, 
            'Aadi': 8}
score


# In[36]:


sum = 0

for _ in range(10):
    n = float(input('Enter a number: '))
    sum = sum + n

average = sum/10

print(f'The average of these numbers is: {average}')


# In[ ]:




