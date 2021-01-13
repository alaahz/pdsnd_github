### Project Title
## _US Bikeshare Date Analysis Project_

### Date created
_**January 12, 2021.**_

### Description
In this project, Python will be used to explore data related to bike share systems for three major cities in the United.

- _Chicago_
- _New York City_
- _Washington_

The program  will ask a user to give input on which data they would like to see. Depending on a user's input, the program will compute and provide a useful information.


### Files used
- _Bikeshare_2.py_

## Softwares needed:
- Python 3, NumPy, and pandas installed using Anaconda.
- A text editor, like _[Sublime](https://www.sublimetext.com/)_ or _[Atom](https://atom.io/)_.
- A terminal application (Terminal on Mac and Linux or Cygwin on Windows).

### Credits
The following links help me to complete the program:

- [pandas](https://pandas.pydata.org/docs/reference/frame.html).
- [ Python- Built-in Exceptions](https://docs.python.org/3/library/exceptions.html#ValueError).
- [python-tabulate](https://pypi.org/project/tabulate/) _Udacity reviewer's suggestion_
- [Markdown Preview package](https://github.com/atom/markdown-preview).

## An Interactive Experience:

The program is set up as a script that takes in raw input to create an interactive experience in the terminal that answers questions about the dataset. The experience is interactive because depending on a user's input, the answers to the questions on the previous page will change! There are four questions that will change the answers:

- Would you like to see data for Chicago, New York, or Washington?
- Would you like to filter the data by month, day, both or not at all?
- (If they chose month) Which month - January, February, March, April, May, or June?
- (If they chose day) Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?

## The Datasets:
Randomly selected data for the first six months of 2017 are provided for all three cities. All three of the data files contain the same core six (6) columns:

- _Start Time (e.g., 2017-01-01 00:07:57)_
- _End Time (e.g., 2017-01-01 00:20:53)_
- _Trip Duration (in seconds - e.g., 776)_
- _Start Station (e.g., Broadway & Barry Ave)_
- _End Station (e.g., Sedgwick St & North Ave)_
- _User Type (Subscriber or Customer)_

**The Chicago and New York City files also have the following two columns:**
- _Gender_
- _Birth Year_

### Statistics Computed:
You will learn about bike share use in Chicago, New York City, and Washington by computing a variety of descriptive statistics. In this project, you'll write code to provide the following information:

##### Popular times of travel (i.e., occurs most often in the start time):
- _most common month._
- _most common day of week._
- _most common hour of day._

##### Popular stations and trip:
- _most common start station._
- _most common end station._
- _most common trip from start to end (i.e., most frequent combination of start station and end station)._

##### Trip duration:
- _total travel time._
- _average travel time._

##### User info:
- _counts of each user type._
- _counts of each gender **(only available for NYC and Chicago)** earliest, most recent, most common year of birth **(only available for NYC and Chicago).**_
