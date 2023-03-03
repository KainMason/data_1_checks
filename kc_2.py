# Assignment Details
"""# Welcome to Knowledge Check 2! 

I hope the videos are going well. Today, we're going to try loading some data and generating a plot using pandas and seaborn. Here are your instructions: 

1. Create a new file in your "data_1_checks" repository titled "kc_2". Remember, you can use .py files or .ipynb. The only problem with colab (what this was written in) is that it's a little trickier to commit to GitHub with it (at least as of this writing in April 2022). We really want you to be able to work with git and GitHub seamlessly, so you have to go the slightly longer route now of doing everything locally rather than on this server.
2. Make a folder titled "assets" in your repo. This is where you will put any CSVs or other files you download you want to load in. This is a nice way to organize data - if you drop everything in your main folder (in your case, "data_1_checks") you'll have a bunch of random data floating around intermingled with the files.
3. Load your data into a DataFrame. 
4. Plot ANY of your data with seaborn (or matplotlib, or any other plotting tool if you have one you really like).
5. Push your changes to GitHub, and make sure to turn in the GitHub link into Google Classroom."""

# About File and Requirements

"""
Hogwarts Feedback Analysis

This Python script reads the "hogwarts.csv" file and performs some basic data analysis using the Pandas library.
The "hogwarts.csv" file contains user feedback for a Harry Potter game, including playtime and feedback sentiment.

Python version: 3.9.13
Author: Kain Mason
Date created: 03/03/2023"""

#IMPORT REQUIREMENTS

#import pandas as pd
#import matplotlib.pyplot as plt


# Start Of File

import pandas as pd
import matplotlib.pyplot as plt

# read the CSV file into a pandas dataframe
df = pd.read_csv("assets/hogwarts.csv")

# count the number of positive and negative feedback
feedback_count = df['Feedback'].value_counts()

# create a pie chart to show the percentage of positive and negative feedback
plt.pie(feedback_count, labels=feedback_count.index, autopct='%1.1f%%')
plt.title("Hogwarts Legacies: Positive vs Negative Feedback")
plt.show()
