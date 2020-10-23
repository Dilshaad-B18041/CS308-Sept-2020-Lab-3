from tkinter import *
import tkinter
from tkinter import filedialog
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)
import pandas as pd

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def func(window, maxprint, minprint, sentprint, fig, plot1):
    # file containing words after removing articles,prepos etc
    token_file = open("token_count.txt", "r")
    # and their corresponding count

    browsed_file = open("browsed_file.txt", "r")  # actual text file

    word_dict = {}  # Dictionary to hold words and their corresponding frequency

    for line in token_file:                     # making the word_dict dictionary
        word, cnt = line.strip().split(" ")
        word_dict[word] = int(cnt)

    # %%  Finding all words that occured maximum time

    # frequency of word(s) occurung max time
    max_cnt = max(word_dict.items(), key=lambda x: x[1])

    max_occur_word = list()     # list to hold all words having max frequency

    for key, value in word_dict.items():  # collecting all words having max frequency
        if value == max_cnt[1]:
            max_occur_word.append(key)

    cnt = 0
    pstr = ""
    # labelprint = Label(window, text="maximum occuring words: ", fg="black")
    for word in range(len(max_occur_word)):
        if (word != len(max_occur_word) - 1):
            if(cnt == 30):
                cnt = 0
                pstr += "\n"
            pstr += max_occur_word[word]
            pstr += ", "
            cnt = cnt + 1
        else:
            if(cnt == 30):
                cnt = 0
                pstr += "\n"
            pstr += max_occur_word[word]
            cnt = cnt + 1
    # pstr[len(pstr) - 2] = " "
    maxprint.configure(
        text="maximum("+str(max_cnt[1])+") occuring words: "+pstr)
    # labelprint.grid(column=1, row=4)
    # print("number of times each of these word occur is : ",max_cnt[1],"\n\n\n")   # printing all words occured max time

    # %% Finding all words that occured minimum number of time

    # frequency of word(s) occurung min time
    min_cnt = min(word_dict.items(), key=lambda x: x[1])

    min_occur_word = list()    # list to hold all words having min frequency

    for key, value in word_dict.items():       # collecting all words having min frequency
        if value == min_cnt[1]:
            min_occur_word.append(key)

    cnt = 0
    pstr = ""
    # labelprint = Label(window, text="maximum occuring words: ", fg="black")
    for word in range(len(min_occur_word)):
        if (word != len(min_occur_word) - 1):
            if(cnt == 30):
                cnt = 0
                pstr += "\n"
            pstr += min_occur_word[word]
            pstr += ", "
            cnt = cnt + 1
        else:
            if(cnt == 30):
                cnt = 0
                pstr += "\n"
            pstr += min_occur_word[word]
            cnt = cnt + 1
    # pstr[len(pstr) - 2] = " "
    minprint.configure(
        text="minimum("+str(min_cnt[1])+") occuring words: "+pstr)

    # print("=========words occuring minimum number of times is/are========\n")
    # for word in min_occur_word:
    #     print(word,"\n")
    # print("number of times each of these word occur is : ",min_cnt[1],"\n\n\n")     # printing all words occured min time

    # #%% counting number of sentences , number of words after removing prepos,articles etc

    all_lines = browsed_file.readlines()  # reading actual text file

    sentence_cnt = 0  # number of sentences
    new_line_cnt = 0  # number of lines

    for line in all_lines:   # calculating number of lines and number of sentences
        for char in line:
            if char == ".":
                sentence_cnt += 1
            elif char == "\n":
                new_line_cnt += 1

    # print("===============================================================")

    # print("Number of sentences in the given text file is : ",sentence_cnt,"\n\n\n")  #printing number of sentences
    sentprint.configure(text="Total number of sentences: "+str(sentence_cnt)+"\n"+"Total number of lines: "+str(
        new_line_cnt)+"\n"+"Number of words after removing articles, propositions etc: "+str(len(word_dict.keys())))
    # print("Number of lines in the given text file is : ",new_line_cnt,"\n\n\n")    #printing number of lines

    # print("Number of words after removing articles, propositions etc is : ",len(word_dict.keys()),"\n\n\n")    #printing
    # #number of words after removing prepos, articles etc

    # #%% words-frequency plot

    # figure1 = plt.Figure(figsize=(6, 5), dpi=100)
    # ax1 = figure1.add_subplot(111)
    #bar1 = FigureCanvasTkAgg(figure1, window)
    #bar1.get_tk_widget().pack(side=tkinter.LEFT, fill=tkinter.BOTH)
    # data1 = {'Country': ['US', 'CA', 'GER', 'UK', 'FR'],
    #          'GDP_Per_Capita': [45000, 42000, 52000, 49000, 47000]
    #          }
    # df1 = pd.DataFrame(data1, columns=['Country', 'GDP_Per_Capita'])

    # df1 = df1[['Country', 'GDP_Per_Capita']].groupby('Country').sum()

    # df1.plot(kind='bar', legend=True, ax=ax1)
    # ax1.set_title('Country Vs. GDP Per Capita')

    plot1.bar(word_dict.keys(), word_dict.values())
    # plot1.xticks(rotation='vertical')
    plot1.set_xticklabels(word_dict.keys(), rotation=90)
    canvas = FigureCanvasTkAgg(fig,
                               master=window)

    canvas.draw()

    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack()

    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas,
                                   window)
    toolbar.update()

    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack()

    # print("===============================================================")

    # plt.style.use('ggplot')

    # plt.figure(figsize=(20, 6))

    # plt.bar(word_dict.keys(), word_dict.values(),
    #         width=0.4, align='center', ax=ax1)

    # plt.xticks(rotation='vertical')

    # plt.xlabel("Words ----->")

    # plt.ylabel("Frequency----->")

    # plt.title("Words and their corresponding frequency of occurance")

    # plt.show()

