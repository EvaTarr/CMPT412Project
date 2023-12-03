# Eva Tarr, 11234313, ELT783

from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
def timeOfCreationAndScore():
    # File path can change to the dataset we want to work with
    file_path = "reddit-r-nonewnormal-dataset-comments.csv"
    allPosts = pd.read_csv(file_path, encoding='utf-8')                         # Read the file
    columns_cleaned = allPosts.dropna(axis=1, how='all')                        # Remove all empty columns
    Posts_cleaned = columns_cleaned.dropna()                                    # remove all empty rows
    Posts_sorted = Posts_cleaned.sort_values(by='created_utc', ascending=True)  # Sort based on the time of creation

    months = {}
    monthsNum = {}
    for i, row in Posts_sorted.iterrows():
        monthName = str(datetime.utcfromtimestamp(row['created_utc']).month) + str(datetime.utcfromtimestamp(row['created_utc']).year)
        if monthName in months:
            months[monthName] += row['score']
            monthsNum[monthName] += 1
        else:
            months[monthName] = row['score']
            monthsNum[monthName] = 1

    for month in months.keys():                       # Get the average score of all comments
        months[month] /= monthsNum[month]

    # Show graph
    fig, leftAxis = plt.subplots(figsize=(20, 10))
    leftAxis.bar(months.keys(), months.values(), color='lightsteelblue', label='Average Score')
    leftAxis.set_xlabel('Month and Year')
    leftAxis.set_ylabel('Average Score', color='lightsteelblue')
    leftAxis.tick_params('y', colors='lightsteelblue')
    plt.xticks(rotation='vertical')
    plt.title("Time of creation and the comment score")
    plt.show()


timeOfCreationAndScore()
