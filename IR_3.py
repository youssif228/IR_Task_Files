import glob
import os
import string
import pandas as pd
import math
import numpy as np
from collections import Counter 
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


os.chdir(r'C:\Users\youss\OneDrive\Desktop\IR Project\Docs')
myFiles= glob.glob('*.txt')

DFdict=[]


#shutil.copyfile(file,'C:\Users\youss\OneDrive\Desktop\DF.txt')
file_size = os.stat('filenew.txt').st_size 
for files in myFiles:
    
    print("\n\n")
    print(files)
    print("\n")
    text = open(files).read()
    lower_case = text.lower()
    cleaned_text = lower_case.translate(str.maketrans('','',string.punctuation))
    tokenized_words = cleaned_text.split()
    text += "\n\n"
    text2 = open('filenew.txt').read()
    
    if files.startswith('Doc'):
        if (file_size==0):
            with open('C:/Users/youss/OneDrive/Desktop/IR Project/Docs/filenew.txt', 'a') as fp:
                fp.write(text)
    
    

    
    ########################## TERM FREQUENCY ################################3
    
    print("\n=========================TERM_FREQUENCY=================================\n")
    
    
    TF = dict(Counter(tokenized_words))

    print(TF)     
    
    ##########################################################3
    
    
    
    
    ########################## NORMALIZED TERM FREQUENCY ################################3
    
    
    if (files.startswith("Doc")):
        
        print("\n=============================NORMALIZED TERM FREQUENCY=============================\n")
        
        DFDict=0
        NORMDFDict=0
        
        DFDict = {}
        NORMDFDict={}
        for word in tokenized_words:
                if word in DFDict:
                    DFDict[word] += 1
                else:
                    DFDict[word] = 1
        for word in DFDict:
            NORMDFDict[word] = DFDict[word] / len(tokenized_words)
        
        print(NORMDFDict)
        
    else:
    
        DFDict=0
        NORMDFDict=0
        
        DFDict = {}
        NORMDFDict={}
        for word in tokenized_words:
                if word in DFDict:
                    DFDict[word] += 1
                else:
                    DFDict[word] = 1
        for word in DFDict:
            NORMDFDict[word] = DFDict[word] / len(tokenized_words)
        print("DF : " , DFDict)
        

      
    
    ########################## NORMALIZED TERM FREQUENCY ################################3
    
    
    

    ########################## IDF ################################3
    if  not ((files.startswith("Doc"))):
        
        print("\n\n=============================INVERSE DOCUMENT FREQUENCY=============================\n\n")  
        
        
        mynewFiles = myFiles[:-1]
        IDFDict=0
        
        IDFDict = {}
        
        for word in DFDict:
            IDFDict[word] = math.log10((len(mynewFiles)) / DFDict[word])
        print(IDFDict)





    
    
    
    ########################## TF_IDF ################################3
    
    if  not ((files.startswith("Doc"))):
        
        print("\n\n=============================TERM FREQUENCY _ INVERSE DOCUMENT FREQUENCY=============================\n\n")  
        
        
        mynewFiles = myFiles[:-1]
        TF_IDFDict=0
        
        TF_IDFDict = {}
        
        for word in DFDict:
            TF_IDFDict[word] = DFDict[word] * IDFDict[word]
        print(TF_IDFDict)




    
        
   
    
    
 