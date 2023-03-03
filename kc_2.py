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
