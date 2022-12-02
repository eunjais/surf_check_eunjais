## from requests lib api call
import requests
import os, sys
## from dotenv for env var
from dotenv import load_dotenv
## import from BeachDB object
from BeachDB import BeachDB

load_dotenv()

## define base_url for api call
base_url = 'https://api.worldweatheronline.com/premium/v1/marine.ashx?key='

# define api_key and g_key
api_key = os.environ.get('api_key')

# check if api_key and g_key are available
if not api_key:
    print('missing api_key or g_key')
    sys.exit(1)

## load data
db_beaches = BeachDB()

## util functions
## get formatted request_url
def __get_request_url(beach_obj):
    if not beach_obj:
        return ''
    lat, long = beach_obj.get('latitude', ''), beach_obj.get('longitude', '')
    request_url = "{}{}&format=json&q={},{}".format(base_url, api_key, lat, long)
    return request_url


## get marine data from api
def __fetch_api(beach_list = []):
    marine_data = []
    for beach in beach_list[0: min(len(beach_list), 1)]:
        request_url = __get_request_url(beach)
        r = requests.get(request_url)
        # add data to list if succeeds
        if r.status_code == 200:
            response_data = r.json().get('data', [])
            #marine_data.append(r.json())
            formatted_data = __xform_data(response_data, beach)
            marine_data.extend(formatted_data)
    return marine_data


## get wave size from wave_height
def __get_wave_size(num):
  wave = float(num)
  wave_height_bins = [0, 4, 10, 12]
  wave_size = ['Small (<4)', 'Medium (4-9)', 'Large (10-12)']
  label = ''
  if wave_height_bins[0] <= wave < wave_height_bins[1]:
    label = wave_size[0]
  elif wave_height_bins[1] <= wave < wave_height_bins[2]:
    label = wave_size[1]
  elif wave_height_bins[2] <= wave <= wave_height_bins[3]:
    label = wave_size[2]
  return label

## transfrom marine data
def __xform_data(data, beach_obj):
    if not data: return []
    hourly_data = []
    beach_id = beach_obj.get('beach_id', '')
    beach_name = beach_obj.get('beach_name', '')
    latitude = beach_obj.get('latitude', '')
    longitude = beach_obj.get('longitude', '')
    for w in data.get('weather', []):
        day = w.get('date')
        hourly, astronomy = w.get('hourly'), w.get('astronomy')
        sunrise, sunset = astronomy[0].get('sunrise'), astronomy[0].get('sunset')
        #print(day, sunrise, sunset)

        for h in hourly:
            time = h.get('time')
            if len(time) == 3:
                time = '0' + time
            elif len(time) == 1:
                time = '0000'
            wave_height = h.get('swellHeight_ft')
            weather_description = h.get('weatherDesc')[0].get('value')
            weather_icon = h.get('weatherIconUrl')[0].get('value')
            temperature = h.get('tempF')
            water_temperature = h.get('waterTemp_F')
            wind_speed = h.get('windspeedMiles')
            cloud_cover = h.get('cloudcover')
            wave_size = __get_wave_size(wave_height)
            # append hourly to list
            hourly_data.append({
                'beach_id': beach_id,
                'beach_name': beach_name,
                'latitude': latitude,
                'longitude': longitude,
                'date': day,
                'time': time,
                'sunrise': sunrise,
                'sunset': sunset, 
                'weather_description': weather_description, 
                'temperature': temperature, 
                'water_temperature': water_temperature, 
                'wind_speed': wind_speed,
                'cloud_cover': cloud_cover,
                'weather_icon': weather_icon,
                'wave_height': wave_height, 
                'wave_size': wave_size,
            })
    return hourly_data


def get_weather_data(search_query):
    # get beach results
    beach_results = db_beaches.search_beaches(search_query)
    marine_data = __fetch_api(beach_results)
    return marine_data


