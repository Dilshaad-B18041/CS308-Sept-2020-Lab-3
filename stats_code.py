#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 20:06:48 2020

@author: Mohd Asim Ansari
Roll no. : B18177 
"""
#%% opening required files

token_file = open("token_count.txt","r") # file containing words after removing articles,prepos etc 
                                       # and their corresponding count
                                       
browsed_file = open("browsed_file.txt","r")# actual text file  

word_dict = {} # Dictionary to hold words and their corresponding frequency

for line in token_file:                     # making the word_dict dictionary 
    word,cnt = line.strip().split(" ")
    word_dict[word] = int(cnt)

#%%  Finding all words that occured maximum time
        
max_cnt = max(word_dict.items(), key = lambda x: x[1])   #frequency of word(s) occurung max time

max_occur_word=list()     # list to hold all words having max frequency

for key,value in word_dict.items(): # collecting all words having max frequency
    if value == max_cnt[1]:
        max_occur_word.append(key)
        
print("======words occuring maximum number of times is/are ========\n")
for word in max_occur_word:
    print(word,"\n")
print("number of times each of these word occur is : ",max_cnt[1],"\n\n\n")   # printing all words occured max time


#%% Finding all words that occured minimum number of time

min_cnt = min(word_dict.items(), key = lambda x: x[1])   #frequency of word(s) occurung min time

min_occur_word = list()    # list to hold all words having min frequency

for key,value in word_dict.items():       # collecting all words having min frequency
    if value == min_cnt[1]:
        min_occur_word.append(key)
        
print("=========words occuring minimum number of times is/are========\n")
for word in min_occur_word:
    print(word,"\n")
print("number of times each of these word occur is : ",min_cnt[1],"\n\n\n")     # printing all words occured min time

#%% counting number of sentences , number of words after removing prepos,articles etc

all_lines = browsed_file.readlines()  # reading actual text file

sentence_cnt = 0          #number of sentences
new_line_cnt = 0          #number of lines

for line in all_lines:   # calculating number of lines and number of sentences
    for char in line:
        if char == ".":
            sentence_cnt += 1
        elif char == "\n":
            new_line_cnt += 1
            
print("===============================================================")            

print("Number of sentences in the given text file is : ",sentence_cnt,"\n\n\n")  #printing number of sentences

print("Number of lines in the given text file is : ",new_line_cnt,"\n\n\n")    #printing number of lines

print("Number of words after removing articles, propositions etc is : ",len(word_dict.keys()),"\n\n\n")    #printing
 #number of words after removing prepos, articles etc
 
#%% words-frequency plot

import matplotlib.pyplot as plt

print("===============================================================")            

plt.style.use('ggplot')

plt.figure(figsize=(20,6))

plt.bar(word_dict.keys(),word_dict.values(),width=0.4,align='center')

plt.xticks(rotation='vertical')

plt.xlabel("Words ----->")

plt.ylabel("Frequency----->")

plt.title("Words and their corresponding frequency of occurance")

plt.show()