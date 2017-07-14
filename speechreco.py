# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import time
from speechreco import recordData,mellisa,con_data_text

# Record Audio


     

con_data_text("Hi Krishna, what can I do for you?")
count =1  
time.sleep(2)      
while(count):
    data = recordData()
    mellisa(data)
