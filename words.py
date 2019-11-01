#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 17:20:01 2019

@author: shan Jiang
"""


'loading packages'
import os
import pandas as pd
import numpy as ny
import codecs
import csv
import nltk
import thulac ## Import THU NLP tool(http://thulac.thunlp.org/)
import pkuseg
import jieba.posseg as pseg


'set current working path'
os.chdir("/Users/shan/Downloads/CASM/Data/")

'Read in two datasets'
xl1 = pd.ExcelFile("./ds_1015/individual_accounts_protest.xlsx")
df = xl1.parse("Sheet1")
xl2 = pd.ExcelFile("./ds_1015/individual_protest_profile_2019-10-15.xlsx")
pf =  xl2.parse("Sheet1")


'overview'  
df = df.rename(str.lower, axis ='columns')
#print(len(df))



'Define the model: news trained'
txt = df['content']
seg = pkuseg.pkuseg(model_name='news', postag = True)  
#print(seg.cut(txt[1]))

new_list = [i[1] for i in seg.cut(txt[1])]
#print(new_list)

cell = dict(seg.cut(txt[1]))
search_tag = ["ns","n","v"]

## Location parse'--match profile user location 
def location_parse():
    location = ()
    party = ()
    action = ()
    geodf = pd.DataFrame({'index': [], 'location': [], 'party':[], 'action':[]})
    ## start from 0, till 99
    for i in range(len(txt)): 
        geodf = geodf.append({'index': i, 'location': location, 'party': party, 'action':action}, 
                             ignore_index=True)
        a = dict(seg.cut(txt[i]))     
        if i == 2:
            print(a)
        temp = {'ns':[], 'n':[], 'v':[]}
        for key, value in a.items():   
            if value in search_tag:
                temp[value].append(key)
#            if (value == search_tag[0]):         
#                temp.append(key)
#            elif (value == search_tag[1]):
#                party = key
            
        location = temp['ns']
        party = temp['n']
        action = temp['v']
        if i == 2:
            print(temp) 
        with pd.ExcelWriter('output.xlsx') as writer:  # doctest: +SKIP
            geodf.to_excel(writer, sheet_name='Sheet_name_1')
                
print(location_parse())  


##if __name__ == "__main__":
##    file= open("file.csv","w") ## open file in write mode
##    for row in  range(0,rows):
##        for col in  range(0,colms): 
##            x,y = pixel2coord(col,row)
##            print "({},{})".format(x,y)
##            lat= ## x or y
##            long= ## x or y
##            file.write("{};{}\n".format(lat,long)) 
#




#for i in range(len(txt)):
#    words = seg.cut(txt[i])
#for word, flag in words:
#    print('%s, %s' % (word, flag))






#'demo 1 for parsing in pkuseg'
#def txt_parse(i):
#    txt1 = {}
#    seg = pkuseg.pkuseg(postag=True)
#    for i in range(len(txt)):
#        txt1 = seg.cut(txt[i])     
#        tag = seg.cut(txt[i]) 
#    return print(tag)        
#
#
#'demo 2 for parsing in pkuseg'
##parse for sentence, use THU package 
#def text_parse(i):	
#    thu1 = thulac.thulac() ## set default 
#    for i in range(0,101):
#        text2 = thu1.cut(txt[i], text =True)  
#    return print(text2)
#
#
#'extract all location variables ns'



'merged dataset'
#mg.df = pd.merge(df, pf, on = "uid")
'Jieba parser'
#words = pseg.cut(txt[1])
#for word, flag in words:
#    print('%s %s' % (word, flag))