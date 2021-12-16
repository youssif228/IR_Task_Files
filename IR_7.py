

######################################################   COSINE SIMILARITY     ##################################################




import glob
import os
import string
import pandas as pd
import math
import numpy as np
from collections import Counter 
from collections import OrderedDict



os.chdir(r'C:\Users\youss\OneDrive\Desktop\IR Project\Docs')
myFiles= glob.glob('*.txt')

dict = {}

mynewFiles = myFiles[:-1]
size = len(mynewFiles)

query = input("\nEnter Your Query : ")
print("\n\n===================================================================")
query.lower()
print("\n")

for file in mynewFiles:
    
    x = (mynewFiles.index(file))
    #print(x)
    
    
    X_list = query.translate(str.maketrans('','',string.punctuation)).split()
    Y_list = open(file).read().lower().translate(str.maketrans('','',string.punctuation)).split()
        
    l1 =[]
    l2 =[]
    
    X_set = set(X_list)
    Y_set = set(Y_list)
    
    rvector = X_set.union(Y_set) 
    for w in rvector:
        if w in X_set: l1.append(1) 
        else: l1.append(0)
        if w in Y_set: l2.append(1)
        else: l2.append(0)
    c = 0
    

    for i in range(len(rvector)):
            c+= l1[i]*l2[i]
    cosine = c / float(math.pow((sum(l1)*sum(l2)) , 0.5))
    print("similarity between query and " , file , " : " , cosine , "\n\n" )
    

    
    dict[file] = cosine



print("\n\n=================================================   Similarity after Ranking   ================================================\n\n\n")

for x in dict:
    output = OrderedDict(sorted(zip(dict.values() , dict.keys()) , reverse=True)) 

for i in output :
    print("similarity between query and " , output[i] , " : " , i , "\n\n" )

