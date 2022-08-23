# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 12:54:48 2017

@author: sanch
"""

# Using Python requests and the Google Maps Geocoding API.
#
# References:
#
# * http://docs.python-requests.org/en/latest/
# * https://developers.google.com/maps/

import requests

GOOGLE_MAPS_API_URL = 'http://maps.googleapis.com/maps/api/geocode/json'
#api_key = 'AIzaSyBMpB8Bx2MqVkX56Vo7Tz9NuKLh_Pwz6iY'


# Do the request and get the response data
def geocoder(direccion):
    params = {
    'address': direccion,
    'sensor': 'false'
    }
    
    req = requests.get(GOOGLE_MAPS_API_URL, params=params)
    res = req.json()

    # Use the first result
    result = res['results'][0]

    geodata = {}
    geodata['lat'] = result['geometry']['location']['lat']
    geodata['lng'] = result['geometry']['location']['lng']

    return geodata

if(__name__ =='__main__'):
    #print(geocoder('Rosario del Tala Entre Rios'))
    ciudad = input('Ingrese en nombre de la ciudad: ')
    geo = geocoder(ciudad + ', Entre Rios')
    print('latitud: ' + str(geo['lat']))
    print('longitud' + str(geo['lng']))