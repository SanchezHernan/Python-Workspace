# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 10:55:37 2018

@author: Hornyt0x
"""
import requests

def geocoding(address):
    import simplejson

    url_prefix = 'http://maps.googleapis.com/maps/api/geocode/json?sensor=false&address='
    (header, response) = requests(url_prefix + address)

    decoder = simplejson.JSONDecoder()
    dict_ = decoder.decode(response)

    try:
        location = dict_['results'][0]['geometry']['location']
    except IndexError:
        return None

    lat = location['lat']
    lng = location['lng']

    return (lat, lng)
    
if(__name__ =='__main__'):
    #print(geocoder('Rosario del Tala Entre Rios'))
    ciudad = input('Ingrese en nombre de la ciudad: ')
    lat, lng = geocoding(input('ciudad: '))
    print('latitud: ' + str(lat))
    print('longitud: ' + str(lng))