# Introduction

My name is Antonio Manuel Salvat Pérez and this is the result of my work for the technical test. In the document it is informed about choosing an option, however, after consulting with the team I decided to work on the two options focusing on the first one.

# Option 1

For the realisation of this option we have use pymongo and pandas Python libraries to save this data using MongoDb, we have also made a small example extracting data from another database instead of a csv file.

In this option we have four files.

- [load.py](https://github.com/antoniosp7/ironhack/blob/master/option1/load.py) : In this file we save data in our database in MongoDb from a csv created. To do this we create a dataframe with the pandas library from the csv.

- [list.py](https://github.com/antoniosp7/ironhack/blob/master/option1/list.py) : This file allows us to list the data contained in our database at the current time.

- [loadMongo.py](https://github.com/antoniosp7/ironhack/blob/master/option1/loadMongo.py) : This file saves the data in our MongoDb database but extracts the data from another MongoDb database.

- [students.csv](https://github.com/antoniosp7/ironhack/blob/master/option1/students.csv) : This would be the csv with the data to be copied.
  

# Option 2

As I mentioned in the introduction, I also wanted to make this option even though I have less experience in this field in order to extract an assessment of reasoning when analysing data rather than implemented techniques.

The file for the analysis would be [app.py](https://github.com/antoniosp7/ironhack/blob/master/option2/app.py) and the corresponding dataset would be [Dataset.data.csv](https://github.com/antoniosp7/ironhack/blob/master/option2/Dataset-data.csv)

## Analysis

First of all, it must be emphasised that we have relied on the data from the dataset's admission process. Therefore, a filtering of variables has been carried out. Not only variables unnecessary for this study have been filtered out, but also some that contained a large percentage of null values, except for some that would be relevant.

First of all, I will highlight what in my opinion would be the most important variables to analyse in this study:

- Is Won
- Drop
- Drop Reason C
- Lost Deal Reason C
- Lost Reason Notes C

First of all, it is worth talking about the number of admitted students versus rejected students, the percentage of admitted students is almost 10% of the total, so it is worth analysing the reason for this percentage of rejected students.

To do so, we have obtained a subset of discarded students to analyse these causes through the variables 'Lost Deal Reason C' and 'Lost Reason Notes C'.

After this we see that most of them, 2039 exactly, were discarded for missing the application, a smaller number for not being able to afford the payment (307 students) and the rest in general would be for not being good candidates or personal reasons. Although this seemed to show a problem, upon analysis we can see that the main problem was directly a lack of application.
Therefore, a study should be carried out to improve this data as it influences the time spent by each of the workers to study a possible new candidate.

![Lost Reasons](https://github.com/antoniosp7/ironhack/blob/master/images/lostReasons.png)

Then i analyse the number of students who reject the proposal after having passed the test. Here we have a better figure and that is that only 18 students out of 341 rejected the proposal and most of them were for reasons related to the 'COVID-19' or personal reasons.
With this data, the most interesting thing to study would be to analyse the few cases rejected due to lack of interest, especially if this lack of interest comes from the procedures carried out, and the people who cannot afford to pay.

![Number of drops](https://github.com/antoniosp7/ironhack/blob/master/images/numberDrops.png)


## About the quality of the data

One of the strengths of this dataset could be the reading of data, i.e. in this case we have focused on the admission process and the dataset contains specific variables to extract the reasons for failing the admission. And from here we could also draw a weak point, this type of variable contains a great subjectivity, so the same variable can contain many types of results from the student did not answer to failed a specific test.

For this weak point, I can think of generalising the input data, that is, creating a kind of template with prefixed values, which would make us lose sight of the different reasons but improve a larger scale analysis. 

However, the health of this dataset would be remarkable for the small study that I have carried out, so that we can get an idea of what the main problems or improvements in the admissions process are.