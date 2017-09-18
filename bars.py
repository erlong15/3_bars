import sys
import json
import math

def distance(lon1, lat1, lon2, lat2):
    radius = 6371 # km

    dlat = math.radians(lat2-lat1)
    dlon = math.radians(lon2-lon1)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = radius * c

    return d

def load_data(filepath):
    with open(filepath, 'r') as json_file:
        json_obj = json.load(json_file)
        return json_obj


def get_biggest_bar(json_bars):
    max_seats = 0
    biggest_bar = None
    for bar in json_bars['features']:
        bar_seats = bar['properties']['Attributes']['SeatsCount']
        if bar_seats > max_seats:
            max_seats = bar_seats
            biggest_bar = bar
    return biggest_bar


def get_smallest_bar(json_bars):
    smallest_bar = json_bars['features'][0]
    min_seats = smallest_bar['properties']['Attributes']['SeatsCount']
    for bar in json_bars['features']:
        bar_seats = bar['properties']['Attributes']['SeatsCount']
        if bar_seats < min_seats:
            min_seats = bar_seats
            smallest_bar = bar
    return smallest_bar


def get_closest_bar(json_bars, longitude, latitude):
    closest_bar =json_bars['features'][0]
    min_distance = distance(longitude, latitude, *closest_bar['geometry']['coordinates'])
    for bar in json_bars['features']:
        bar_distance = distance(longitude, latitude, *bar['geometry']['coordinates'])
        if bar_distance < min_distance:
           min_distance = bar_distance
           closest_bar = bar
    return closest_bar


if __name__ == '__main__':
    json_bars = load_data(sys.argv[1])
    print("The biggest bar is %s" % json.dumps(get_biggest_bar(json_bars), indent=4, ensure_ascii=False))
    print("The smallest bar is %s" % json.dumps(get_smallest_bar(json_bars), indent=4, ensure_ascii=False))
    longitude = float(input("input your longitude: "))
    latitude = float(input("input your latitude: "))
    print("The closest bar: %s" % json.dumps(get_closest_bar(json_bars, longitude, latitude), indent=4, ensure_ascii=False))
