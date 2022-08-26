from sqlite3 import paramstyle
from textwrap import indent
# from urllib
import requests
import streamlit as st
import datetime
import pandas as pd

'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the  functions
''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''

'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a  file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The  package 💡
'''

# USER INPUTS

# Date
date_input = st.date_input(
    "When would you like to go",
    datetime.datetime(2019, 7, 6, 10, 10, 0))
st.write('Your pickup time is:', date_input)

time_input = st.time_input(
    "When would you like to go",
    datetime.time())
st.write('Your pickup time is:', time_input)

datetime_input = f"{date_input} {time_input}"

# pickup longitude
pickup_longitude_input = st.number_input('Insert a pickup longitude', -73.950655)
st.write('The pickup longitude is ', pickup_longitude_input)

# pickup latitude
pickup_latitude_input = st.number_input('Insert a pickup latitude', 40.783282)
st.write('The pickup latitude is ', pickup_longitude_input)

# dropoff longitude
dropoff_longitude_input = st.number_input('Insert a dropoff longitude', -73.950655)
st.write('The pickup longitude is ', dropoff_longitude_input)

# dropoff latitude
dropoff_latitude_input = st.number_input('Insert a dropoff latitude', 40.783282)
st.write('The pickup latitude is ', dropoff_latitude_input)

# passenger count
passenger_count_input = st.number_input('Insert a number of passenger', 1)
st.write('The current number is ', passenger_count_input)

#Params Dict
my_params = dict(
        pickup_datetime=datetime_input,
        pickup_longitude=pickup_longitude_input,
        pickup_latitude=pickup_latitude_input,
        dropoff_longitude=dropoff_longitude_input,
        dropoff_latitude=dropoff_latitude_input,
        passenger_count=passenger_count_input)


url = 'https://taxifare-experiment-lzj6yiwoga-ew.a.run.app/predict'
# url = "https://taxifare.lewagon.ai/predict"

r = requests.get(url, params=my_params).json()

fare = r["fare_amount"]

st.markdown(
    '**Your fare will be:**  '
    )
fare


if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')
