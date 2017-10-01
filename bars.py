import sys
import json
from math import sin, cos, radians, sqrt, asin


def distance(lon1, lat1, lon2, lat2):
    """
    Using haversine formula - https://en.wikipedia.org/wiki/Haversine_formula
    """

    radius = 6371  # km
    dlat = radians(lat2-lat1)
    dlon = radians(lon2-lon1)
    hav = sin(dlat/2)**2 + cos(radians(lat1)) * cos(radians(lat2)) * (sin(dlon/2)**2)
    distance = 2 * radius * asin(sqrt(hav))

    return distance


def load_data(filepath):
    with open(filepath, 'r') as json_file:
        json_obj = json.load(json_file)
        return json_obj


def get_biggest_bar(json_bars):
    biggest_bar = max(json_bars, 
                      key=lambda x: x['properties']['Attributes']['SeatsCount'])
    return biggest_bar


def get_smallest_bar(json_bars):
    smallest_bar = min(json_bars, 
                       key=lambda x: x['properties']['Attributes']['SeatsCount'])
    return smallest_bar


def get_closest_bar(json_bars, longitude, latitude):
    closest_bar = min(json_bars, key=lambda x: (distance(longitude, latitude,
                                                *x['geometry']['coordinates'])))
    return closest_bar

def format_bar_data(bar_desc, bar_json):
    bar_info = """{desc}:
    Бар {name}  на {seats}  мест
    Адрес {address}, {district}
    Координаты: {lng}, {lat}
    """.format(desc=bar_desc,
               name=bar_json['properties']['Attributes']['Name'],
               seats=bar_json['properties']['Attributes']['SeatsCount'],
               address=bar_json['properties']['Attributes']['Address'],
               district=bar_json['properties']['Attributes']['District'],
               lng=bar_json['geometry']['coordinates'][0],
               lat=bar_json['geometry']['coordinates'][1]
               )
    return bar_info

if __name__ == '__main__':
    json_data = load_data(sys.argv[1])
    json_bars = json_data['features']

    print(format_bar_data("Самый большой бар", get_biggest_bar(json_bars)))

    print(format_bar_data('Самый маленький бар', get_smallest_bar(json_bars)))

    longitude = float(input("input your longitude: "))
    latitude = float(input("input your latitude: "))

    print(format_bar_data('Ближайший бар', get_closest_bar(json_bars,longitude, latitude)))

