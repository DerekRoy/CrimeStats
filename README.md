GOAL
The goal of this report is to analyze crime data in an effort to give vancouver law enforcement insight on where crimes are happening, when crimes are most prevalent, what types of crime are being committed, and how resources might be allocated to better prevent or catch criminals.

DATA
For this project there were three different data sets:
1. Vancouver Crime 2002 - 2018 from the the Vancouver data catalogue at:
data.vancouver.ca
2. Weather data from 2013 - 2017 collected at YVR INT A weather terminal.
3. Census information from 2016 from: ​data.vancouver.ca​ (This data was unused due to
time constraints)

The crime data contained Type, Year, Month, Day, Block of Neighborhood, Policing
Neighborhood, X(UTM Zone 10), and Y (UTM Zone 10). Data from 2018 was removed so it would not affect the year to year averages. A column containing the day of week was then added for future processing within the program. After these initial changes more data was separated into crimes by type of crime.
Weather data was imported and processed so that the first 22 lines of text was removed in order to get the data neatly into a pandas dataframe. Several different years of weather were appended together and the values were narrowed down to Year, Month, Day, and Temperature.
Census data in an .xls file was difficult to import, so ultimately there was no more time left to bring in the data and do something meaningful with it.

PROCESSING
The first task was to break the data into time segments to find some information on when crimes take place in Vancouver. After plotting the yearly trend of crime, crimes were graphed by type. There was a marked decrease in most types of crime, but a rise in theft from vehicles, mischief, other types of theft, and murder. The data set on murder in this case is very small and hasn’t risen dramatically.

The next step in this analysis was a monthly average break down. Vancouver’s crime rate drops dramatically from October to February, and then ramps up in the summer months.

The average temperature per month and the amount of crime are 60.82% correlated, meaning there is a high chance that crime rises with temperature. Linear regression was used to find the correlation value, which was squared to find the correlation of the two data sets. In the per month average by crime type, bike theft is identical in shape to average temperature per month. In fact after running a correlation test it turns out that weather and bike theft are 96.87% correlated. With good weather people in Vancouver tend to bike more leading to more potential incidents of theft. With these metrics the Vancouver Police Department (VPD) should consider bringing more staff on in May for the crime peak in July and August, and then look at cutting back slightly coming into December.

The daily break down jumps in the beginning, middle, and end of the month. Here we see crimes like theft from cars, mischief, and commercial break-ins rising on the first and fifteenth of the month. One could assume that this is due to biweekly pay, and that more people are out on the streets with money. This is perfectly mirrored when plotting average crimes per day of the week. Again there is a peak when during the weekend when there are very few obligations for people to fulfill. Theft from a car, mischief, commercial and residential break-ins, and many other crimes start to increase from Friday onwards.

Looking at crimes per hour gives us an even better picture of when crimes are occuring. Looking at time based figures, it may be shocking to see the wide array of crimes happening throughout the day. Peak crime times can be seen anywhere from midnight to three in the afternoon. KMeans was used to determine an area of patrol for police officers where crimes are most likely to occur. It found the ideal patrol locations based on each crime type during its peak hour of activity. Knowing this will reduce some of the most common crimes in the Vancouver area, and the cluster can be changed in the KMeans tool. Currently the clustering is set to thirteen, but can be readjusted dependent on patrol quantity. We created a map of vancouver that shows the general crime areas by using a low alpha variable in the plot. We saw that the central business district encounters a lot of crime.

SUMMARY
- Vancouver crime is correlated to the weather with peak months being from June to August
- Each month crime increases on the 1st and 15th
- Crimes increase in frequency on Friday and Saturday
- Most crime peaks at midnight through the night, though there are also daytime peaks
- Based on common crime peak hours there are ideal areas to patrol to prevent crime
- Vancouver’s major crime districts are the Central Business district and West End
TECHNIQUES
- Linear Regression
- KMeans
- Data Visualization
- Pandas Dataframes
- Seaborn plotting
- Matplotlib.pyplot
- Correlation coefficients
LIMITATIONS
   
It was difficult implementing a wide variety of machine learning tools, and I would have liked to utilize that more for in depth results. I would have also liked to use more statistical tests to check data to prove my hypothesis. KMeans could have been implemented with much more care than was used.
Crime Data Analysis
Summer 2018 Computational Data Analysis
- Applied linear regression to data to determine statistical correlation of variables.
- Computed KMeans classifier locations to determine locations best suited for patrol to
prevent crime.
- Implemented data visualization techniques to give further insights into trends in crime
data.
- Coded files into pandas data frames for processing.
- Planned a project itinerary that lead my team to meet each goal on time.
