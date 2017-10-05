import json
import argparse
from math import sin, cos, radians, sqrt, asin


def calc_distance(lon1, lat1, lon2, lat2):
    radius_km = 6371
    delta_lat = radians(lat2 - lat1)
    delta_long = radians(lon2 - lon1)
    hav = (sin(delta_lat/2)**2 +
           cos(radians(lat1)) *
           cos(radians(lat2)) *
           (sin(delta_long/2)**2))
    bar_distance = 2 * radius_km * asin(sqrt(hav))
    return bar_distance


def load_data(file_path):
    with open(file_path, 'r') as json_file:
        json_obj = json.load(json_file)
        return json_obj


def get_biggest_bar(json_bars):
    biggest_bar = max(
       json_bars, key=lambda x: x['properties']['Attributes']['SeatsCount'])
    return biggest_bar


def get_smallest_bar(json_bars):
    smallest_bar = min(
        json_bars, key=lambda x: x['properties']['Attributes']['SeatsCount'])
    return smallest_bar


def get_closest_bar(json_bars, longitude, latitude):
    closest_bar = min(
        json_bars,
        key=lambda x: (calc_distance(longitude, latitude,
                                     *x['geometry']['coordinates'])))
    return closest_bar


def format_bar_data(bar_desc, bar_json):
    bar_info = """{desc}:
    Бар: {name}
    Мест в баре: {seats}
    Адрес: {address}, {district}
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


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input',
                        help='JSON file with bars',
                        required=True)
    return parser.parse_args()


if __name__ == '__main__':
    args = get_args()
    json_data = load_data(args.input)
    json_bar_list = json_data['features']

    print(format_bar_data("Самый большой бар",
                          get_biggest_bar(json_bar_list)))

    print(format_bar_data('Самый маленький бар',
                          get_smallest_bar(json_bar_list)))

    in_longitude = float(input("input your longitude: "))
    in_latitude = float(input("input your latitude: "))

    print(format_bar_data('Ближайший бар',
                          get_closest_bar(json_bar_list,
                                          in_longitude,
                                          in_latitude)))
