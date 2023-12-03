# Eva Tarr, 11234313, ELT783

from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
def dayTimeCreationAndScore():
    # File path can change to the dataset we want to work with
    file_path = "reddit-r-nonewnormal-dataset-comments.csv"

    allPosts = pd.read_csv(file_path, encoding='utf-8')                             # Read the csv file
    columns_cleaned = allPosts.dropna(axis=1, how='all')                            # Clean all empty comments out
    Posts_cleaned = columns_cleaned.dropna()                                        # Clean all empty rows out

    Posts_sorted = Posts_cleaned.sort_values(by='created_utc', ascending=True)      # Sort posts based on their creation dateTime

    hours = {}
    hoursNum = {}
    for i, row in Posts_sorted.iterrows():
        hour = str(datetime.utcfromtimestamp(row['created_utc']).hour)              # Get the hour in which the post was created
        if hour in hours:
            hours[hour] += row['score']
            hoursNum[hour] += 1
        else:
            hours[hour] = row['score']
            hoursNum[hour] = 1

    for hour in hours.keys():                                                        # Get the average score for each hour
        hours[hour] /= hoursNum[hour]

    hoursSorted = dict(sorted(hours.items(), key=lambda item: int(item[0])))        # Sort the hours dictionary based on the keys

    # Display the graph
    fig, leftAxis = plt.subplots(figsize=(20, 10))
    leftAxis.bar(hoursSorted.keys(), hoursSorted.values(), color='pink', label='Average Score')
    leftAxis.set_xlabel('Time Of Day')
    leftAxis.set_ylabel('Average Score', color='lightsteelblue')
    leftAxis.tick_params('y', colors='lightsteelblue')
    plt.xticks(rotation='vertical')
    plt.title("Hour of creation and the comment score")
    plt.show()

dayTimeCreationAndScore()
