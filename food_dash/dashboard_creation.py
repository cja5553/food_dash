#using plotly for an animated choropleth map
import plotly.express as px
import pandas as pd
import datetime
import json
from urllib.request import urlopen

# loading the counties
def loading_counties_file():
  with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response: # loading counties from this plotly url. 
    counties = json.load(response)
  return(counties)

# this function here provides the red-to-green color scale that we intend to use for our dashboard
# The plotly function provides some colors but they are usual scales of one color (eg blue)
def green_red_col_scale():
  colors = ["#3ba513", "#51d320","#9bf778","#e6836f","#ee3c1a","#7c2818"] # getting the colors
  cc_scale=[]
  for i in range(0,6,1):
    current_col=[(i/5),colors[i]] # setting the bin range for each color
    cc_scale.append(current_col)
  return(cc_scale)
    
def show_and_save_plot(save_name,attribute_name,cc_scale,data, counties):
  # identifying the attributes for our choropleth_mapbox
  fig = px.choropleth_mapbox(data_frame=data, geojson=counties, locations=data.county, center={'lat':37.0902, 'lon':-95.7129},  mapbox_style='open-street-map', color=attribute_name, color_continuous_scale=cc_scale, animation_frame='month', opacity=0.6,zoom=2)
  # removing the boundaries as county is so refined, it having boundaries becomes a nuisance
  fig.update_traces(marker_line_width=0)
  # saving the names
  fig.write_html(save_name)
  fig.show()
