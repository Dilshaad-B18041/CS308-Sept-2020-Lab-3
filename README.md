# CS308-Sept-2020-Lab-3

Team members

- A.Dilshaad B18041
- Rahul Anand B18078
- Mohd Asim Ansari B18177
- Mohib Qureshi B18070
- Abhinav Mehta B18099

## File Analyser app

This app is capable to provide the statistical data of the words 
in the text file uploaded by the user. The statistical data may include
a histogram, bar graph etc. of the data in the text file. It can also extract
sentences having required keywords given by the user. 

### Design

- Accepts input text file from the user and saves it in the current directory.
- Refines the text file and separates words in the file based on
    - Punctuations `. / ' "`
    - Spaces and prepositions.
    - Keywords from the given file.
- Saves the refined data in a new txt file in the current directory.
- Create graphs based on the data obtained from the refined file.
- Feature to edit the file again and then refresh the screen to display statistics 
wrt new changes

### Requirements

- Python3
- tkinter
- nltk
- Pandas
- Matplotlib

### How to run ?

1. Clone this repo using `git clone` ---
2. Go to the folder CS308-Sept-2020-Lab-3.
3. Install the required liraries.
4. Run `main.py` file using `python main.py`.
5. Upload a `.txt` file by clicking on **Choose Main Text File** button.
6. Now click on **Choose Ignore Text File** button to select a file with the words user wants to
   exclude other than punctuations and articles.
7. Now click on **Choose Extract Text File** button and select file which will have the keywords
   and the corresponding sentences will get extracted.
