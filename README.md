# CrimeStats

GOAL    

The goal of this report is to analyze crime data in an effort to give vancouver law enforcement insight on where crimes are happening, when crimes are most prevalent, what types of crime are being committed, and how resources might be allocated to better prevent or catch criminals. 

DATA

For this project there were three different data sets: 
Vancouver Crime 2002 - 2018  from the the Vancouver data catalogue at: data.vancouver.ca
Weather data from 2013 - 2017 collected at YVR INT A weather terminal. 
Census information from 2016 from: data.vancouver.ca (This data was unused due to time constraints)

The crime data contained Type, Year, Month, Day, Block of Neighborhood, Policing Neighborhood, X(UTM Zone 10), and Y (UTM Zone 10). Data from 2018 was removed so as not to affect averages year to year. A column containing day of week was then added for future processing within the program. After these initial changes more data was separated into crimes by type of crime. 

Weather data was imported and processed so that the first 22 lines of text was removed in order to get the data neatly into a pandas dataframe. Several different years of weather were appended together and values were narrowed down to Year, Month, Day, and Temperature.

Census data, in .xls file, was difficult to import, and ultimately there was no more time left to bring in the data, and do something meaningful with it. 

open Final Project.ipynb to take a look at what has been done
