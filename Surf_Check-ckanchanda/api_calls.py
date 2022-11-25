# Import the requests library.
import requests
#from citipy import citipy
import pandas as pd
import numpy as np
import time
from datetime import datetime
import json as js

# Import the API key.
from config import api_key
api_key = "1d33ea93dff947868fd183328222411" 

beach = beaches_df['beach_name']
lat = beaches_df['latitude']
long = beaches_df['longitude']
coordinates = list(beaches_lat_lngs)


# Starting URL for Weather Map API Call.
url = 'http://api.worldweatheronline.com/premium/v1/marine.ashx?key=' + api_key + BEACH
beach_url = url + "&format=json&q=" + str(lat) + "," + str(long)

response = requests.get(beach_url).json()