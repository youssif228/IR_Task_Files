import glob
import os
import string
import pandas as pd
import math
import numpy as np
from collections import Counter


os.chdir(r'C:\Users\youss\OneDrive\Desktop\IR Project\Docs')
myFiles = glob.glob('*.txt')


######################################## PHRASE QUERY ##################################################


index_pos_list = []
print("\n")
val = input("Enter term: ")
val.lower()
print("=========================================")

for file in myFiles:
    
    if file.startswith("Doc"):
        
    
        print("\n")
        text = open(file,encoding='utf-8').read() 
        lower = text.lower()
        cleaned_text = lower.translate(str.maketrans('','',string.punctuation))
        tokens = cleaned_text.split()
        
        for i in range(len(tokens)):
            if tokens[i] == val:
                index_pos_list.append(i)
        print(file , "==>" , val , "==>" , index_pos_list)
        if len(index_pos_list)==0:
            print("\n","there is no term in this document")
        index_pos_list.clear()
    
    
   