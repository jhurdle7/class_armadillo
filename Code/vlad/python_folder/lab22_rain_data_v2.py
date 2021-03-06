# Lab22 Rain Data Version 2 https://github.com/PdxCodeGuild/class_armadillo/blob/master/1%20Python/labs/lab22-rain_data.md

"""
The 'City of Portland Bureau of Environmental Services' operates and maintains a network of rain gauges around Portland, and publishes their data publicly: http://or.water.usgs.gov/non-usgs/bes/

The data tables available on the site look something like...

Daily  Hourly data -->

   Date     Total    0   1
--------------------------
25-MAR-2016     0    0   0
24-MAR-2016     6    0   1
23-MAR-2016     -    -   -
MORE...

Download one of these files and write a function to load the file. The two columns that are most important are the date and the daily total. The simplest representation of this data is a list of tuples, but you may also use a list of dictionaries, or a list of instances of a custom class.

To parse the dates, use datetime.strptime. This allows for easy access to the year, month, and day as ints. Below I've shown how to parse an example string, resulting in a datetime object. We can then access the year, month, and day on that datetime as ints. Later, if you want to print the datetime in a more human-readable format, you can use datetime.strftime.

import datetime
date = datetime.datetime.strptime('25-MAR-2016', '%d-%b-%Y')
print(date.year)   # 2016
print(date.month)  # 3
print(date.day)    # 25
print(date)  # 2016-03-25 00:00:00
print(date.strftime('%d-%b-%Y'))  # 25-Mar-2016

Version 2

Now that you've successfully extracted the data, let's done some statistics.

1. Calculate the mean of the data:
mean

2. Use the mean to calculate the standard deviation, which is a measure of how "spread out" the data is:
standard_deviation

68.2% of the data falls within 1 standard deviation of the mean.

bell_curve

3. Find the day which had the most rain.
4. Find the year which had the most rain on average.

"""

import string
import requests
import re
import math
import datetime
import random
import statistics 
# from datetime import datetime

response = requests.get('https://or.water.usgs.gov/non-usgs/bes/hayden_island.rain')
rain_data = response.text

# find all the matching phone numbers
date_and_daily_total = r'(\d+-\w+-\d+)\s+(\d+)' # expression 
results = re.findall(date_and_daily_total, rain_data) # this is making a list of Tuples

# use the starter code from the lab22 to make it it string dates to be intergers to be  
# from datetime import datetime # I have this like at the time comment here so it does not repeat

# use a for loop to go to each of the dates and change into change it into numbers into an interger and to change from tuple to a list
rain_data_dict = {} # use this empty dictionry
for rain in results:
   rain = list(rain) # this will change from tuple to a list because Tuples can't be edited or change vaalues 
   # print(type(rain))
# turn a string into a datetime object
   rain[0] = datetime.datetime.strptime(rain[0], '%d-%b-%Y') # this is to get to the first element of the list
   rain[1] = int(rain[1]) # turning string into interger to change the second value from a string to an interger to add it later
   rain_data_dict.update({rain[0]:rain[1]}) # the key is the  date and the value is how much rain has fallen 
# print(rain_data_dict)


# access the properties of that object
#print(type(rain_data_dict[0].year))   # LEArn how to use this print version
# print(rain_data.month)  # 3
# print(rain_data.day)    # 25
# print(rain_data)  # 2016-03-25 00:00:00

# turn the datetime object back into a string
# print(rain_data.strftime('%d-%b-%Y'))  # 25-Mar-2016

# # I need to make the daily total to be an interger so I can take the average of them 
# also I need to clean the data ask what else do I need to do to clean this data

# import random
# import math


""" use the following functions below to get version number 2 mean, variance and 
standard_deviation """

#function to get the mean: 
# https://en.wikipedia.org/wiki/Arithmetic_mean

def mean(rain_data_dict):
   total = 0
   for key, value in rain_data_dict.items(): # we need this logic to get inside the key or value pair in a dictionary 
      # print(value)
      total += value
   return total / len(rain_data_dict) # get inside the dictionary to get the value of the years

average = mean(rain_data_dict)
print(average) # 9.604221969409682


# function to get the Variance: 
# https://en.wikipedia.org/wiki/Variance

def variance(rain_data_dict, average):
   #  average = mean(rain_data_dict) I do not need this because I passed as a argument from the mean function above
   total = 0
   for key, value in rain_data_dict.items():
      total += (value - average) ** 2
   return total / len(rain_data_dict)

variances = variance(rain_data_dict, average)
print(variances) # 481.5039589162603


# function to get the standard_deviation: 
# https://en.wikipedia.org/wiki/Standard_deviation

def standard_deviation(variances):
   return math.sqrt(variances)
deviations = standard_deviation(variances)

# nums = [random.randint(1, 99) for _ in range(100)]
print(f'The mean is {average}') # 9.604221969409682
print(f'The variance is {variances}') #481.5039589162603
print(f'The standard deviation is {deviations}') #21.943198465954325










# instructor started code to do it using the entire site: 

# import requests
# import re

# # use string operations to parse the rain file

# response = requests.get('https://or.water.usgs.gov/non-usgs/bes/skyline_school.rain')
# # print(response.text)
# lines = response.text.split('\n')
# lines = lines[11:] # chop off the junk at the start
# for line in lines:
#     print(line.split())


# # or use regular expressions
# # https://regex101.com/r/QwMfRM/1



# # get all the rain data on the site
# def get_rain_file_urls():
#     response = requests.get('https://or.water.usgs.gov/non-usgs/bes/')
#     text = response.text
#     rain_files = re.findall(r'\w+\.rain', text)
#     rain_files = ['https://or.water.usgs.gov/non-usgs/bes/' + rain_file for rain_file in rain_files]
#     return rain_files

# def get_rain_data(url):
#     # your code here
#     print(url)
#     pass

# rain_file_urls = get_rain_file_urls()
# for rain_file_url in rain_file_urls:
#     data = get_rain_data(rain_file_url)
#     print(data)

# exit()