#!/usr/bin/env python
# coding: utf-8

# In[1]:


BS=float(input("BASIC SALARY"))
HRA=BS/5
DA=BS/2
PF=BS*11/100
print("HRA","=","Rs",HRA)
print("DA","=","Rs",DA)
print("PF","=","Rs",PF)
 
if BS>10000:
    ALLOWANCE = 1700
elif BS>5000:
    ALLOWANCE = 1500
else: 
    ALLOWANCE = 1300
    
gross_salary= BS+HRA+DA+ALLOWANCE-PF
print("GROSS SALARY","=","Rs",gross_salary)


# In[ ]:




