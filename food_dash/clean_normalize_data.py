import pandas as pd
import datetime

def cleaning_data(data):
    # converting county columns to string from integer
    (data["county"]) = (data["county"]).astype(str)
    
    # For counties with 4 digits, we will add a 0 at the front
    (data["county"]) = (pd.Series(data.county)).str.pad(width=5, fillchar="0")
    
    # converting dates in the "date_range_start" to actual dates
    format = '%Y-%m' 
    data["date_range_start"]=pd.to_datetime(data["date_range_start"], format=format)
    data = data.rename(columns={'date_range_start': 'month'})
    
    # changing the name of the counts of each dataframe to reflect the type of food-consumption in which we are counting
    new_type_name=str(data["type"][0])+str("_count")
    data = data.rename(columns={'month_count':new_type_name})
    data=data.drop(["type"],axis=1)
    data=data.set_index(['month','county']) # setting the index. 
    return(data)

def merging_data(df1,df2):
    # performing a join
    merged_data=df1.join(df2, how="outer")
    merged_data=merged_data.fillna(0) # rows with NA are simply 0 now 
    return(merged_data)

def calculating_reliance(data,unhealthy_col_name,healthy_col_name,desired_col_name):
    # calculating what we define as unhealthy food reliance (for both fast-food and convenience store) per our paper
    data[desired_col_name]=data[unhealthy_col_name]/(data[unhealthy_col_name]+data[healthy_col_name])
    # we only want to data with the "unhealthy food reliance" score, and no longer need the aggregated counts of each element, so we remove these respective columns
    data=data.drop([unhealthy_col_name, healthy_col_name], axis=1)
    return(data)
    
def preparing_data_for_viz(df1,df2,unhealthy_col_name,healthy_col_name,desired_col_name):
    # cleaning the 2 datasets
    df1_new=cleaning_data(df1)
    df2_new=cleaning_data(df2)
    # merging them together
    merged_data=merging_data(df1_new,df2_new)
    
    # calculating the reliance based on our specified unhealthy attribute. 
    viz_ready_data=calculating_reliance(merged_data,unhealthy_col_name,healthy_col_name,desired_col_name)
    
    # Because dashboards on plotly do not handle indexes well, we remove the respective indexes
    viz_ready_data=viz_ready_data.reset_index()
    
    # because choropleth_mapbox do not handle datetime stamps very well, we have to convert them back into strings. 
    viz_ready_data['month'] = viz_ready_data['month'].dt.strftime('%Y-%m')
    return(viz_ready_data)
