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
    bars_dict = dict(map(lambda x: (x['properties']['Attributes']['SeatsCount'], x),
                     json_bars['features']))

    biggest_bar = bars_dict[max(bars_dict)]
    return biggest_bar


def get_smallest_bar(json_bars):
    bars_dict = dict(map(lambda x: (x['properties']['Attributes']['SeatsCount'], x),
                     json_bars['features']))
    smallest_bar = bars_dict[min(bars_dict)]
    return smallest_bar


def get_closest_bar(json_bars, longitude, latitude):
    bars_dict = dict(map(lambda x: (distance(longitude, latitude,
                     *x['geometry']['coordinates']), x),
                     json_bars['features']))
    closest_bar = bars_dict[min(bars_dict)]
    return closest_bar


if __name__ == '__main__':
    json_bars = load_data(sys.argv[1])
    print("The biggest bar is %s" % json.dumps(get_biggest_bar(json_bars), indent=4,
          indent=4, ensure_ascii=False))
    print("The smallest bar is %s" % json.dumps(get_smallest_bar(json_bars),
          indent=4, ensure_ascii=False))
    longitude = float(input("input your longitude: "))
    latitude = float(input("input your latitude: "))
    print("The closest bar: %s" % json.dumps(get_closest_bar(json_bars, longitude, latitude),
          indent=4, ensure_ascii=False))
