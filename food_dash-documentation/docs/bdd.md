## Behavior-Driven-Development

### Title
COVID-19 food consumption Dashboard

### Narrative

#### Feature 1. For clean_normalize_data.py 

##### Feature 1.1: function cleaning_data

###### As an: 
researcher dealing with time and county-level aggregated data, it remains common to witness alot of issues when attempting to wrangle the data. Some very common elements include (A) having county FIPS IDs stored as integers instead of strings, (B) having 4-digit instead of the rightful 5-digit FIPS codes as a result of having FIPS IDs stored as integers (in A), (C) having time stored as a datetime instead string/INT;  

######  I want: 

the correct information (ie data type in A-C above) to be reflected in my data. This includes ensuring that county IDs are accurately reflected as a 5-digit FIPS string, having time stored as a datetime instead string/INT, and ensuring that both the FIPS and datetimes are set as an index as its respective columns. 

######  so that: 

Firstly, it will be easier to deal with the data from all aspects later. This could include making additional computations, running regression models or feeding the data into the dashboard (which in this overarching project is our goal). Failing to use this clean_data function could 'corrupt' and add distress to our latter processes.  

##### Feature 1.2 and 1.3: function merging_data and calculating_reliance

###### As an: 
Researcher looking to compute reliance of unhealthy food choices in spatio-temporal dimensions (ie the spatial aspects are the counties and the temporal aspects are the monthly-level time-frames), these two sub-features are targetted towards helping me merge the data before calculating the appropriate reliances for unhealthy food-consumption. 



###### I want: 

to have features that will allow me to 'spit-out' a dataframe that contains my "unhealthy reliance" metric based on my specified attribute of interest. To do so, in feature 1.2 (merging_data) we merge the dataframes containing the attributed of interest and in feature 1.3 (calculating_reliance) we feed the merged dataframes with the respective attributes deemed of "unhealthy reliance" such that feature 1.3 is able to automatically return to us a normalized dataframe containing our "unhealthy reliance" metric of interest. 



###### so that: 

we can obtain (A) a normalized dataframe with our "unhealthy reliance" metric based on our specified unhealthy attributes and (B) using this normalized dataframe, we can feed it into the spatio_temporal_dash.py file. The goal of this file is to return to us a spatio-temporal dashboard. 


##### Feature 1.4: function saved_normalized 

##### As an:  

Researcher dealing with large amounts of data across multiple spatial and temporal dimensions, of which, at this feature point, we have conducted alot of wrangling work. Thus, having this function that will save our normalized data in a simple and efficient manner for easy retrieval is critical. 


###### I want: 

to efficiently normalize data that is of importance to us and save them in a streamlined and efficient manner

###### so that: 

I could understand the workflow of my (A) research progress and (B) extract these datasets whenever it is needed in an efficient manner. (so I wouldn't have to redo the entire workflow again). 


##### Feature 1.5: function preparing_data_for_viz

###### As an:  

Researcher whose ultimate goal is to have a dataframe which could be directly read into spatio_temporal_dash.py (this function will spit out a spatio-temporal dashboard)


###### I want: 

have functions, which calls the above-mentioned functions, and produces a dataframe with my "unhealthy reliance" metric calculated and my spatial (ie county-level FIPS ID) and temporal (ie monthly datetime) clearly identified. 

###### so that: 

We could fun this function, of which the output could simply be fed into spatio_temporal_dash.py (this function will spit out a spatio-temporal dashboard), in a manner whereby spatio_temporal_dash.py is solely focused on the visual aspects of the dashboard, instead of trying to wrangly through untidy and uncleaned datasets while trying to process a spatio-temporal dashboard, which can prove to be tricky. 



#### Feature 2. For dashboard_creation.py

###### As an

Researcher looking to generate a spatial temporal dashboard for my readers and the journal editors 

###### I want 

To be able to generate a function that 'spits out' a spatial-temporal dashboard with ease (ie one line of code which simply calls the function)

###### so that 

the spatial temporal dashboard is done in a simple and visually appeasing manner and individuals wishing to do something similar (ie replicate the dashboard with the same or a different dataset) could do so by simply calling this function. 

###  Acceptance criteria

#### Feature 1. For clean_normalize_data.py 

##### Given 

That a researcher has a numerous US census county-level dataset which takes place across numerous monthly scales. 

##### When 

a typical CSV file from most conventional data sources (including those of the .gov websites) produces (A) extremely undesirable columns (for example the 5-digit FIPS code is an INT rather than a string and some of the '0's at the fore have been removed as a result OR time is saved as a STR instead of DATETIME), 

AND 

The researcher wants to calculate a proportional metric that requires divisional computation of attributes scattered across distinct datasets. 

##### Then

The researcher could utilize and call the relevant functions from clean_normalize_data.py to perform cleaning and saved the normalized dataset, of which it will be expected to be used for futuristic purposes, of which in my case, it is to prepare a 'cleaned' and 'tidy' dataset for a dashboard. Other cases could include preparing it for spatial or time-series regression/panel models. 


#### Feature 2. For spatio_temporal_dash.py

##### Given 

A researcher wants to proudce a spatial-temporal dashboard with ease 

##### When 

he/she has a cleaned/tidy dataset with the appropriate ID column linking it to the spatial elements (such as county/cbg/state) and a datetime column linking it with the temporal elements of the dataset in which he/she intends to visualize. 

##### Then 

This function can be called upon (of which the dataset is fed into) to produce and 'spit-out' a spatio-temporal dashbaord with ease, thus saving time and energy needed to visualize the multi-dimensional aspects of spatial-temporal data. 

