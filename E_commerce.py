#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
pd.options.display.max_rows = 10


# In[ ]:





# In E-commerce, both the retailers (here brands) and the company have to make profit to sustain in the business. The E-Commerce company has the following rule for computing their own revenue:
# The company charges
# 
# (i) 25% on the orders having final price (discounted price) greater than 600
# 
# (ii) 15% on the orders having final price (discounted price) greater than 350 but less than or equal to 600
# 
# (iii) 10% on the orders having final price (discounted price) greater than 100 but less than or equal to 350
# 
# (iv) Otherwise, 5% on the final price (discounted price) 
# 
# Q 1. Find the net revenue generated by the E-Commerce company over all orders placed.

# In[ ]:





# Q2 .Compare performance regionwise
# 
# a) Draw a lineplot for the monthly net Revenue of E-Commerce Company for each region separately. 
# 
# b) Identify the best and the worst performing months for each region. 
# 
# Note: Only those days with actual orders(Order_Date) placed are present in the dataset. Assuming there were no orders on other days

# In[ ]:



