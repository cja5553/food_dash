### User Guide

#### clean_normalize_data

##### <sub>clean_normalize_data.cleaning_data(data)</sub>

Reads the data with the aggregated visit counts and converts the columns into its neccessary data type. 
Returns the DataFrame with columns converted to its appropriate types and inappropriate values fixed. This includes converting counties to strings, filling them up with 0's if they are 4-digits long, and converting dates into datetimes. 

- **data**(*pandas.DataFrame*) - this arguement takes a dataFrame with at least 3 columns (1) the aggregated visitation counts for each county on each month, (2) the county FIPS code, and (3) the month (or date). It assumes that dates are titled ``date_range_start``, and counties are titled ``County``. 

##### <sub>clean_normalize_data.merging_data(df1,df2)</sub>

Merges the specified 2 dataFrames based on ``Month`` and ``County`` set as the index of the dataFrames. 

Returns 1 merged DataFrame containing attributes from both the DataFrames, based on each ``Month`` on each ``County``

- **df1**(*pandas.dataFrame*) - this arguement takes a first dataFrame with at least 3 columns (1) the aggregated visitation counts for each county on each month, (2) the county FIPS code, and (3) the month (or date). It assumes that the columns contains the appropriate data types. Feed it into the ``cleaning_data`` if the columns do not contain the appropriate data types. 

- **df2**(*pandas.dataFrame*) - same as ``df1``


##### <sub>clean_normalize_data.calculating_reliance(data,unhealthy_col_name,healthy_col_name,desired_col_name)</sub>

Takes a DataFrame with one column as the ``unhealthy_col_name`` and another as the ``healthy_col_name``. 

Returns DataFrame with the computed *unhealthy reliance index* for each specified ``County`` on each ``Month`` - calculated by ``unhealthy_col_name``/(``unhealthy_col_name``+``healthy_col_name``). 

- **data**(*pandas.dataFrame*) - takes a dataFrame which contains the following columns: ``County``, ``Month``, the specified ``unhealthy_col_name``, and ``unhealthy_col_name``

- **unhealthy_col_name**(*str*) - Name of the column of which we wish to identify as our unhealthy element, of which we will calculate our "unhealthy reliance index" by. 

- **healthy_col_name**(*str*) - Name of the column of which we wish to identify as our healthy element. 

- **desired_col_name**(*str*) - Column Name of our specified "unhealthy reliance index", to which the data frame of our output will reflect  


##### <sub>clean_normalize_data.preparing_data_for_viz(df1,df2,unhealthy_col_name,healthy_col_name,desired_col_name)</sub>

Combines all the above functions together (ie ``calculating_reliance()``, ``merging_data()``,``cleaning_data()``). 

Returns an output of a DataFrame that is ready to be fed into the functions used to construct the Dashboard. 

- **df1**(*pandas.dataFrame*): Refer to ``merging_data`` above
- **df2**(*pandas.dataFrame*): Refer to ``merging_data`` above
- **unhealthy_col_name**(*str*): Refer to ``preparing_data_for_viz`` above. 
- **healthy_col_name**(*str*): Refer to ``preparing_data_for_viz`` above. 
- **desired_col_name**(*str*): Refer to ``preparing_data_for_viz`` above. 



#### dashboard_creation

##### dashboard_creation.loading_counties_file()

Returns the county shapefiles. 

##### dashboard_creation.green_red_col_scale()

Returns the scale of which we use to visualize our dashboard. The scale ranges from 0 to 1, with 0 being dark-red in color to 1 being green in color. Here 0 is assumed to be the worst and 1 is assumed to be the best. 

##### dashboard_creation.show_and_save_plot(save_name,attribute_name,cc_scale,data, counties)

Returns a Dashboard and saves the dashboard based on the assigned ``save_name``

- **save_name**(*str*): Name and folder location of where we wish to save our Dashboard

- **attribute_name**(*str*): Column of the variable of interest that we wish to spatio-temporally visualize in our dashboard. 

- **cc_scale**(*dict*): dictionary of the color scales and its corresponding values which we wish to have displayed on our dashboard. 

- **data**(*pandas.DataFrame*): dataFrame of our data to be used to construct our dashboard. 

- **counties**(*json shpfile*): json shapefile of our counties. 



