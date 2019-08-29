{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 2016 US Bike Share Activity Snapshot\n",
    "\n",
    "## Table of Contents\n",
    "- [Introduction](#intro)\n",
    "- [Posing Questions](#pose_questions)\n",
    "- [Data Collection and Wrangling](#wrangling)\n",
    "  - [Condensing the Trip Data](#condensing)\n",
    "- [Exploratory Data Analysis](#eda)\n",
    "  - [Statistics](#statistics)\n",
    "  - [Visualizations](#visualizations)\n",
    "- [Performing Your Own Analysis](#eda_continued)\n",
    "- [Conclusions](#conclusions)\n",
    "\n",
    "<a id='intro'></a>\n",
    "## Introduction\n",
    "\n",
    "Over the past decade, bicycle-sharing systems have been growing in number and popularity in cities across the world. Bicycle-sharing systems allow users to rent bicycles for short trips, typically 30 minutes or less. Thanks to the rise in information technologies, it is easy for a user of the system to access a dock within the system to unlock or return bicycles. These technologies also provide a wealth of data that can be used to explore how these bike-sharing systems are used.\n",
    "\n",
    "In this project, you will perform an exploratory analysis on data provided by [Motivate](https://www.motivateco.com/), a bike-share system provider for many major cities in the United States. You will compare the system usage between three large cities: New York City, Chicago, and Washington, DC. You will also see if there are any differences within each system for those users that are registered, regular users and those users that are short-term, casual users."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<a id='pose_questions'></a>\n",
    "## Posing Questions\n",
    "\n",
    "Before looking at the bike sharing data, you should start by asking questions you might want to understand about the bike share data. Consider, for example, if you were working for Motivate. What kinds of information would you want to know about in order to make smarter business decisions? If you were a user of the bike-share service, what factors might influence how you would want to use the service?\n",
    "\n",
    "**Question 1**: Write at least two questions related to bike sharing that you think could be answered by data.\n",
    "\n",
    "**Answer**: \n",
    "1)Busy hour and Busy day in a week.\n",
    "\n",
    "2)How subcriber are performing againsts customers.\n",
    "\n",
    "3)How subcriber or customers driving the bikes.\n",
    "\n",
    "4)How duration of the customers vs subcribers.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<a id='wrangling'></a>\n",
    "## Data Collection and Wrangling\n",
    "\n",
    "Now it's time to collect and explore our data. In this project, we will focus on the record of individual trips taken in 2016 from our selected cities: New York City, Chicago, and Washington, DC. Each of these cities has a page where we can freely download the trip data.:\n",
    "\n",
    "- New York City (Citi Bike): [Link](https://www.citibikenyc.com/system-data)\n",
    "- Chicago (Divvy): [Link](https://www.divvybikes.com/system-data)\n",
    "- Washington, DC (Capital Bikeshare): [Link](https://www.capitalbikeshare.com/system-data)\n",
    "\n",
    "If you visit these pages, you will notice that each city has a different way of delivering its data. Chicago updates with new data twice a year, Washington DC is quarterly, and New York City is monthly. **However, you do not need to download the data yourself.** The data has already been collected for you in the `/data/` folder of the project files. While the original data for 2016 is spread among multiple files for each city, the files in the `/data/` folder collect all of the trip data for the year into one file per city. Some data wrangling of inconsistencies in timestamp format within each city has already been performed for you. In addition, a random 2% sample of the original data is taken to make the exploration more manageable. \n",
    "\n",
    "**Question 2**: However, there is still a lot of data for us to investigate, so it's a good idea to start off by looking at one entry from each of the cities we're going to analyze. Run the first code cell below to load some packages and functions that you'll be using in your analysis. Then, complete the second code cell to print out the first trip recorded from each of the cities (the second line of each data file).\n",
    "\n",
    "**Answer:**\n",
    "\n",
    "City: NYC\n",
    "OrderedDict([('tripduration', '839'),\n",
    "             ('starttime', '1/1/2016 00:09:55'),\n",
    "             ('stoptime', '1/1/2016 00:23:54'),\n",
    "             ('start station id', '532'),\n",
    "             ('start station name', 'S 5 Pl & S 4 St'),\n",
    "             ('start station latitude', '40.710451'),\n",
    "             ('start station longitude', '-73.960876'),\n",
    "             ('end station id', '401'),\n",
    "             ('end station name', 'Allen St & Rivington St'),\n",
    "             ('end station latitude', '40.72019576'),\n",
    "             ('end station longitude', '-73.98997825'),\n",
    "             ('bikeid', '17109'),\n",
    "             ('usertype', 'Customer'),\n",
    "             ('birth year', ''),\n",
    "             ('gender', '0')])\n",
    "\n",
    "City: Chicago\n",
    "OrderedDict([('trip_id', '9080545'),\n",
    "             ('starttime', '3/31/2016 23:30'),\n",
    "             ('stoptime', '3/31/2016 23:46'),\n",
    "             ('bikeid', '2295'),\n",
    "             ('tripduration', '926'),\n",
    "             ('from_station_id', '156'),\n",
    "             ('from_station_name', 'Clark St & Wellington Ave'),\n",
    "             ('to_station_id', '166'),\n",
    "             ('to_station_name', 'Ashland Ave & Wrightwood Ave'),\n",
    "             ('usertype', 'Subscriber'),\n",
    "             ('gender', 'Male'),\n",
    "             ('birthyear', '1990')])\n",
    "\n",
    "City: Washington\n",
    "OrderedDict([('Duration (ms)', '427387'),\n",
    "             ('Start date', '3/31/2016 22:57'),\n",
    "             ('End date', '3/31/2016 23:04'),\n",
    "             ('Start station number', '31602'),\n",
    "             ('Start station', 'Park Rd & Holmead Pl NW'),\n",
    "             ('End station number', '31207'),\n",
    "             ('End station', 'Georgia Ave and Fairmont St NW'),\n",
    "             ('Bike number', 'W20842'),\n",
    "             ('Member Type', 'Registered')])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "## import all necessary packages and functions.\n",
    "import csv # read and write csv files\n",
    "from datetime import datetime # operations to parse dates\n",
    "from pprint import pprint # use to print data structures like dictionaries in\n",
    "                          # a nicer way than the base print function.\n",
    "import pandas\n",
    "import numpy\n",
    "import matplotlib"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "City: NYC\n",
      "OrderedDict([('tripduration', '839'),\n",
      "             ('starttime', '1/1/2016 00:09:55'),\n",
      "             ('stoptime', '1/1/2016 00:23:54'),\n",
      "             ('start station id', '532'),\n",
      "             ('start station name', 'S 5 Pl & S 4 St'),\n",
      "             ('start station latitude', '40.710451'),\n",
      "             ('start station longitude', '-73.960876'),\n",
      "             ('end station id', '401'),\n",
      "             ('end station name', 'Allen St & Rivington St'),\n",
      "             ('end station latitude', '40.72019576'),\n",
      "             ('end station longitude', '-73.98997825'),\n",
      "             ('bikeid', '17109'),\n",
      "             ('usertype', 'Customer'),\n",
      "             ('birth year', ''),\n",
      "             ('gender', '0')])\n",
      "\n",
      "City: Chicago\n",
      "OrderedDict([('trip_id', '9080545'),\n",
      "             ('starttime', '3/31/2016 23:30'),\n",
      "             ('stoptime', '3/31/2016 23:46'),\n",
      "             ('bikeid', '2295'),\n",
      "             ('tripduration', '926'),\n",
      "             ('from_station_id', '156'),\n",
      "             ('from_station_name', 'Clark St & Wellington Ave'),\n",
      "             ('to_station_id', '166'),\n",
      "             ('to_station_name', 'Ashland Ave & Wrightwood Ave'),\n",
      "             ('usertype', 'Subscriber'),\n",
      "             ('gender', 'Male'),\n",
      "             ('birthyear', '1990')])\n",
      "\n",
      "City: Washington\n",
      "OrderedDict([('Duration (ms)', '427387'),\n",
      "             ('Start date', '3/31/2016 22:57'),\n",
      "             ('End date', '3/31/2016 23:04'),\n",
      "             ('Start station number', '31602'),\n",
      "             ('Start station', 'Park Rd & Holmead Pl NW'),\n",
      "             ('End station number', '31207'),\n",
      "             ('End station', 'Georgia Ave and Fairmont St NW'),\n",
      "             ('Bike number', 'W20842'),\n",
      "             ('Member Type', 'Registered')])\n"
     ]
    }
   ],
   "source": [
    "def print_first_point(filename):\n",
    "    \"\"\"\n",
    "    This function prints and returns the first data point (second row) from\n",
    "    a csv file that includes a header row.\n",
    "    \"\"\"\n",
    "    # print city name for reference\n",
    "    city = filename.split('-')[0].split('/')[-1]\n",
    "    print('\\nCity: {}'.format(city))\n",
    "    \n",
    "    with open(filename, 'r') as f_in:\n",
    "        ## TODO: Use the csv library to set up a DictReader object. ##\n",
    "        ## see https://docs.python.org/3/library/csv.html           ##\n",
    "        trip_reader = csv.DictReader(f_in)\n",
    "        \n",
    "        ## TODO: Use a function on the DictReader object to read the     ##\n",
    "        ## first trip from the data file and store it in a variable.     ##\n",
    "        ## see https://docs.python.org/3/library/csv.html#reader-objects ##\n",
    "        first_trip = next(trip_reader)\n",
    "        \n",
    "        ## TODO: Use the pprint library to print the first trip. ##\n",
    "        ## see https://docs.python.org/3/library/pprint.html     ##\n",
    "        pprint(first_trip)\n",
    "    # output city name and first trip for later testing\n",
    "    return (city, first_trip)\n",
    "\n",
    "# list of files for each city\n",
    "data_files = ['./data/NYC-CitiBike-2016.csv',\n",
    "              './data/Chicago-Divvy-2016.csv',\n",
    "              './data/Washington-CapitalBikeshare-2016.csv',]\n",
    "\n",
    "# print the first trip from each file, store in dictionary\n",
    "example_trips = {}\n",
    "for data_file in data_files:\n",
    "    city, first_trip = print_first_point(data_file)\n",
    "    example_trips[city] = first_trip"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "If everything has been filled out correctly, you should see below the printout of each city name (which has been parsed from the data file name) that the first trip has been parsed in the form of a dictionary. When you set up a `DictReader` object, the first row of the data file is normally interpreted as column names. Every other row in the data file will use those column names as keys, as a dictionary is generated for each row.\n",
    "\n",
    "This will be useful since we can refer to quantities by an easily-understandable label instead of just a numeric index. For example, if we have a trip stored in the variable `row`, then we would rather get the trip duration from `row['duration']` instead of `row[0]`.\n",
    "\n",
    "<a id='condensing'></a>\n",
    "### Condensing the Trip Data\n",
    "\n",
    "It should also be observable from the above printout that each city provides different information. Even where the information is the same, the column names and formats are sometimes different. To make things as simple as possible when we get to the actual exploration, we should trim and clean the data. Cleaning the data makes sure that the data formats across the cities are consistent, while trimming focuses only on the parts of the data we are most interested in to make the exploration easier to work with.\n",
    "\n",
    "You will generate new data files with five values of interest for each trip: trip duration, starting month, starting hour, day of the week, and user type. Each of these may require additional wrangling depending on the city:\n",
    "\n",
    "- **Duration**: This has been given to us in seconds (New York, Chicago) or milliseconds (Washington). A more natural unit of analysis will be if all the trip durations are given in terms of minutes.\n",
    "- **Month**, **Hour**, **Day of Week**: Ridership volume is likely to change based on the season, time of day, and whether it is a weekday or weekend. Use the start time of the trip to obtain these values. The New York City data includes the seconds in their timestamps, while Washington and Chicago do not. The [`datetime`](https://docs.python.org/3/library/datetime.html) package will be very useful here to make the needed conversions.\n",
    "- **User Type**: It is possible that users who are subscribed to a bike-share system will have different patterns of use compared to users who only have temporary passes. Washington divides its users into two types: 'Registered' for users with annual, monthly, and other longer-term subscriptions, and 'Casual', for users with 24-hour, 3-day, and other short-term passes. The New York and Chicago data uses 'Subscriber' and 'Customer' for these groups, respectively. For consistency, you will convert the Washington labels to match the other two.\n",
    "\n",
    "\n",
    "**Question 3a**: Complete the helper functions in the code cells below to address each of the cleaning tasks described above.\n",
    "\n",
    "**Answer:**\n",
    "City: Washington\n",
    "OrderedDict([('duration', '7.123116666666666'),\n",
    "             ('month', '3'),\n",
    "             ('hour', '22'),\n",
    "             ('day_of_week', 'Thursday'),\n",
    "             ('user_type', 'Subscriber')])\n",
    "\n",
    "City: Chicago\n",
    "OrderedDict([('duration', '15.433333333333334'),\n",
    "             ('month', '3'),\n",
    "             ('hour', '23'),\n",
    "             ('day_of_week', 'Thursday'),\n",
    "             ('user_type', 'Subscriber')])\n",
    "\n",
    "City: NYC\n",
    "OrderedDict([('duration', '13.983333333333333'),\n",
    "             ('month', '1'),\n",
    "             ('hour', '0'),\n",
    "             ('day_of_week', 'Friday'),\n",
    "             ('user_type', 'Customer')])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "def duration_in_mins(datum, city):\n",
    "\n",
    "    if city=='NYC':\n",
    "        duration=int(datum['tripduration'])/60\n",
    "    elif city=='Chicago':\n",
    "        duration=int(datum['tripduration'])/60\n",
    "    else:\n",
    "        duration=(int(datum['Duration (ms)'])/1000)/60\n",
    "    \n",
    "    return duration\n",
    "\n",
    "\n",
    "# Some tests to check that your code works. There should be no output if all of\n",
    "# the assertions pass. The `example_trips` dictionary was obtained from when\n",
    "# you printed the first trip from each of the original data files.\n",
    "tests = {'NYC': 13.9833,\n",
    "         'Chicago': 15.4333,\n",
    "         'Washington': 7.1231}\n",
    "\n",
    "for city in tests:\n",
    "    assert abs(duration_in_mins(example_trips[city], city) - tests[city]) < .001"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "def time_of_trip(datum, city):\n",
    "    \"\"\"\n",
    "    Takes as input a dictionary containing info about a single trip (datum) and\n",
    "    its origin city (city) and returns the month, hour, and day of the week in\n",
    "    which the trip was made.\n",
    "    \n",
    "    Remember that NYC includes seconds, while Washington and Chicago do not.\n",
    "    \n",
    "    HINT: You should use the datetime module to parse the original date\n",
    "    strings into a format that is useful for extracting the desired information.\n",
    "    see https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior\n",
    "    \"\"\"\n",
    "    if city=='NYC':\n",
    "        extdt=datetime.strptime(datum['starttime'], \"%m/%d/%Y %H:%M:%S\")\n",
    "        month=int(extdt.strftime(\"%m\"))\n",
    "        hour=int(extdt.strftime(\"%H\"))\n",
    "        day_of_week=extdt.strftime(\"%A\")\n",
    "        #print(month,hour,day_of_week)\n",
    "    elif city=='Chicago':\n",
    "        extdt=datetime.strptime(datum['starttime'], \"%m/%d/%Y %H:%M\")\n",
    "        month=int(extdt.strftime(\"%m\"))\n",
    "        hour=int(extdt.strftime(\"%H\"))\n",
    "        day_of_week=extdt.strftime(\"%A\")\n",
    "        #print(month,hour,day_of_week)\n",
    "    else:\n",
    "        extdt=datetime.strptime(datum['Start date'], \"%m/%d/%Y %H:%M\")\n",
    "        month=int(extdt.strftime(\"%m\"))\n",
    "        hour=int(extdt.strftime(\"%H\"))\n",
    "        day_of_week=extdt.strftime(\"%A\")\n",
    "        #print(month,hour,day_of_week)\n",
    "    \n",
    "    return (month, hour, day_of_week)\n",
    "\n",
    "\n",
    "# Some tests to check that your code works. There should be no output if all of\n",
    "# the assertions pass. The `example_trips` dictionary was obtained from when\n",
    "# you printed the first trip from each of the original data files.\n",
    "tests = {'NYC': (1, 0, 'Friday'),\n",
    "         'Chicago': (3, 23, 'Thursday'),\n",
    "         'Washington': (3, 22, 'Thursday')}\n",
    "\n",
    "for city in tests:\n",
    "    assert time_of_trip(example_trips[city], city) == tests[city]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "def type_of_user(datum, city):\n",
    "    \"\"\"\n",
    "    Takes as input a dictionary containing info about a single trip (datum) and\n",
    "    its origin city (city) and returns the type of system user that made the\n",
    "    trip.\n",
    "    \n",
    "    Remember that Washington has different category names compared to Chicago\n",
    "    and NYC. \n",
    "    \"\"\"\n",
    "    \n",
    "    if city=='NYC':\n",
    "        user_type=datum['usertype']\n",
    "    elif city=='Chicago':\n",
    "        user_type=datum['usertype']\n",
    "    else:\n",
    "        if datum['Member Type']=='Registered':\n",
    "            user_type='Subscriber'\n",
    "        else:\n",
    "            user_type='Customer'\n",
    "    \n",
    "    return user_type\n",
    "\n",
    "\n",
    "# Some tests to check that your code works. There should be no output if all of\n",
    "# the assertions pass. The `example_trips` dictionary was obtained from when\n",
    "# you printed the first trip from each of the original data files.\n",
    "tests = {'NYC': 'Customer',\n",
    "         'Chicago': 'Subscriber',\n",
    "         'Washington': 'Subscriber'}\n",
    "\n",
    "for city in tests:\n",
    "    assert type_of_user(example_trips[city], city) == tests[city]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Question 3b**: Now, use the helper functions you wrote above to create a condensed data file for each city consisting only of the data fields indicated above. In the `/examples/` folder, you will see an example datafile from the [Bay Area Bike Share](http://www.bayareabikeshare.com/open-data) before and after conversion. Make sure that your output is formatted to be consistent with the example file.\n",
    "\n",
    "**Answer**\n",
    "City: Washington\n",
    "OrderedDict([('duration', '7.123116666666666'),\n",
    "             ('month', '3'),\n",
    "             ('hour', '22'),\n",
    "             ('day_of_week', 'Thursday'),\n",
    "             ('user_type', 'Subscriber')])\n",
    "\n",
    "City: Chicago\n",
    "OrderedDict([('duration', '15.433333333333334'),\n",
    "             ('month', '3'),\n",
    "             ('hour', '23'),\n",
    "             ('day_of_week', 'Thursday'),\n",
    "             ('user_type', 'Subscriber')])\n",
    "\n",
    "City: NYC\n",
    "OrderedDict([('duration', '13.983333333333333'),\n",
    "             ('month', '1'),\n",
    "             ('hour', '0'),\n",
    "             ('day_of_week', 'Friday'),\n",
    "             ('user_type', 'Customer')])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "def condense_data(in_file, out_file, city):\n",
    "    \"\"\"\n",
    "    This function takes full data from the specified input file\n",
    "    and writes the condensed data to a specified output file. The city\n",
    "    argument determines how the input file will be parsed.\n",
    "    \n",
    "    HINT: See the cell below to see how the arguments are structured!\n",
    "    \"\"\"\n",
    "    \n",
    "    with open(out_file, 'w') as f_out, open(in_file, 'r') as f_in:\n",
    "        # set up csv DictWriter object - writer requires column names for the\n",
    "        # first row as the \"fieldnames\" argument\n",
    "        out_colnames = ['duration', 'month', 'hour', 'day_of_week', 'user_type']        \n",
    "        trip_writer = csv.DictWriter(f_out, fieldnames = out_colnames)\n",
    "        trip_writer.writeheader()\n",
    "        \n",
    "        ## TODO: set up csv DictReader object ##\n",
    "        trip_reader = csv.DictReader(f_in)\n",
    "\n",
    "        # collect data from and process each row\n",
    "        for row in trip_reader:\n",
    "            # set up a dictionary to hold the values for the cleaned and trimmed\n",
    "            # data point\n",
    "            new_point = {}\n",
    "            \n",
    "\n",
    "            ## TODO: use the helper functions to get the cleaned data from  ##\n",
    "            ## the original data dictionaries.                              ##\n",
    "            ## Note that the keys for the new_point dictionary should match ##\n",
    "            ## the column names set in the DictWriter object above.         ##\n",
    "            month, hour, day_of_week = time_of_trip(row, city)\n",
    "            duration=duration_in_mins(row, city)\n",
    "            user_type=type_of_user(row, city)\n",
    "            new_point[out_colnames[0]]=duration\n",
    "            new_point[out_colnames[1]]=month\n",
    "            new_point[out_colnames[2]]=hour\n",
    "            new_point[out_colnames[3]]=day_of_week\n",
    "            new_point[out_colnames[4]]=user_type\n",
    "\n",
    "            ## TODO: write the processed information to the output file.     ##\n",
    "            ## see https://docs.python.org/3/library/csv.html#writer-objects ##\n",
    "            trip_writer.writerow(new_point)\n",
    "            "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "City: Washington\n",
      "OrderedDict([('duration', '7.123116666666666'),\n",
      "             ('month', '3'),\n",
      "             ('hour', '22'),\n",
      "             ('day_of_week', 'Thursday'),\n",
      "             ('user_type', 'Subscriber')])\n",
      "\n",
      "City: Chicago\n",
      "OrderedDict([('duration', '15.433333333333334'),\n",
      "             ('month', '3'),\n",
      "             ('hour', '23'),\n",
      "             ('day_of_week', 'Thursday'),\n",
      "             ('user_type', 'Subscriber')])\n",
      "\n",
      "City: NYC\n",
      "OrderedDict([('duration', '13.983333333333333'),\n",
      "             ('month', '1'),\n",
      "             ('hour', '0'),\n",
      "             ('day_of_week', 'Friday'),\n",
      "             ('user_type', 'Customer')])\n"
     ]
    }
   ],
   "source": [
    "# Run this cell to check your work\n",
    "city_info = {'Washington': {'in_file': './data/Washington-CapitalBikeshare-2016.csv',\n",
    "                            'out_file': './data/Washington-2016-Summary.csv'},\n",
    "             'Chicago': {'in_file': './data/Chicago-Divvy-2016.csv',\n",
    "                         'out_file': './data/Chicago-2016-Summary.csv'},\n",
    "             'NYC': {'in_file': './data/NYC-CitiBike-2016.csv',\n",
    "                     'out_file': './data/NYC-2016-Summary.csv'}}\n",
    "\n",
    "for city, filenames in city_info.items():\n",
    "    condense_data(filenames['in_file'], filenames['out_file'], city)\n",
    "    print_first_point(filenames['out_file'])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "> **Tip**: If you save a jupyter Notebook, the output from running code blocks will also be saved. However, the state of your workspace will be reset once a new session is started. Make sure that you run all of the necessary code blocks from your previous session to reestablish variables and functions before picking up where you last left off.\n",
    "\n",
    "<a id='eda'></a>\n",
    "## Exploratory Data Analysis\n",
    "\n",
    "Now that you have the data collected and wrangled, you're ready to start exploring the data. In this section you will write some code to compute descriptive statistics from the data. You will also be introduced to the `matplotlib` library to create some basic histograms of the data.\n",
    "\n",
    "<a id='statistics'></a>\n",
    "### Statistics\n",
    "\n",
    "First, let's compute some basic counts. The first cell below contains a function that uses the csv module to iterate through a provided data file, returning the number of trips made by subscribers and customers. The second cell runs this function on the example Bay Area data in the `/examples/` folder. Modify the cells to answer the question below.\n",
    "\n",
    "**Question 4a**: Which city has the highest number of trips? Which city has the highest proportion of trips made by subscribers? Which city has the highest proportion of trips made by short-term customers?\n",
    "\n",
    "**Answer**: \n",
    "Results:\n",
    "================================================================\n",
    "City: NYC \n",
    "\n",
    "{'n_subscribers': 245896, 'n_customers': 30902, 'n_total': 276798, 'sub_ratio': 88.83590199351151, 'cust_ratio': 11.164098006488485}\n",
    "\n",
    "City: Chicago \n",
    "\n",
    "{'n_subscribers': 54982, 'n_customers': 17149, 'n_total': 72131, 'sub_ratio': 76.22520136973007, 'cust_ratio': 23.774798630269924}\n",
    "\n",
    "City: Washington \n",
    "\n",
    "{'n_subscribers': 51753, 'n_customers': 14573, 'n_total': 66326, 'sub_ratio': 78.0282242257938, 'cust_ratio': 21.971775774206193}\n",
    "\n",
    "=========================================================================================================================\n",
    "\n",
    "1. Number of trips made by NYC is 276,798, Chicago is 72,131 and Washington is 66,326. So highest number of trips is made by NYC City.\n",
    "\n",
    "2. Number of subscribers in NYC is 245,896 leading to percentage of trips made by subscribers is 88.84%, Chicago is 54,982 leading to percentage of trips made by subscribers is 76.23% and Washington is 51,753 leading to percentage of trips made by subscribers is 78.03%. So NYC city has highest proportion of trips made by subscribers\n",
    "\n",
    "3. Number of customers in NYC is 30,902 leading to percentage of trips made by customers is 11.16%, Chicago is 17,149 leading to percentage of trips made by customers is 23.77% and Washington is 14,573 leading to percentage of trips made by customers is 21.97%. So Chicago city has highest proportion of trips made by subscribers\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "def number_of_trips(filename):\n",
    "    \"\"\"\n",
    "    This function reads in a file with trip data and reports the number of\n",
    "    trips made by subscribers, customers, and total overall.\n",
    "    \"\"\"\n",
    "    with open(filename, 'r') as f_in:\n",
    "        # set up csv reader object\n",
    "        reader = csv.DictReader(f_in)\n",
    "        \n",
    "        # initialize count variables\n",
    "        n_subscribers = 0\n",
    "        n_customers = 0\n",
    "        \n",
    "        # tally up ride types\n",
    "        for row in reader:\n",
    "            if row['user_type'] == 'Subscriber':\n",
    "                n_subscribers += 1\n",
    "            else:\n",
    "                n_customers += 1\n",
    "        \n",
    "        # compute total number of rides\n",
    "        n_total = n_subscribers + n_customers\n",
    "        \n",
    "        # return tallies as a tuple\n",
    "        return(n_subscribers, n_customers, n_total)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "City: NYC \n",
      "\n",
      "{'n_subscribers': 245896, 'n_customers': 30902, 'n_total': 276798, 'sub_ratio': 88.83590199351151, 'cust_ratio': 11.164098006488485}\n",
      "City: Chicago \n",
      "\n",
      "{'n_subscribers': 54982, 'n_customers': 17149, 'n_total': 72131, 'sub_ratio': 76.22520136973007, 'cust_ratio': 23.774798630269924}\n",
      "City: Washington \n",
      "\n",
      "{'n_subscribers': 51753, 'n_customers': 14573, 'n_total': 66326, 'sub_ratio': 78.0282242257938, 'cust_ratio': 21.971775774206193}\n"
     ]
    }
   ],
   "source": [
    "## Modify this and the previous cell to answer Question 4a. Remember to run ##\n",
    "## the function on the cleaned data files you created from Question 3.      ##\n",
    "\n",
    "nycflpth='./data/NYC-2016-Summary.csv'\n",
    "chiflpth='./data/Chicago-2016-Summary.csv' \n",
    "wasflpth='./data/Washington-2016-Summary.csv'\n",
    "n_subscribers, n_customers, n_total=number_of_trips(nycflpth)\n",
    "nyc_out= {}\n",
    "nyc_out['n_subscribers']=n_subscribers\n",
    "nyc_out['n_customers']=n_customers\n",
    "nyc_out['n_total']=n_total\n",
    "nyc_out['sub_ratio']=(float(n_subscribers)/n_total)*100\n",
    "nyc_out['cust_ratio']=(float(n_customers)/n_total)*100\n",
    "print('City: NYC \\n')\n",
    "print(nyc_out)\n",
    "n_subscribers, n_customers, n_total=number_of_trips(chiflpth)\n",
    "chi_out= {}\n",
    "chi_out['n_subscribers']=n_subscribers\n",
    "chi_out['n_customers']=n_customers\n",
    "chi_out['n_total']=n_total\n",
    "chi_out['sub_ratio']=(float(n_subscribers)/n_total)*100\n",
    "chi_out['cust_ratio']=(float(n_customers)/n_total)*100\n",
    "print('City: Chicago \\n')\n",
    "print(chi_out)\n",
    "n_subscribers, n_customers, n_total=number_of_trips(wasflpth)\n",
    "was_out= {}\n",
    "was_out['n_subscribers']=n_subscribers\n",
    "was_out['n_customers']=n_customers\n",
    "was_out['n_total']=n_total\n",
    "was_out['sub_ratio']=(float(n_subscribers)/n_total)*100\n",
    "was_out['cust_ratio']=(float(n_customers)/n_total)*100\n",
    "print('City: Washington \\n')\n",
    "print(was_out)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now, you will write your own code to continue investigating properties of the data.\n",
    "\n",
    "**Question 4b**: Bike-share systems are designed for riders to take short trips. Most of the time, users are allowed to take trips of 30 minutes or less with no additional charges, with overage charges made for trips of longer than that duration. What is the average trip length for each city? What proportion of rides made in each city are longer than 30 minutes?\n",
    "\n",
    "**Answer**: average trip length for NYC is 15.812, Chicago is 16.564 and Washimgton is 18.933. Proportion of rides made in each city are longer than 30 minutes are NYC is 7.302%, Chicago is 8.332% and Washimgton is 10.8388%"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'path': './data/NYC-2016-Summary.csv', 'average_travel': 15.812592998022623, 'proportion_overtime': 7.3024371563378345}\n",
      "{'path': './data/Chicago-2016-Summary.csv', 'average_travel': 16.563629368787343, 'proportion_overtime': 8.332062497400562}\n",
      "{'path': './data/Washington-2016-Summary.csv', 'average_travel': 18.93287355913719, 'proportion_overtime': 10.83888671109369}\n"
     ]
    }
   ],
   "source": [
    "## Use this and additional cells to answer Question 4b.                 ##\n",
    "##                                                                      ##\n",
    "## HINT: The csv module reads in all of the data as strings, including  ##\n",
    "## numeric values. You will need a function to convert the strings      ##\n",
    "## into an appropriate numeric type before you aggregate data.          ##\n",
    "## TIP: For the Bay Area example, the average trip length is 14 minutes ##\n",
    "## and 3.5% of trips are longer than 30 minutes.                        ##\n",
    "\n",
    "def trip_durat_cal(filenm):\n",
    "    data_dur = pandas.read_csv(filenm)\n",
    "    avgr = numpy.average(data_dur['duration'])\n",
    "    rid_gt30 = (len(data_dur[data_dur['duration']>30])/len(data_dur))*100\n",
    "    return avgr,rid_gt30\n",
    "\n",
    "filepth = ['./data/NYC-2016-Summary.csv', \n",
    "             './data/Chicago-2016-Summary.csv', \n",
    "             './data/Washington-2016-Summary.csv']\n",
    "for path in filepth:    \n",
    "    average_travel, proportion_overtime = trip_durat_cal(path)\n",
    "    cal_dur = {}\n",
    "    cal_dur['path']=path\n",
    "    cal_dur['average_travel']=average_travel\n",
    "    cal_dur['proportion_overtime']=proportion_overtime\n",
    "    print(cal_dur)  "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Question 4c**: Dig deeper into the question of trip duration based on ridership. Choose one city. Within that city, which type of user takes longer rides on average: Subscribers or Customers?\n",
    "\n",
    "**Answer**: \n",
    "{'path': './data/NYC-2016-Summary.csv', 'Average Customers Duration': 84.557453936348423, 'Average Subscribers Duration': 63.474524661741931, 'Proportion Customers': 34.45802206500767, 'Proportion Subscribers': 64.96314253203383}\n",
    "{'path': './data/Chicago-2016-Summary.csv', 'Average Customers Duration': 64.098786374293198, 'Average Subscribers Duration': 64.320138888888891, 'Proportion Customers': 80.43261231281198, 'Proportion Subscribers': 19.56738768718802}\n",
    "{'path': './data/Washington-2016-Summary.csv', 'Average Customers Duration': 79.788448199941357, 'Average Subscribers Duration': 68.109266289893625, 'Proportion Customers': 79.07914869940187, 'Proportion Subscribers': 20.920851300598137}\n",
    "\n",
    "I am picking NYC for the calculation.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'path': './data/NYC-2016-Summary.csv', 'Average Customers Duration': 84.55745393634842, 'Average Subscribers Duration': 63.47452466174193, 'Proportion Customers': 34.45802206500767, 'Proportion Subscribers': 64.96314253203383}\n",
      "{'path': './data/Chicago-2016-Summary.csv', 'Average Customers Duration': 64.0987863742932, 'Average Subscribers Duration': 64.32013888888889, 'Proportion Customers': 80.43261231281198, 'Proportion Subscribers': 19.56738768718802}\n",
      "{'path': './data/Washington-2016-Summary.csv', 'Average Customers Duration': 79.78844819994136, 'Average Subscribers Duration': 68.10926628989363, 'Proportion Customers': 79.07914869940187, 'Proportion Subscribers': 20.920851300598137}\n"
     ]
    }
   ],
   "source": [
    "def cal_gt30_rids(filenm):\n",
    "    data_dur = pandas.read_csv(filenm)\n",
    "    dur_gt30 = data_dur[data_dur['duration']>30]\n",
    "    cust = (len(dur_gt30[dur_gt30['user_type'] == 'Customer'])/len(dur_gt30))*100\n",
    "    cust_dur = dur_gt30[dur_gt30['user_type'] == 'Customer']\n",
    "    avg_cust = numpy.average(cust_dur['duration'])\n",
    "    subs = (len(dur_gt30[dur_gt30['user_type'] == 'Subscriber'])/len(dur_gt30))*100\n",
    "    subs_dur = dur_gt30[dur_gt30['user_type'] == 'Subscriber']\n",
    "    avg_subs = numpy.average(subs_dur['duration'])\n",
    "    return cust, subs, avg_cust, avg_subs\n",
    "filepth = ['./data/NYC-2016-Summary.csv', \n",
    "             './data/Chicago-2016-Summary.csv', \n",
    "             './data/Washington-2016-Summary.csv']\n",
    "for path in filepth:    \n",
    "    cust, subs, avg_cust, avg_subs = cal_gt30_rids(path)\n",
    "    cal_dur = {}\n",
    "    cal_dur['path']=path\n",
    "    cal_dur['Average Customers Duration']=avg_cust\n",
    "    cal_dur['Average Subscribers Duration']=avg_subs\n",
    "    cal_dur['Proportion Customers']=cust\n",
    "    cal_dur['Proportion Subscribers']=subs\n",
    "    print(cal_dur)  "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<a id='visualizations'></a>\n",
    "### Visualizations\n",
    "\n",
    "The last set of values that you computed should have pulled up an interesting result. While the mean trip time for Subscribers is well under 30 minutes, the mean trip time for Customers is actually _above_ 30 minutes! It will be interesting for us to look at how the trip times are distributed. In order to do this, a new library will be introduced here, `matplotlib`. Run the cell below to load the library and to generate an example plot."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# load library\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "# this is a 'magic word' that allows for plots to be displayed\n",
    "# inline with the notebook. If you want to know more, see:\n",
    "# http://ipython.readthedocs.io/en/stable/interactive/magics.html\n",
    "%matplotlib inline \n",
    "\n",
    "# example histogram, data taken from bay area sample\n",
    "data = [ 7.65,  8.92,  7.42,  5.50, 16.17,  4.20,  8.98,  9.62, 11.48, 14.33,\n",
    "        19.02, 21.53,  3.90,  7.97,  2.62,  2.67,  3.08, 14.40, 12.90,  7.83,\n",
    "        25.12,  8.30,  4.93, 12.43, 10.60,  6.17, 10.88,  4.78, 15.15,  3.53,\n",
    "         9.43, 13.32, 11.72,  9.85,  5.22, 15.10,  3.95,  3.17,  8.78,  1.88,\n",
    "         4.55, 12.68, 12.38,  9.78,  7.63,  6.45, 17.38, 11.90, 11.52,  8.63,]\n",
    "plt.hist(data)\n",
    "plt.title('Distribution of Trip Durations')\n",
    "plt.xlabel('Duration (m)')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Above graph right skewed since most of the datd falls to right."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "In the above cell, we collected fifty trip times in a list, and passed this list as the first argument to the `.hist()` function. This function performs the computations and creates plotting objects for generating a histogram, but the plot is actually not rendered until the `.show()` function is executed. The `.title()` and `.xlabel()` functions provide some labeling for plot context.\n",
    "\n",
    "You will now use these functions to create a histogram of the trip times for the city you selected in question 4c. Don't separate the Subscribers and Customers for now: just collect all of the trip times and plot them."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "39396.0\n"
     ]
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "## Use this and additional cells to collect all of the trip times as a list ##\n",
    "## and then use pyplot functions to generate a histogram of trip times.     ##\n",
    "data_hist=pandas.read_csv('./data/NYC-2016-Summary.csv')\n",
    "\n",
    "data_dur=numpy.round(data_hist['duration']).values.T.flatten()\n",
    "print(max(data_dur))\n",
    "plt.hist(data_dur)\n",
    "plt.axis([50, 4000,0,300000])\n",
    "plt.title('Distribution of Trip Durations')\n",
    "plt.xlabel('Duration (m)')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "If you followed the use of the `.hist()` and `.show()` functions exactly like in the example, you're probably looking at a plot that's completely unexpected. The plot consists of one extremely tall bar on the left, maybe a very short second bar, and a whole lot of empty space in the center and right. Take a look at the duration values on the x-axis. This suggests that there are some highly infrequent outliers in the data. Instead of reprocessing the data, you will use additional parameters with the `.hist()` function to limit the range of data that is plotted. Documentation for the function can be found [[here]](https://matplotlib.org/devdocs/api/_as_gen/matplotlib.pyplot.hist.html#matplotlib.pyplot.hist).\n",
    "\n",
    "**Question 5**: Use the parameters of the `.hist()` function to plot the distribution of trip times for the Subscribers in your selected city. Do the same thing for only the Customers. Add limits to the plots so that only trips of duration less than 75 minutes are plotted. As a bonus, set the plots up so that bars are in five-minute wide intervals. For each group, where is the peak of each distribution? How would you describe the shape of each distribution?\n",
    "\n",
    "**Answer**: Most subcribers drive bike for 5 to 20 mins. Most customers drive bike for 10 to 30 mins"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "75.0\n"
     ]
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "## Use this and additional cells to answer Question 5. ##\n",
    "cust_data75 = data_hist[(data_hist['duration']<75) & (data_hist['user_type'] == 'Subscriber')]\n",
    "bin_list=[]\n",
    "for a in range(0,75,5):\n",
    "    bin_list.append(int(a))\n",
    "data_dur=numpy.round(cust_data75['duration']).values.T.flatten()\n",
    "print(max(data_dur))\n",
    "plt.hist(data_dur,bins=bin_list)\n",
    "plt.title('Subscriber Distribution of Trip Durations less than 75')\n",
    "plt.xlabel('Duration (m)')\n",
    "plt.show()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Above graph right skewed since most of the datd falls to right."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "75.0\n"
     ]
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "cust_data75 = data_hist[(data_hist['duration']<75) & (data_hist['user_type'] == 'Customer')]\n",
    "bin_list=[]\n",
    "for a in range(0,75,5):\n",
    "    bin_list.append(int(a))\n",
    "data_dur=numpy.round(cust_data75['duration']).values.T.flatten()\n",
    "print(max(data_dur))\n",
    "plt.hist(data_dur,bins=bin_list)\n",
    "plt.title('Customer Distribution of Trip Durations less than 75')\n",
    "plt.xlabel('Duration (m)')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Above graph right skewed since most of the datd falls to right."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>duration</th>\n",
       "      <th>month</th>\n",
       "      <th>hour</th>\n",
       "      <th>day_of_week</th>\n",
       "      <th>user_type</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>13.983333</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>Friday</td>\n",
       "      <td>Customer</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>11.433333</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>Friday</td>\n",
       "      <td>Subscriber</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>5.250000</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>Friday</td>\n",
       "      <td>Subscriber</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>12.316667</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>Friday</td>\n",
       "      <td>Subscriber</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>20.883333</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>Friday</td>\n",
       "      <td>Customer</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>8.750000</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>Friday</td>\n",
       "      <td>Subscriber</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>10.983333</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>Friday</td>\n",
       "      <td>Subscriber</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>7.733333</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Friday</td>\n",
       "      <td>Subscriber</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>3.433333</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Friday</td>\n",
       "      <td>Subscriber</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>7.083333</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Friday</td>\n",
       "      <td>Customer</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>13.300000</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>Friday</td>\n",
       "      <td>Subscriber</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>9.733333</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>Friday</td>\n",
       "      <td>Subscriber</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>8.416667</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>Friday</td>\n",
       "      <td>Subscriber</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13</th>\n",
       "      <td>23.850000</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>Friday</td>\n",
       "      <td>Subscriber</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14</th>\n",
       "      <td>11.216667</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>Friday</td>\n",
       "      <td>Subscriber</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15</th>\n",
       "      <td>9.016667</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>Friday</td>\n",
       "      <td>Subscriber</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>16</th>\n",
       "      <td>3.183333</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>Friday</td>\n",
       "      <td>Subscriber</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>17</th>\n",
       "      <td>13.916667</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>Friday</td>\n",
       "      <td>Subscriber</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>18</th>\n",
       "      <td>13.133333</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>Friday</td>\n",
       "      <td>Subscriber</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>19</th>\n",
       "      <td>9.966667</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>Friday</td>\n",
       "      <td>Subscriber</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>20</th>\n",
       "      <td>20.633333</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>Friday</td>\n",
       "      <td>Subscriber</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>21</th>\n",
       "      <td>7.666667</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>Friday</td>\n",
       "      <td>Subscriber</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>22</th>\n",
       "      <td>23.450000</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>Friday</td>\n",
       "      <td>Subscriber</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>23</th>\n",
       "      <td>4.700000</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>Friday</td>\n",
       "      <td>Subscriber</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>24</th>\n",
       "      <td>3.550000</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>Friday</td>\n",
       "      <td>Subscriber</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25</th>\n",
       "      <td>16.400000</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>Friday</td>\n",
       "      <td>Customer</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>26</th>\n",
       "      <td>5.200000</td>\n",
       "      <td>1</td>\n",
       "      <td>4</td>\n",
       "      <td>Friday</td>\n",
       "      <td>Subscriber</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>27</th>\n",
       "      <td>23.700000</td>\n",
       "      <td>1</td>\n",
       "      <td>4</td>\n",
       "      <td>Friday</td>\n",
       "      <td>Customer</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>28</th>\n",
       "      <td>11.150000</td>\n",
       "      <td>1</td>\n",
       "      <td>4</td>\n",
       "      <td>Friday</td>\n",
       "      <td>Subscriber</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>29</th>\n",
       "      <td>3.716667</td>\n",
       "      <td>1</td>\n",
       "      <td>5</td>\n",
       "      <td>Friday</td>\n",
       "      <td>Subscriber</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>276768</th>\n",
       "      <td>10.783333</td>\n",
       "      <td>12</td>\n",
       "      <td>19</td>\n",
       "      <td>Saturday</td>\n",
       "      <td>Subscriber</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>276769</th>\n",
       "      <td>4.866667</td>\n",
       "      <td>12</td>\n",
       "      <td>19</td>\n",
       "      <td>Saturday</td>\n",
       "      <td>Subscriber</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>276770</th>\n",
       "      <td>8.050000</td>\n",
       "      <td>12</td>\n",
       "      <td>19</td>\n",
       "      <td>Saturday</td>\n",
       "      <td>Subscriber</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>276771</th>\n",
       "      <td>48.466667</td>\n",
       "      <td>12</td>\n",
       "      <td>20</td>\n",
       "      <td>Saturday</td>\n",
       "      <td>Subscriber</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>276772</th>\n",
       "      <td>25.550000</td>\n",
       "      <td>12</td>\n",
       "      <td>20</td>\n",
       "      <td>Saturday</td>\n",
       "      <td>Customer</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>276773</th>\n",
       "      <td>2.800000</td>\n",
       "      <td>12</td>\n",
       "      <td>20</td>\n",
       "      <td>Saturday</td>\n",
       "      <td>Subscriber</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>276774</th>\n",
       "      <td>29.000000</td>\n",
       "      <td>12</td>\n",
       "      <td>20</td>\n",
       "      <td>Saturday</td>\n",
       "      <td>Subscriber</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>276775</th>\n",
       "      <td>35.333333</td>\n",
       "      <td>12</td>\n",
       "      <td>20</td>\n",
       "      <td>Saturday</td>\n",
       "      <td>Subscriber</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>276776</th>\n",
       "      <td>22.466667</td>\n",
       "      <td>12</td>\n",
       "      <td>20</td>\n",
       "      <td>Saturday</td>\n",
       "      <td>Subscriber</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>276777</th>\n",
       "      <td>30.800000</td>\n",
       "      <td>12</td>\n",
       "      <td>20</td>\n",
       "      <td>Saturday</td>\n",
       "      <td>Subscriber</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>276778</th>\n",
       "      <td>17.050000</td>\n",
       "      <td>12</td>\n",
       "      <td>20</td>\n",
       "      <td>Saturday</td>\n",
       "      <td>Subscriber</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>276779</th>\n",
       "      <td>13.783333</td>\n",
       "      <td>12</td>\n",
       "      <td>20</td>\n",
       "      <td>Saturday</td>\n",
       "      <td>Subscriber</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>276780</th>\n",
       "      <td>11.633333</td>\n",
       "      <td>12</td>\n",
       "      <td>20</td>\n",
       "      <td>Saturday</td>\n",
       "      <td>Subscriber</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>276781</th>\n",
       "      <td>1.416667</td>\n",
       "      <td>12</td>\n",
       "      <td>20</td>\n",
       "      <td>Saturday</td>\n",
       "      <td>Subscriber</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>276782</th>\n",
       "      <td>16.800000</td>\n",
       "      <td>12</td>\n",
       "      <td>20</td>\n",
       "      <td>Saturday</td>\n",
       "      <td>Subscriber</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>276783</th>\n",
       "      <td>5.733333</td>\n",
       "      <td>12</td>\n",
       "      <td>21</td>\n",
       "      <td>Saturday</td>\n",
       "      <td>Subscriber</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>276784</th>\n",
       "      <td>13.583333</td>\n",
       "      <td>12</td>\n",
       "      <td>21</td>\n",
       "      <td>Saturday</td>\n",
       "      <td>Subscriber</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>276785</th>\n",
       "      <td>27.333333</td>\n",
       "      <td>12</td>\n",
       "      <td>21</td>\n",
       "      <td>Saturday</td>\n",
       "      <td>Customer</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>276786</th>\n",
       "      <td>17.850000</td>\n",
       "      <td>12</td>\n",
       "      <td>21</td>\n",
       "      <td>Saturday</td>\n",
       "      <td>Subscriber</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>276787</th>\n",
       "      <td>11.066667</td>\n",
       "      <td>12</td>\n",
       "      <td>21</td>\n",
       "      <td>Saturday</td>\n",
       "      <td>Subscriber</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>276788</th>\n",
       "      <td>12.633333</td>\n",
       "      <td>12</td>\n",
       "      <td>21</td>\n",
       "      <td>Saturday</td>\n",
       "      <td>Subscriber</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>276789</th>\n",
       "      <td>29.966667</td>\n",
       "      <td>12</td>\n",
       "      <td>21</td>\n",
       "      <td>Saturday</td>\n",
       "      <td>Subscriber</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>276790</th>\n",
       "      <td>11.683333</td>\n",
       "      <td>12</td>\n",
       "      <td>21</td>\n",
       "      <td>Saturday</td>\n",
       "      <td>Subscriber</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>276791</th>\n",
       "      <td>3.916667</td>\n",
       "      <td>12</td>\n",
       "      <td>22</td>\n",
       "      <td>Saturday</td>\n",
       "      <td>Subscriber</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>276792</th>\n",
       "      <td>9.350000</td>\n",
       "      <td>12</td>\n",
       "      <td>22</td>\n",
       "      <td>Saturday</td>\n",
       "      <td>Subscriber</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>276793</th>\n",
       "      <td>4.916667</td>\n",
       "      <td>12</td>\n",
       "      <td>22</td>\n",
       "      <td>Saturday</td>\n",
       "      <td>Customer</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>276794</th>\n",
       "      <td>4.616667</td>\n",
       "      <td>12</td>\n",
       "      <td>22</td>\n",
       "      <td>Saturday</td>\n",
       "      <td>Subscriber</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>276795</th>\n",
       "      <td>10.016667</td>\n",
       "      <td>12</td>\n",
       "      <td>23</td>\n",
       "      <td>Saturday</td>\n",
       "      <td>Subscriber</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>276796</th>\n",
       "      <td>35.033333</td>\n",
       "      <td>12</td>\n",
       "      <td>23</td>\n",
       "      <td>Saturday</td>\n",
       "      <td>Subscriber</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>276797</th>\n",
       "      <td>20.966667</td>\n",
       "      <td>12</td>\n",
       "      <td>23</td>\n",
       "      <td>Saturday</td>\n",
       "      <td>Subscriber</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>276798 rows × 5 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "         duration  month  hour day_of_week   user_type\n",
       "0       13.983333      1     0      Friday    Customer\n",
       "1       11.433333      1     0      Friday  Subscriber\n",
       "2        5.250000      1     0      Friday  Subscriber\n",
       "3       12.316667      1     0      Friday  Subscriber\n",
       "4       20.883333      1     0      Friday    Customer\n",
       "5        8.750000      1     0      Friday  Subscriber\n",
       "6       10.983333      1     0      Friday  Subscriber\n",
       "7        7.733333      1     1      Friday  Subscriber\n",
       "8        3.433333      1     1      Friday  Subscriber\n",
       "9        7.083333      1     1      Friday    Customer\n",
       "10      13.300000      1     2      Friday  Subscriber\n",
       "11       9.733333      1     2      Friday  Subscriber\n",
       "12       8.416667      1     2      Friday  Subscriber\n",
       "13      23.850000      1     2      Friday  Subscriber\n",
       "14      11.216667      1     2      Friday  Subscriber\n",
       "15       9.016667      1     2      Friday  Subscriber\n",
       "16       3.183333      1     2      Friday  Subscriber\n",
       "17      13.916667      1     2      Friday  Subscriber\n",
       "18      13.133333      1     2      Friday  Subscriber\n",
       "19       9.966667      1     3      Friday  Subscriber\n",
       "20      20.633333      1     3      Friday  Subscriber\n",
       "21       7.666667      1     3      Friday  Subscriber\n",
       "22      23.450000      1     3      Friday  Subscriber\n",
       "23       4.700000      1     3      Friday  Subscriber\n",
       "24       3.550000      1     3      Friday  Subscriber\n",
       "25      16.400000      1     3      Friday    Customer\n",
       "26       5.200000      1     4      Friday  Subscriber\n",
       "27      23.700000      1     4      Friday    Customer\n",
       "28      11.150000      1     4      Friday  Subscriber\n",
       "29       3.716667      1     5      Friday  Subscriber\n",
       "...           ...    ...   ...         ...         ...\n",
       "276768  10.783333     12    19    Saturday  Subscriber\n",
       "276769   4.866667     12    19    Saturday  Subscriber\n",
       "276770   8.050000     12    19    Saturday  Subscriber\n",
       "276771  48.466667     12    20    Saturday  Subscriber\n",
       "276772  25.550000     12    20    Saturday    Customer\n",
       "276773   2.800000     12    20    Saturday  Subscriber\n",
       "276774  29.000000     12    20    Saturday  Subscriber\n",
       "276775  35.333333     12    20    Saturday  Subscriber\n",
       "276776  22.466667     12    20    Saturday  Subscriber\n",
       "276777  30.800000     12    20    Saturday  Subscriber\n",
       "276778  17.050000     12    20    Saturday  Subscriber\n",
       "276779  13.783333     12    20    Saturday  Subscriber\n",
       "276780  11.633333     12    20    Saturday  Subscriber\n",
       "276781   1.416667     12    20    Saturday  Subscriber\n",
       "276782  16.800000     12    20    Saturday  Subscriber\n",
       "276783   5.733333     12    21    Saturday  Subscriber\n",
       "276784  13.583333     12    21    Saturday  Subscriber\n",
       "276785  27.333333     12    21    Saturday    Customer\n",
       "276786  17.850000     12    21    Saturday  Subscriber\n",
       "276787  11.066667     12    21    Saturday  Subscriber\n",
       "276788  12.633333     12    21    Saturday  Subscriber\n",
       "276789  29.966667     12    21    Saturday  Subscriber\n",
       "276790  11.683333     12    21    Saturday  Subscriber\n",
       "276791   3.916667     12    22    Saturday  Subscriber\n",
       "276792   9.350000     12    22    Saturday  Subscriber\n",
       "276793   4.916667     12    22    Saturday    Customer\n",
       "276794   4.616667     12    22    Saturday  Subscriber\n",
       "276795  10.016667     12    23    Saturday  Subscriber\n",
       "276796  35.033333     12    23    Saturday  Subscriber\n",
       "276797  20.966667     12    23    Saturday  Subscriber\n",
       "\n",
       "[276798 rows x 5 columns]"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data_hist"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": true
   },
   "source": [
    "<a id='eda_continued'></a>\n",
    "## Performing Your Own Analysis\n",
    "\n",
    "So far, you've performed an initial exploration into the data available. You have compared the relative volume of trips made between three U.S. cities and the ratio of trips made by Subscribers and Customers. For one of these cities, you have investigated differences between Subscribers and Customers in terms of how long a typical trip lasts. Now it is your turn to continue the exploration in a direction that you choose. Here are a few suggestions for questions to explore:\n",
    "\n",
    "- How does ridership differ by month or season? Which month / season has the highest ridership? Does the ratio of Subscriber trips to Customer trips change depending on the month or season?\n",
    "- Is the pattern of ridership different on the weekends versus weekdays? On what days are Subscribers most likely to use the system? What about Customers? Does the average duration of rides change depending on the day of the week?\n",
    "- During what time of day is the system used the most? Is there a difference in usage patterns for Subscribers and Customers?\n",
    "\n",
    "If any of the questions you posed in your answer to question 1 align with the bullet points above, this is a good opportunity to investigate one of them. As part of your investigation, you will need to create a visualization. If you want to create something other than a histogram, then you might want to consult the [Pyplot documentation](https://matplotlib.org/devdocs/api/pyplot_summary.html). In particular, if you are plotting values across a categorical variable (e.g. city, user type), a bar chart will be useful. The [documentation page for `.bar()`](https://matplotlib.org/devdocs/api/_as_gen/matplotlib.pyplot.bar.html#matplotlib.pyplot.bar) includes links at the bottom of the page with examples for you to build off of for your own use.\n",
    "\n",
    "**Question 6**: Continue the investigation by exploring another question that could be answered by the data available. Document the question you want to explore below. Your investigation should involve at least two variables and should compare at least two groups. You should also use at least one visualization as part of your explorations.\n",
    "\n",
    "**Answer**: dutation, usertype"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "23\n"
     ]
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAa8AAAEWCAYAAADRrhi8AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADl0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uIDMuMC4yLCBodHRwOi8vbWF0cGxvdGxpYi5vcmcvOIA7rQAAH/JJREFUeJzt3XuYHVWZ7/HvjxABAQVMg7lhK+AFcAwaLg6eEcHjcBsBDyiMSnAYoueBGbzMjIEZR1BxwoyAIoonCpOAyEW8ECEeRSQiOgQTJkBCVCJEEhKTBgImck1454+1GnZ27+7e3enqvVf693mefrr2qqpVb61dVW/VqupqRQRmZmYl2arVAZiZmQ2Uk5eZmRXHycvMzIrj5GVmZsVx8jIzs+I4eZmZWXGcvDaDpP8l6TdDWN8PJU3Jw6dIun0I636/pB8PVX0DWO7Bku6XtF7SsQ3GL5P0zuGOqz+SjpO0PMe9X6vjGSqSvibpU8O4vE5JIWnr4VpmgxhC0p6tWv5IJOkQSSuqXEZTyUvSX0uan3fkVfkg+7bNWbCkcyR9c3PqqFKO7zlJ6/LPbyVdImls9zQR8fOIeF2TdfW7rhFxRETMGoLYexwwIuKqiHjX5tY9CJ8BLomIHSLi+y1Y/mB9ATgjx/3fm1uZpLmSns7b0h8lLZA0TdI2QxBrb8vscQIUER+JiM9WtcxWy+38ty1a9tn5GNn985Sk5yWNyeNnSnq2bppRwxDXzHw8eHdd+Rdz+SlVx1CFfpOXpI8DXwQ+D+wG7A58FTim2tCGTx9nhddGxI7ALsBxwCuBBbUJbIiWL0lb6lXwq4DFrQ5iEGf+g467jwPSGXl7Ggt8AjgRmCNJg1hGy65krLGI+Hw+2dkhInYAzgfmRsQjNZP9e+00EbFxmML7LTCl+0Pefk4AfjdMyx96EdHrD/ByYD1wQh/TzAQ+V/P5EGBFzedPAg8D64DfAIcBhwPPAs/l+u/O044DZgOPAUuB02rqOQf4NvDNXNe9wGuBs4A1wHLgXXWxXwasysv/HDAqjzsF+AVwUV7W5xqs1znAN+vKRgF3A18YgnWdC5yX43gK2DOX/W1djF8GngB+DRxWs6xlwDsbxQs8BERe3nrgrbm+22um/3PgV7nuXwF/XjNuLvDZvPx1wI+BMX1sA6fl7+ux/P2Ny+W/A57P67ce2KbBvMuAfwDuybFcC2zbRN2deR23rou7vv1e+I5zG/8sL+cR0slJfTzb5FgD+BPwu1z+hlz/46Sk9u66feBSYE6e550N6n0htpqy3YEngaOb3JeWkbaxe4BngK2Babmd1wH3AcfVxPs0sDGvz+O9LKNh++ZxAXwEuB9YC3wFUB7Xb1s2+p7oe79sWCeg/D2uyePuAfZtsKzz8vo+ndf5kibWYw/gp8CjeZlXATs1u332sU8ofy9TejtW9jP/VsC/AL/P630F8PK6Np1C2tcfAf65n2P0F4A/ADvnsqOBHwK3A6ds7jKB7fJy1pK2w39k0223t+10G9K298aaaXclHTM6+myjfhrwcGADNQeIXhqm4Q4HvI6UVGoPOHvUH2xr5v0Z6apuW2AS0EU+YOfpnwb+krTTXgE8CPwzMJq0Ez5YU9f3gf8HbJ8b407gwzUHtg3A3+W6tmuwXj3iy+WfAeYNwbrOzRvBPjmG0fQ8+G4APpbHvY+08+xSs1P1lrw66XlgP4WcvEhXkmuBD+Zln5Q/v6Imtt+RTg62y5+n9/L9H0rakN9M2hC/DNxWt/P3OJjXjb+TdOKyC7AE+Eh/dfeyjo3a74XvGLiatL1sRdrG3tZHXAHsmYdHkw7wZwMvyXGtA15Xsw88ARzcXXeD+l6Ira78NuD8/valmrZaCEwkb7Oks+dxebnvIyXPsfXfeaP9tYnvLoAbgZ1IibYLODyPa6ot678n+t4vG9ZJ2ucX5DhESsxje1lej3buZz32BP53Xv+O/H18sZnts59j51+QEugOdW3/WP5ZAPyfPub/G9I29xpgB+C7wJV1bfp10nb9JtLJzBv6OkYDM4D/m8uuI+33tclr0MsEpgM/z200EVjEpttuX9vpV8n7QP58JvCD/tq4v66qVwCPRMSGfqbrzUbSRrG3pNERsSwiGl6mSpoIvA34ZEQ8HRELgW+QDrDdfh4RP8rxfJu0sU2PiOeAa4BOSTtJ2g04AvhoRPwpItaQztxOrKlrZUR8OSI2RMRTA1inlaQvaNDrWmNmRCzOMTzXYPwa0o70XERcS7qaO2oAsfbmKOD+iLgyL/tq0pXdX9VM858R8dvcNteRTiYaeT9weUTcFRHPkK6E3yqpcwDxXBwRKyPiMeAHNcva3Lrrv+PnSN2B4/I21uwDMQeRdubpEfFsRPyUdDA8qWaaGyLiFxHxfEQ83WS90Pv21JuLI2J59zYbEd/Obfd83kbuBw5osq5m2nd6RDweEQ8Bt/LidzPgtmxiv+ytzueAHYHXk66YlkTEqibXsc/1iIilEXFzRDwTEV3AhcDb6+btbfvsyxTg+ohYX1sPsBcpaX8KmCnp4F7mfz9wYUQ8kOs4Czixrrv43Ih4KiLuJvUIvamfmK4ATpb08ryO9fegN2eZ7wXOi4jHImJ5XtcX9LOdzgL+uubWyQeBK/tZl36T16PAmMH2r0fEUuCjpKuCNZKukTSul8nHAY9FxLqast8D42s+r64ZfoqUWDfWfIZ0kHkV6Wx5laTHJT1OOtvbtWb+5YNYJXI8j9UXDnBdm43h4cinItnvSe20ucblumrVt/UfaoafJLVrv3Xljf7Rurr609uyNrfu+vb9J9KZ+52SFkv6mybrGQcsj4jna8rq22tIt6c+bLIcSSdLWlizne8LjGmyrmbat7fvZjBt2d9+2bDOfLJwCam7b7WkGZJe1uQ69rkeknbN++rDkv5Iui1R337N7gvkOrcjXWls8vBVPkl4NJ9MzSF1Ub6nl2rq99Hfk3oQdhtsXPlkoIPUNXhjg5P2zVnmODbdNjc5vvS1nUbEPNKV2NslvZ50NTy7r3WB/pPXf5G66no84lzjT8BLaz6/snZkRHwrIt5G2nCDdBOTPFxrJbCLpB1rynYn9YsP1HLSJe2YiNgp/7wsIvapDW2gleYzg78iXR73MIB1bTaG8XU383cntRP03e791bsyx1hrsG29SV2StiddsQ+mroHU/adc3Ou2R107RMQfIuK0iBgHfBj4apOPUK8EJtY9VFPfXoPZniYCb+HF7anPfal+OZJeRerGOYPU5bsTqbtG9dP2YtDf3SDbss/9sq86I+LiiHgLqZv9taR7Kg1D6y/2Ov+W5/mziHgZ8AFebL/Beg/phGRuP9NFH8uq30d3J3WDr248edO+SXpY6IohXuYqUndh7bxAU9sppET/AdJV1/XN9F70mbwi4gngX4GvSDpW0ksljZZ0hKR/z5MtBI6UtIukV5KuPrqDfp2kQ/PjwE+Tro66r5RWk7r5tsrLWg78Evg3SdtK+jPgVNLZyYDkLoUfAxdIepmkrSTtIam+O6ApeZ3fQOqTfyWpa6F+mqbXdQB2Bf4+L/8EUl//nDxuIemSfrSkycDxNfN1kR6UeE0v9c4BXqv0JxBbS3ofsDepK2ygvgV8SNKkvO6fJ90TXDaIupquO3fxPAx8QNKofJa+R1+VSTpB0oT8cS3p4NHM017dZ4b/lNv7ENJJzDWDWam8H70duIF0P6X2O224L/Vie9I6dOV6P0Q6o+22Gpgg6SW9zD/o724wbdnfftlbnZL2l3SgpNGk76H7QZRGVtP7dt/IjuQHWiSNp/ekOBBTgCvqek2QdLykHfJ6v4t0sO7tCuNq4GOSXi1pB9J3c20M/hZOt4tJ9/huG+JlXgecJWnn/B3+Xc24/rZTSN2Ex5HapFFi7aHfg2lEXAh8nHSp2UU6ezqDF/tLryT1fS4jbZjX1sy+DelG3iOky81dSTe9Id2zAnhU0l15+CTSjcGVwPeAT0fEzc2sSAMnk26u30faEa4nPaI8EO+TtJ70hNlsUpfKWyJiZYNpB7quzZhH6iN/hPQk1fER8Wge9ynSwXotcC7pQARARDyZp/9Fvkw/qLbSXMfRpDOwR0ndNUfHpo/0NiUibsmxfId09rUHm95bHLQm6j6NdLB5lHRG/st+qtwfmJe/09nAmRHxYBNxPAu8m3S/5hHSDeaTI+LXA1ohuETSOtIB9ouk9Tq8pjuyr32pUVz3AReQekhWA28kPWHZ7aekJyP/IKnHd7uZ392g2pK+98ve6nwZ6cx9Lak76lHS03ONfAk4XtJaSRf3Mk2tc0kPrDwB3ER6SGHQcgI8lMYH4DNJJ1yPA/9Bepp6bi9VXU7aHm4jPZj2NJsmhEHJ96RuqU+sQ7DMc0nfzYOkbfeFe1ZNbKdExArgLlKSa9izVU+N18HMzGz4SLqc9JDVvzQzvf/Q0czMWkrpCdf3AE2/im1LfauDmZkVQNJnSQ9w/EeTXc9pPncbmplZaXzlZWZmxSn+nteYMWOis7Oz1WGYmRVlwYIFj0RER6vjGKzik1dnZyfz589vdRhmZkWRVP+WnaK429DMzIrj5GVmZsVx8jIzs+I4eZmZWXGcvMzMrDhOXmZmVhwnLzMzK46Tl5mZFcfJy8zMilP8GzbMrCyd024a1HzLph81xJFYyXzlZWZmxXHyMjOz4jh5mZlZcZy8zMysOJUmL0nbSrpT0t2SFks6N5fPlPSgpIX5Z1Iul6SLJS2VdI+kN1cZn5mZlanqpw2fAQ6NiPWSRgO3S/phHvePEXF93fRHAHvlnwOBS/NvMzOzF1R65RXJ+vxxdP6JPmY5Brgiz3cHsJOksVXGaGZm5an8npekUZIWAmuAmyNiXh51Xu4avEjSNrlsPLC8ZvYVuay+zqmS5kua39XVVWn8ZmbWfipPXhGxMSImAROAAyTtC5wFvB7YH9gF+GSeXI2qaFDnjIiYHBGTOzo6KorczMza1bA9bRgRjwNzgcMjYlXuGnwG+E/ggDzZCmBizWwTgJXDFaOZmZWh6qcNOyTtlIe3A94J/Lr7PpYkAccCi/Iss4GT81OHBwFPRMSqKmM0M7PyVP204VhglqRRpER5XUTcKOmnkjpI3YQLgY/k6ecARwJLgSeBD1Ucn5mZFajS5BUR9wD7NSg/tJfpAzi9ypjMzKx8fsOGmZkVx8nLzMyK4//nZWaDMtj/y2U2FHzlZWZmxXHyMjOz4rjb0KzNDLY7btn0o4Y4ErP25SsvMzMrjpOXmZkVx8nLzMyK4+RlZmbF8QMbZiOc/17LSuQrLzMzK46Tl5mZFcfJy8zMiuPkZWZmxXHyMjOz4jh5mZlZcfyovJkVYTCP9Pt9j1suJy+zLYT/XstGkkq7DSVtK+lOSXdLWizp3Fz+aknzJN0v6VpJL8nl2+TPS/P4zirjMzOzMlV9z+sZ4NCIeBMwCThc0kHA+cBFEbEXsBY4NU9/KrA2IvYELsrTmZmZbaLS5BXJ+vxxdP4J4FDg+lw+Czg2Dx+TP5PHHyZJVcZoZmblqfxpQ0mjJC0E1gA3A78DHo+IDXmSFcD4PDweWA6Qxz8BvKLqGM3MrCyVJ6+I2BgRk4AJwAHAGxpNln83usqK+gJJUyXNlzS/q6tr6II1M7MiDNvfeUXE48Bc4CBgJ0ndTzpOAFbm4RXARIA8/uXAYw3qmhERkyNickdHR9Whm5lZm6n6acMOSTvl4e2AdwJLgFuB4/NkU4Ab8vDs/Jk8/qcR0ePKy8zMRraq/85rLDBL0ihSorwuIm6UdB9wjaTPAf8NXJanvwy4UtJS0hXXiRXHZ2ZmBao0eUXEPcB+DcofIN3/qi9/GjihypjMzKx8frehmZkVx8nLzMyK4+RlZmbFcfIyM7PiOHmZmVlxnLzMzKw4Tl5mZlYcJy8zMyuOk5eZmRWn6tdDmY1ondNuanUIZlskX3mZmVlxnLzMzKw4Tl5mZlYcJy8zMyuOk5eZmRXHycvMzIrj5GVmZsVx8jIzs+I4eZmZWXGcvMzMrDiVJi9JEyXdKmmJpMWSzszl50h6WNLC/HNkzTxnSVoq6TeS/rLK+MzMrExVv9twA/CJiLhL0o7AAkk353EXRcQXaieWtDdwIrAPMA74iaTXRsTGiuM0M7OCVHrlFRGrIuKuPLwOWAKM72OWY4BrIuKZiHgQWAocUGWMZmZWnmF7q7ykTmA/YB5wMHCGpJOB+aSrs7WkxHZHzWwraJDsJE0FpgLsvvvulcZtZuUa7Fv9l00/aogjsaE2LA9sSNoB+A7w0Yj4I3ApsAcwCVgFXNA9aYPZo0dBxIyImBwRkzs6OiqK2szM2lXlyUvSaFLiuioivgsQEasjYmNEPA98nRe7BlcAE2tmnwCsrDpGMzMrS9VPGwq4DFgSERfWlI+tmew4YFEeng2cKGkbSa8G9gLurDJGMzMrT9X3vA4GPgjcK2lhLjsbOEnSJFKX4DLgwwARsVjSdcB9pCcVT/eThmZmVq/S5BURt9P4PtacPuY5DzivsqDMzKx4fsOGmZkVx8nLzMyK4+RlZmbFcfIyM7PiOHmZmVlxnLzMzKw4Tl5mZlYcJy8zMyuOk5eZmRXHycvMzIrj5GVmZsVx8jIzs+I4eZmZWXGcvMzMrDhOXmZmVhwnLzMzK46Tl5mZFcfJy8zMiuPkZWZmxak0eUmaKOlWSUskLZZ0Zi7fRdLNku7Pv3fO5ZJ0saSlku6R9OYq4zMzszJtXXH9G4BPRMRdknYEFki6GTgFuCUipkuaBkwDPgkcAeyVfw4ELs2/zVqqc9pNrQ7BzGpUeuUVEasi4q48vA5YAowHjgFm5clmAcfm4WOAKyK5A9hJ0tgqYzQzs/IM2z0vSZ3AfsA8YLeIWAUpwQG75snGA8trZluRy+rrmippvqT5XV1dVYZtZmZtaFiSl6QdgO8AH42IP/Y1aYOy6FEQMSMiJkfE5I6OjqEK08zMClF58pI0mpS4roqI7+bi1d3dgfn3mly+AphYM/sEYGXVMZqZWVmqftpQwGXAkoi4sGbUbGBKHp4C3FBTfnJ+6vAg4Inu7kUzM7NuVT9teDDwQeBeSQtz2dnAdOA6SacCDwEn5HFzgCOBpcCTwIcqjs/MzApUafKKiNtpfB8L4LAG0wdwepUxmZlZ+fyGDTMzK46Tl5mZFcfJy8zMiuPkZWZmxXHyMjOz4jh5mZlZcZy8zMysOE5eZmZWHCcvMzMrjpOXmZkVx8nLzMyK4+RlZmbFcfIyM7PiOHmZmVlxnLzMzKw4Tl5mZlYcJy8zMyuOk5eZmRXHycvMzIrj5GVmZsXZusrKJV0OHA2siYh9c9k5wGlAV57s7IiYk8edBZwKbAT+PiJ+VGV8ZmbtoHPaTYOab9n0o4Y4knJUfeU1Ezi8QflFETEp/3Qnrr2BE4F98jxflTSq4vjMzKxAlV55RcRtkjqbnPwY4JqIeAZ4UNJS4ADgvyoKz8ysIV8Jtb9W3fM6Q9I9ki6XtHMuGw8sr5lmRS7rQdJUSfMlze/q6mo0iZmZbcFakbwuBfYAJgGrgAtyuRpMG40qiIgZETE5IiZ3dHRUE6WZmbWtYU9eEbE6IjZGxPPA10ldg5CutCbWTDoBWDnc8ZmZWfsb9uQlaWzNx+OARXl4NnCipG0kvRrYC7hzuOMzM7P2V/Wj8lcDhwBjJK0APg0cImkSqUtwGfBhgIhYLOk64D5gA3B6RGysMj4zMytT1U8bntSg+LI+pj8POK+6iMzMbEvgN2yYmVlxnLzMzKw4Tl5mZlYcJy8zMyuOk5eZmRXHycvMzIrj5GVmZsVx8jIzs+I4eZmZWXGcvMzMrDhOXmZmVhwnLzMzK46Tl5mZFcfJy8zMiuPkZWZmxXHyMjOz4jh5mZlZcZy8zMysOE5eZmZWnK2rrFzS5cDRwJqI2DeX7QJcC3QCy4D3RsRaSQK+BBwJPAmcEhF3VRmfmdlQ6px2U6tDGDEqTV7ATOAS4IqasmnALRExXdK0/PmTwBHAXvnnQODS/NtsyPjgYrZlqLTbMCJuAx6rKz4GmJWHZwHH1pRfEckdwE6SxlYZn5mZlakV97x2i4hVAPn3rrl8PLC8ZroVuawHSVMlzZc0v6urq9Jgzcys/bTTAxtqUBaNJoyIGRExOSImd3R0VByWmZm1m1Ykr9Xd3YH595pcvgKYWDPdBGDlMMdmZmYFaEXymg1MycNTgBtqyk9WchDwRHf3opmZWa2qH5W/GjgEGCNpBfBpYDpwnaRTgYeAE/Lkc0iPyS8lPSr/oSpjMzOzclWavCLipF5GHdZg2gBOrzIeMzPbMrTTAxtmZmZNcfIyM7PiOHmZmVlxqn49lFkl/Jons5HNV15mZlYcJy8zMyuOk5eZmRXHycvMzIrj5GVmZsVx8jIzs+I4eZmZWXGcvMzMrDhOXmZmVhwnLzMzK46Tl5mZFcfJy8zMiuPkZWZmxXHyMjOz4jh5mZlZcVr2/7wkLQPWARuBDRExWdIuwLVAJ7AMeG9ErG1VjGZm1p5afeX1joiYFBGT8+dpwC0RsRdwS/5sZma2iVYnr3rHALPy8Czg2BbGYmZmbaqVySuAH0taIGlqLtstIlYB5N+7NppR0lRJ8yXN7+rqGqZwzcysXbTsnhdwcESslLQrcLOkXzc7Y0TMAGYATJ48OaoK0MzM2lPLrrwiYmX+vQb4HnAAsFrSWID8e02r4jMzs/bVkuQlaXtJO3YPA+8CFgGzgSl5sinADa2Iz8zM2lurug13A74nqTuGb0XE/5f0K+A6SacCDwEntCg+MzNrYy1JXhHxAPCmBuWPAocNf0RmZlaSVj6w0XKd024a1HzLph81xJGYmdlAtNvfeZmZmfXLycvMzIrj5GVmZsUZ0fe8rPUGe9/RzEY2X3mZmVlxnLzMzKw4Tl5mZlYcJy8zMyuOH9gYBP9xs5lZa/nKy8zMiuPkZWZmxXHyMjOz4jh5mZlZcZy8zMysOE5eZmZWHCcvMzMrjv/Oy4aEX7BrZsPJyWsY+Y+bzcyGhpNXAZz0zMw21XbJS9LhwJeAUcA3ImJ6i0MacdwFaGbtrq0e2JA0CvgKcASwN3CSpL1bG5WZmbWbtkpewAHA0oh4ICKeBa4BjmlxTGZm1mbardtwPLC85vMK4MD6iSRNBabmj+sl/WaQyxsDPDLIeduezh/0rFt0uwyS26Qnt0lPw9omm7GPA7xqiMJoiXZLXmpQFj0KImYAMzZ7YdL8iJi8ufVsadwuPblNenKb9OQ2GT7t1m24AphY83kCsLJFsZiZWZtqt+T1K2AvSa+W9BLgRGB2i2MyM7M201bdhhGxQdIZwI9Ij8pfHhGLK1zkZnc9bqHcLj25TXpym/TkNhkmiuhxS8nMzKyttVu3oZmZWb+cvMzMrDgjNnlJOlzSbyQtlTSt1fG0A0nLJN0raaGk+a2OpxUkXS5pjaRFNWW7SLpZ0v35986tjLEVemmXcyQ9nLeXhZKObGWMw0nSREm3SloiabGkM3P5iN9WhsuITF5+DVWf3hERk0bw36rMBA6vK5sG3BIRewG35M8jzUx6tgvARXl7mRQRc4Y5plbaAHwiIt4AHAScno8h3laGyYhMXvg1VNaLiLgNeKyu+BhgVh6eBRw7rEG1gV7aZcSKiFURcVceXgcsIb0haMRvK8NlpCavRq+hGt+iWNpJAD+WtCC/gsuS3SJiFaSDFrBri+NpJ2dIuid3K47ILjJJncB+wDy8rQybkZq8mnoN1Qh0cES8mdSderqkv2h1QNbWLgX2ACYBq4ALWhvO8JO0A/Ad4KMR8cdWxzOSjNTk5ddQNRARK/PvNcD3SN2rBqsljQXIv9e0OJ62EBGrI2JjRDwPfJ0Rtr1IGk1KXFdFxHdzsbeVYTJSk5dfQ1VH0vaSduweBt4FLOp7rhFjNjAlD08BbmhhLG2j+yCdHccI2l4kCbgMWBIRF9aM8rYyTEbsGzbyY71f5MXXUJ3X4pBaStJrSFdbkF4b9q2R2CaSrgYOIf1ri9XAp4HvA9cBuwMPASdExIh6eKGXdjmE1GUYwDLgw933e7Z0kt4G/By4F3g+F59Nuu81oreV4TJik5eZmZVrpHYbmplZwZy8zMysOE5eZmZWHCcvMzMrjpOXmZkVx8nLtniSNua3ni+WdLekj0sasm1f0imSxtV8/sZQvehZ0rGS/nWA8/xkpL6qyUYOPypvWzxJ6yNihzy8K/At4BcR8ekB1DEqIjb2Mm4u8A8RMeT/RkbSL4F3R8QjA5hnCjBhJP6dno0cvvKyESW/+moq6YWyyldNl3SPl3SjpEPy8HpJn5E0D3irpH+V9CtJiyTNyPMfD0wGrspXd9tJmitpcq7jpPw/0hZJOr9mOeslnZevBO+QtFt9rJJeCzzTnbgkzZR0af4/Ug9Ient+Ie4SSTNrZp0NnDTUbWfWTpy8bMSJiAdI235/b/zeHlgUEQdGxO3AJRGxf0TsC2wHHB0R1wPzgffn/2n1VPfMuSvxfOBQ0pso9pd0bE3dd0TEm4DbgNMaLP9g4K66sp1zfR8DfgBcBOwDvFHSpLx+a4FtJL2iieYwK5KTl41Ujf6zQL2NpBevdnuHpHmS7iUlkH36mX9/YG5EdEXEBuAqoPtN/c8CN+bhBUBng/nHAl11ZT+I1Nd/L7A6Iu7NL8ZdXFfHGmAcZluorVsdgNlwy+9x3Eg6wG9g05O4bWuGn+6+zyVpW+CrwOSIWC7pnLppGy6qj3HPxYs3nDfSeF98Cnh5Xdkz+ffzNcPdn2vr2DbPb7ZF8pWXjSiSOoCvkboAu18oO0nSVpIm0vu/9ehOVI/k/+F0fM24dcCODeaZB7xd0hhJo0j3oX42gHCXAHsOYHrghTeev5K0bmZbJF952UiwnaSFwGjSldaVQPe/sfgF8CCpG24RPe8xARARj0v6ep5uGenf6nSbCXxN0lPAW2vmWSXpLOBW0lXYnIgYyL/IuA24QJJqrtKa8RbS/bQNA5jHrCh+VN6sjUn6Euk+108GOM/siLilusjMWsvdhmbt7fPASwc4zyInLtvS+crLzMyK4ysvMzMrjpOXmZkVx8nLzMyK4+RlZmbFcfIyM7Pi/A/Bm5Yzt7NL5wAAAABJRU5ErkJggg==\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "## Use this and additional cells to continue to explore the dataset. ##\n",
    "## Once you have performed your exploration, document your findings  ##\n",
    "## in the Markdown cell above.          ##\n",
    "cust_data75 = data_hist[(data_hist['duration']<75) & (data_hist['user_type'] == 'Customer')&(data_hist['day_of_week'] == 'Monday')]\n",
    "bin_list=[]\n",
    "for a in range(0,23,1):\n",
    "    bin_list.append(int(a))\n",
    "data_dur=numpy.round(cust_data75['hour']).values.T.flatten()\n",
    "print(max(data_dur))\n",
    "plt.hist(data_dur,bins=bin_list)\n",
    "plt.title('Customer Distribution of hours for Durations less than 75 on Monday')\n",
    "plt.xlabel('Duration (m)')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Above graph left skewed since most of the datd falls to left."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "23\n"
     ]
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "cust_data75 = data_hist[(data_hist['duration']<75) & (data_hist['user_type'] == 'Customer')&(data_hist['day_of_week'] == 'Tuesday')]\n",
    "bin_list=[]\n",
    "for a in range(0,23,1):\n",
    "    bin_list.append(int(a))\n",
    "data_dur=numpy.round(cust_data75['hour']).values.T.flatten()\n",
    "print(max(data_dur))\n",
    "plt.hist(data_dur,bins=bin_list)\n",
    "plt.title('Customer Distribution of hours for Durations less than 75 on Tuesday')\n",
    "plt.xlabel('Duration (m)')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Above graph left skewed since most of the datd falls to left."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "23\n"
     ]
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "cust_data75 = data_hist[(data_hist['duration']<75) & (data_hist['user_type'] == 'Customer')&(data_hist['day_of_week'] == 'Wednesday')]\n",
    "bin_list=[]\n",
    "for a in range(0,23,1):\n",
    "    bin_list.append(int(a))\n",
    "data_dur=numpy.round(cust_data75['hour']).values.T.flatten()\n",
    "print(max(data_dur))\n",
    "plt.hist(data_dur,bins=bin_list)\n",
    "plt.title('Customer Distribution of hours for Durations less than 75 on Wednesday')\n",
    "plt.xlabel('Duration (m)')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Above graph left skewed since most of the datd falls to left."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "23\n"
     ]
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "cust_data75 = data_hist[(data_hist['duration']<75) & (data_hist['user_type'] == 'Customer')&(data_hist['day_of_week'] == 'Thursday')]\n",
    "bin_list=[]\n",
    "for a in range(0,23,1):\n",
    "    bin_list.append(int(a))\n",
    "data_dur=numpy.round(cust_data75['hour']).values.T.flatten()\n",
    "print(max(data_dur))\n",
    "plt.hist(data_dur,bins=bin_list)\n",
    "plt.title('Customer Distribution of hours for Durations less than 75 on Thursday')\n",
    "plt.xlabel('Duration (m)')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Above graph left skewed since most of the datd falls to left."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "23\n"
     ]
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "cust_data75 = data_hist[(data_hist['duration']<75) & (data_hist['user_type'] == 'Customer')&(data_hist['day_of_week'] == 'Friday')]\n",
    "bin_list=[]\n",
    "for a in range(0,23,1):\n",
    "    bin_list.append(int(a))\n",
    "data_dur=numpy.round(cust_data75['hour']).values.T.flatten()\n",
    "print(max(data_dur))\n",
    "plt.hist(data_dur,bins=bin_list)\n",
    "plt.title('Customer Distribution of hours for Durations less than 75 on Friday')\n",
    "plt.xlabel('Duration (m)')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Above graph left skewed since most of the datd falls to left."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "23\n"
     ]
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "cust_data75 = data_hist[(data_hist['duration']<75) & (data_hist['user_type'] == 'Customer')&(data_hist['day_of_week'] == 'Saturday')]\n",
    "bin_list=[]\n",
    "for a in range(0,23,1):\n",
    "    bin_list.append(int(a))\n",
    "data_dur=numpy.round(cust_data75['hour']).values.T.flatten()\n",
    "print(max(data_dur))\n",
    "plt.hist(data_dur,bins=bin_list)\n",
    "plt.title('Customer Distribution of hours for Durations less than 75 on Saturday')\n",
    "plt.xlabel('Duration (m)')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Above graph left skewed since most of the datd falls to left."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "23\n"
     ]
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "cust_data75 = data_hist[(data_hist['duration']<75) & (data_hist['user_type'] == 'Customer')&(data_hist['day_of_week'] == 'Sunday')]\n",
    "bin_list=[]\n",
    "for a in range(0,23,1):\n",
    "    bin_list.append(int(a))\n",
    "data_dur=numpy.round(cust_data75['hour']).values.T.flatten()\n",
    "print(max(data_dur))\n",
    "plt.hist(data_dur,bins=bin_list)\n",
    "plt.title('Customer Distribution of hours for Durations less than 75 on Sunday')\n",
    "plt.xlabel('Duration (m)')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Above graph left skewed since most of the datd falls to left."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "23\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "Text(0.5, 1.0, 'Subscriber Distribution of hours for Durations less than 75 on Monday')"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "cust_data75 = data_hist[(data_hist['duration']<75) & (data_hist['user_type'] == 'Subscriber')&(data_hist['day_of_week'] == 'Monday')]\n",
    "bin_list=[]\n",
    "for a in range(0,23,1):\n",
    "    bin_list.append(int(a))\n",
    "data_dur=numpy.round(cust_data75['hour']).values.T.flatten()\n",
    "print(max(data_dur))\n",
    "plt.hist(data_dur,bins=bin_list)\n",
    "plt.title('Subscriber Distribution of hours for Durations less than 75 on Monday')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Above graph left skewed since most of the datd falls to left."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "23\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "Text(0.5, 1.0, 'Subscriber Distribution of hours for Durations less than 75 on Tuesday')"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "cust_data75 = data_hist[(data_hist['duration']<75) & (data_hist['user_type'] == 'Subscriber')&(data_hist['day_of_week'] == 'Tuesday')]\n",
    "bin_list=[]\n",
    "for a in range(0,23,1):\n",
    "    bin_list.append(int(a))\n",
    "data_dur=numpy.round(cust_data75['hour']).values.T.flatten()\n",
    "print(max(data_dur))\n",
    "plt.hist(data_dur,bins=bin_list)\n",
    "plt.title('Subscriber Distribution of hours for Durations less than 75 on Tuesday')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Above graph left skewed since most of the datd falls to left."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "23\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "Text(0.5, 1.0, 'Subscriber Distribution of hours for Durations less than 75 on Wednesday')"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "cust_data75 = data_hist[(data_hist['duration']<75) & (data_hist['user_type'] == 'Subscriber')&(data_hist['day_of_week'] == 'Wednesday')]\n",
    "bin_list=[]\n",
    "for a in range(0,23,1):\n",
    "    bin_list.append(int(a))\n",
    "data_dur=numpy.round(cust_data75['hour']).values.T.flatten()\n",
    "print(max(data_dur))\n",
    "plt.hist(data_dur,bins=bin_list)\n",
    "plt.title('Subscriber Distribution of hours for Durations less than 75 on Wednesday')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Above graph left skewed since most of the datd falls to left."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "23\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "Text(0.5, 1.0, 'Subscriber Distribution of hours for Durations less than 75 on Thursday')"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "cust_data75 = data_hist[(data_hist['duration']<75) & (data_hist['user_type'] == 'Subscriber')&(data_hist['day_of_week'] == 'Thursday')]\n",
    "bin_list=[]\n",
    "for a in range(0,23,1):\n",
    "    bin_list.append(int(a))\n",
    "data_dur=numpy.round(cust_data75['hour']).values.T.flatten()\n",
    "print(max(data_dur))\n",
    "plt.hist(data_dur,bins=bin_list)\n",
    "plt.title('Subscriber Distribution of hours for Durations less than 75 on Thursday')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Above graph left skewed since most of the datd falls to left."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "23\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "Text(0.5, 1.0, 'Subscriber Distribution of hours for Durations less than 75 on Friday')"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "cust_data75 = data_hist[(data_hist['duration']<75) & (data_hist['user_type'] == 'Subscriber')&(data_hist['day_of_week'] == 'Friday')]\n",
    "bin_list=[]\n",
    "for a in range(0,23,1):\n",
    "    bin_list.append(int(a))\n",
    "data_dur=numpy.round(cust_data75['hour']).values.T.flatten()\n",
    "print(max(data_dur))\n",
    "plt.hist(data_dur,bins=bin_list)\n",
    "plt.title('Subscriber Distribution of hours for Durations less than 75 on Friday')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Above graph left skewed since most of the datd falls to left."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "23\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "Text(0.5, 1.0, 'Subscriber Distribution of hours for Durations less than 75 on Saturday')"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "cust_data75 = data_hist[(data_hist['duration']<75) & (data_hist['user_type'] == 'Subscriber')&(data_hist['day_of_week'] == 'Saturday')]\n",
    "bin_list=[]\n",
    "for a in range(0,23,1):\n",
    "    bin_list.append(int(a))\n",
    "data_dur=numpy.round(cust_data75['hour']).values.T.flatten()\n",
    "print(max(data_dur))\n",
    "plt.hist(data_dur,bins=bin_list)\n",
    "plt.title('Subscriber Distribution of hours for Durations less than 75 on Saturday')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Above graph left skewed since most of the datd falls to left."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "23\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "Text(0.5, 1.0, 'Subscriber Distribution of hours for Durations less than 75 on Sunday')"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "cust_data75 = data_hist[(data_hist['duration']<75) & (data_hist['user_type'] == 'Subscriber')&(data_hist['day_of_week'] == 'Sunday')]\n",
    "bin_list=[]\n",
    "for a in range(0,23,1):\n",
    "    bin_list.append(int(a))\n",
    "data_dur=numpy.round(cust_data75['hour']).values.T.flatten()\n",
    "print(max(data_dur))\n",
    "plt.hist(data_dur,bins=bin_list)\n",
    "plt.title('Subscriber Distribution of hours for Durations less than 75 on Sunday')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Above graph left skewed since most of the datd falls to left."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "City: Washington\n",
      "OrderedDict([('duration', '7.123116666666666'),\n",
      "             ('month', '3'),\n",
      "             ('hour', '22'),\n",
      "             ('day', '31'),\n",
      "             ('user_type', 'Subscriber')])\n",
      "\n",
      "City: Chicago\n",
      "OrderedDict([('duration', '15.433333333333334'),\n",
      "             ('month', '3'),\n",
      "             ('hour', '23'),\n",
      "             ('day', '31'),\n",
      "             ('user_type', 'Subscriber')])\n",
      "\n",
      "City: NYC\n",
      "OrderedDict([('duration', '13.983333333333333'),\n",
      "             ('month', '1'),\n",
      "             ('hour', '0'),\n",
      "             ('day', '01'),\n",
      "             ('user_type', 'Customer')])\n"
     ]
    }
   ],
   "source": [
    "def time_of_trip1(datum, city):\n",
    "\n",
    "    if city=='NYC':\n",
    "        extdt=datetime.strptime(datum['starttime'], \"%m/%d/%Y %H:%M:%S\")\n",
    "        month=int(extdt.strftime(\"%m\"))\n",
    "        hour=int(extdt.strftime(\"%H\"))\n",
    "        day=extdt.strftime(\"%d\")\n",
    "        #print(month,hour,day_of_week)\n",
    "    elif city=='Chicago':\n",
    "        extdt=datetime.strptime(datum['starttime'], \"%m/%d/%Y %H:%M\")\n",
    "        month=int(extdt.strftime(\"%m\"))\n",
    "        hour=int(extdt.strftime(\"%H\"))\n",
    "        day=extdt.strftime(\"%d\")\n",
    "        #print(month,hour,day_of_week)\n",
    "    else:\n",
    "        extdt=datetime.strptime(datum['Start date'], \"%m/%d/%Y %H:%M\")\n",
    "        month=int(extdt.strftime(\"%m\"))\n",
    "        hour=int(extdt.strftime(\"%H\"))\n",
    "        day=extdt.strftime(\"%d\")\n",
    "        #print(month,hour,day_of_week)\n",
    "    \n",
    "    return (month, hour, day)\n",
    "def condense_data1(in_file, out_file, city):\n",
    "    \"\"\"\n",
    "    This function takes full data from the specified input file\n",
    "    and writes the condensed data to a specified output file. The city\n",
    "    argument determines how the input file will be parsed.\n",
    "    \n",
    "    HINT: See the cell below to see how the arguments are structured!\n",
    "    \"\"\"\n",
    "    \n",
    "    with open(out_file, 'w') as f_out, open(in_file, 'r') as f_in:\n",
    "        # set up csv DictWriter object - writer requires column names for the\n",
    "        # first row as the \"fieldnames\" argument\n",
    "        out_colnames = ['duration', 'month', 'hour', 'day', 'user_type']        \n",
    "        trip_writer = csv.DictWriter(f_out, fieldnames = out_colnames)\n",
    "        trip_writer.writeheader()\n",
    "        \n",
    "        ## TODO: set up csv DictReader object ##\n",
    "        trip_reader = csv.DictReader(f_in)\n",
    "\n",
    "        # collect data from and process each row\n",
    "        for row in trip_reader:\n",
    "            # set up a dictionary to hold the values for the cleaned and trimmed\n",
    "            # data point\n",
    "            new_point = {}\n",
    "            \n",
    "\n",
    "            ## TODO: use the helper functions to get the cleaned data from  ##\n",
    "            ## the original data dictionaries.                              ##\n",
    "            ## Note that the keys for the new_point dictionary should match ##\n",
    "            ## the column names set in the DictWriter object above.         ##\n",
    "            month, hour, day = time_of_trip1(row, city)\n",
    "            duration=duration_in_mins(row, city)\n",
    "            user_type=type_of_user(row, city)\n",
    "            new_point[out_colnames[0]]=duration\n",
    "            new_point[out_colnames[1]]=month\n",
    "            new_point[out_colnames[2]]=hour\n",
    "            new_point[out_colnames[3]]=day\n",
    "            new_point[out_colnames[4]]=user_type\n",
    "\n",
    "            ## TODO: write the processed information to the output file.     ##\n",
    "            ## see https://docs.python.org/3/library/csv.html#writer-objects ##\n",
    "            trip_writer.writerow(new_point)\n",
    "            \n",
    "city_info = {'Washington': {'in_file': './data/Washington-CapitalBikeshare-2016.csv',\n",
    "                            'out_file': './data/Washington-2016-Summary_new.csv'},\n",
    "             'Chicago': {'in_file': './data/Chicago-Divvy-2016.csv',\n",
    "                         'out_file': './data/Chicago-2016-Summary_new.csv'},\n",
    "             'NYC': {'in_file': './data/NYC-CitiBike-2016.csv',\n",
    "                     'out_file': './data/NYC-2016-Summary_new.csv'}}\n",
    "\n",
    "for city, filenames in city_info.items():\n",
    "    condense_data1(filenames['in_file'], filenames['out_file'], city)\n",
    "    print_first_point(filenames['out_file'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "data_dur1 = pandas.read_csv('./data/NYC-2016-Summary_new.csv')\n",
    "cust_data1=data_dur1[(data_dur1['duration']<75)]\n",
    "cust_data = cust_data1.groupby(['month','day']).size().reset_index(name='counts')\n",
    "dup = cust_data[cust_data['counts'] == cust_data.groupby(['month'])['counts'].transform(max)]\n",
    "x=numpy.round(dup['month']).values.T.flatten()\n",
    "y=numpy.round(dup['day']).values.T.flatten()\n",
    "plt.scatter(x, y, alpha=0.5)\n",
    "plt.title('Scatter plot pythonspot.com')\n",
    "plt.xlabel('month')\n",
    "plt.ylabel('day')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "cust_data1=data_dur1[(data_dur1['duration']<75) & (data_hist['user_type'] == 'Subscriber')]\n",
    "cust_data = cust_data1.groupby(['month','day']).size().reset_index(name='counts')\n",
    "dup = cust_data[cust_data['counts'] == cust_data.groupby(['month'])['counts'].transform(max)]\n",
    "x=numpy.round(dup['month']).values.T.flatten()\n",
    "y=numpy.round(dup['day']).values.T.flatten()\n",
    "plt.scatter(x, y, alpha=0.5)\n",
    "plt.title('Scatter plot pythonspot.com')\n",
    "plt.xlabel('month')\n",
    "plt.ylabel('day')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "cust_data1=data_dur1[(data_dur1['duration']<75) & (data_hist['user_type'] == 'Customer')]\n",
    "cust_data = cust_data1.groupby(['month','day']).size().reset_index(name='counts')\n",
    "dup = cust_data[cust_data['counts'] == cust_data.groupby(['month'])['counts'].transform(max)]\n",
    "x=numpy.round(dup['month']).values.T.flatten()\n",
    "y=numpy.round(dup['day']).values.T.flatten()\n",
    "plt.scatter(x, y, alpha=0.5)\n",
    "plt.title('Scatter plot pythonspot.com')\n",
    "plt.xlabel('month')\n",
    "plt.ylabel('day')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Conclusion for above scatter plot**\n",
    "\n",
    "Busy days in each month are derived more by subcribers when compare with customers."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<a id='conclusions'></a>\n",
    "## Conclusions\n",
    "\n",
    "Congratulations on completing the project! This is only a sampling of the data analysis process: from generating questions, wrangling the data, and to exploring the data. Normally, at this point in the data analysis process, you might want to draw conclusions about the data by performing a statistical test or fitting the data to a model for making predictions. There are also a lot of potential analyses that could be performed on the data which are not possible with only the data provided. For example, detailed location data has not been investigated. Where are the most commonly used docks? What are the most common routes? As another example, weather has potential to have a large impact on daily ridership. How much is ridership impacted when there is rain or snow? Are subscribers or customers affected more by changes in weather?\n",
    "\n",
    "**Question 7**: Putting the bike share data aside, think of a topic or field of interest where you would like to be able to apply the techniques of data science. What would you like to be able to learn from your chosen subject?\n",
    "\n",
    "**Answer**: This alanysis can be applied to tower to calculate busy hour on the tower and how the tower is performing when busy. And calculating treands of the call duration during peek and non peek hours.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from subprocess import call\n",
    "call(['python', '-m', 'nbconvert', 'Bike_Share_Analysis.ipynb'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "anaconda-cloud": {},
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 1
}
