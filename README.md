# Exercise 7: Plotting climate data in Python

This week we'll put together our data analysis and plotting skills using Pandas and Matplotlib to visualize the temperature data we have been exploring for the course thus far.
For each problem you will create or modify a Python script, then upload your files to GitHub.
The answers to the questions in this week's exercise should be given by modifying the document in places where asked or at the end of this document in the [section titled Answers](#answers).

- **Exercise 7 is due by 16:00 on 27.10.**
- Don't forget to check out [the hints for this week's exercise](https://geo-python.github.io/2017/lessons/L7/exercise-7-hints.html) if you're having trouble.
- Scores on this exercise are out of 20 points.

## Problem 0 - Creating the data file for this week (2 points)

Your first task in this exercise is to write out a file with the contents of the Pandas DataFrame(s) you produced in [Exercise 6](https://github.com/Geo-Python-2017/Exercise-6), Problems 3 and 4.
As described in [Lesson 5](https://geo-python.github.io/2017/lessons/L5/pandas-basic-operations.html#writing-data), data can be saved to a file in Pandas using `dataFrame.to_csv('file.csv, sep=',')`.
Start by creating one data file for the Helsinki temperature data (`helsinki.csv`) and a second for the Sodankylä data (`sodankyla.csv`).

## Problem 1 - Doing time, plotting temperatures (6 points)

In this first problem we'll work with using the datetime format for Pandas data, and creating a line plot of data from a file.
You should:

1. Load the Helsinki temperature data file produced above (`helsinki.csv`) into Pandas
2. Convert the `DATE_m` (or your equivalent date variable) column to the Pandas datetime format.
3. Set the `DATE_m` column as the DataFrame index
4. Make a line plot of temperatures in Celsius from 2010-2017.
    - The line should be a dashed black line with circles for the data points, and include a descriptive title and axis labels.

Save your Python script file as `temperature_plot.py` in GitHub and include a copy of the plot it produces in your answer to Problem 1 below.
More guidance on this problem can be found in [the hints for this week's exercise](https://geo-python.github.io/2017/lessons/L7/exercise-7-hints.html).

## Problem 2 - Seasonal temperature anomalies, visualized (6 points)

![img/Ex7-2.png](img/Ex7-2.png)<br/>
*The goal for this problem is to make this plot.*

For Problem 2, the goal is to recreate the plot above, a 4-panel plot showing seasonal temperature anomalies from 1953-2016.
To do this, you should:

1. Start by creating a new Python script called `anomaly_subplots.py` and performing steps 1-3 from Problem 1 to prepare the data for plotting.
2. Create a yearly Pandas datetime index from 1953-2016 using the `pd.date_range()` function.
3. Create an empty Pandas DataFrame called `seasonalData` using the index you just created and column titles 'Winter', 'Spring', 'Summer', and 'Fall'.
4. Fill the data frame with mean anomaly temperatures (calculated in Exercise 6) for each season in each year.
    - Assume that Winter is December-February, Spring is March-May, Summer is June-August, and Fall is September-November.
5. Create a figure with 4 subplots in the arrangement shown above, labeling axes as needed, with gridlines on, and with a line legend for each panel.
    - You can find tips about these different plot features in the [Matplotlib documentation](https://matplotlib.org/contents.html) and [the hints for this week's exercise](https://geo-python.github.io/2017/lessons/L7/exercise-7-hints.html).

Save your Python script in GitHub and include a copy of the plot it produces in your answer to Problem 2 below.

## Problem 3 - Seasonal temperature anomalies, animated (6 points)

![img/Ex7-2.png](img/Ex7-3.gif)<br/>
*The goal for this problem is to make this kind of animation.*

For Problem 3, the goal is to recreate **65 individual bar plots** that can be animated like the animation above that shows the variation in seasonal temperature anomalies
from 1953-2016.

To do this, you should:

1. Start by creating a new Python script called `anomaly_barplots.py`. You should use the same data as in Problem 2.
2. You should select data for each season of each year between 1953-2017 using the techniques that you have learned during the Lesson 7.
    - Assume that Winter is December-February, Spring is March-May, Summer is June-August, and Fall is September-November.
3. You should calculate the mean temperature of the **weather anomalies** (*outcome from Problem 3 in Exercise 6 last week*) based on the selected data for each season of the year. You should end up having altogether four values for each year (i.e. one for winter, spring, summer, and fall).
4. You should create a bar plot for each year using Pandas (altogether 65 plots) that visualizes the weather anomalies in a similar manner as in the animation above (notice that the y-scale is standardized).
5. Change the aesthetics of your plot: modify the colors of the bars (you can choose the colors yourself), and add a title, X-label (should be the year), and Y-label (you can use the same text as in the animation).
6. You should save each of those plots into an empty folder on your disk
7. (**optional**) After you have saved all those 65 plots into your disk, you can find information from [the hints for this week's exercise](https://geo-python.github.io/2017/lessons/L7/exercise-7-hints.html) on how to create an animation from those plots

Save your Python script in GitHub and include copies of the plots that you created **OR** the animation that was produced from those plots in your answer to Problem 3 below.

# Problem 4 (optional) - Comparing seasonal temperature anomalies, animated

In problem 4, which is an optional task, your aim is to create a similar animation as in Problem 3 but create a 2-panel plot (2 rows, 1 column) where the upper plot
visualizes the weather anomalies from Helsinki, and the lower visualizes the weather anomalies from **Sodankylä** (data from Problem 4 in Exercise 6 last week).

Write your codes into a separate script called `anomaly_bar_subplots.py`, and add your code and the animation to GitHub.

# Answers

## Problem 1 - Answers to questions

### 1. 
![](img/mavtemp.png)
### 2.
![](img/anomalysubplots.png)
### 3. 
![](img/Animation.gif)
### 4. 
![](img/Animation2.gif)




