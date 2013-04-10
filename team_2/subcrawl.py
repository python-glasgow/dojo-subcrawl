import re
from requests import get

stations = [
    'Bridge Street SPT Subway Station',
    'West Street SPT Subway Station',
    'Shields Road SPT Subway Station',
    'Kinning Park SPT Subway Station',
    'Cessnock SPT Subway Station',
    'Ibrox SPT Subway Station',
    'Govan SPT Subway Station',
    'Partick SPT Subway Station',
    'Kelvinhall SPT Subway Station',
    'Hillhead SPT Subway Station',
    'Kelvinbridge SPT Subway Station',
    'St Georges Cross SPT Subway',
    'Cowcaddens SPT Subway ',
    'Buchanan Street SPT Subway Station',
    'St Enoch SPT Subway Station',
]

locations = [
    '-4.258747,55.851902',
    '-4.265957,55.849495',
    '-4.275398,55.849976',
    '-4.287758,55.850555',
    '-4.294453,55.852097',
    '-4.304752,55.854603',
    '-4.310589,55.862309',
    '-4.308701,55.869820',
    '-4.300117,55.870880',
    '-4.293423,55.875214',
    '-4.280205,55.873962',
    '-4.267502,55.872036',
    '-4.259777,55.868954',
    '-4.253426,55.862499',
    '-4.255314,55.857300',
]

locations = [','.join(reversed(location.split(","))) for location in locations]


ADDRESS = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?&opennow=true&location=%s&rankby=distance&sensor=false&types=bar&key=AIzaSyD4_M9VE56pyf037YQ_OnEl33J-8EVZYoM'
DIRECTIONS = 'https://maps.googleapis.com/maps/api/directions/json?origin=%s&destination=%s&mode=walking&sensor=false'

from datetime import datetime, timedelta

today = datetime.now().today() + timedelta(days=1)
start_time = datetime(today.year, today.month, today.day, 11, 0, 0)

visited = []

STOP_TIME = 25
SUBWAY_TIME = 6

last_time = start_time


def remove_html_tags(data):
    p = re.compile(r'<.*?>')
    return p.sub(' ', data)

for i, (location, station) in enumerate(zip(locations, stations)):

    print last_time, station, "\n"

    url = ADDRESS % location
    results = get(url).json()

    for result in results['results']:
        if result['id'] not in visited:
            pub = result['name']
            visited.append(result['id'])
            pub_lat_lng = ','.join(map(str, [result['geometry']['location']['lat'], result['geometry']['location']['lng']]))
            break

    directions_url = DIRECTIONS % (location, pub_lat_lng)

    directions_json = get(directions_url).json()

    leg = directions_json['routes'][0]['legs'][0]

    duration = timedelta(seconds=leg['duration']['value'])

    last_time = last_time + duration

    directions_json['routes'][0]['legs']

    for step in leg['steps']:
        print "\t", remove_html_tags(step['html_instructions'])

    print "\n", last_time, pub

    last_time = last_time + timedelta(minutes=STOP_TIME)

    print last_time, "LEAVE\n"

    directions_url = DIRECTIONS % (pub_lat_lng, location)

    directions_json = get(directions_url).json()

    leg = directions_json['routes'][0]['legs'][0]

    duration = timedelta(seconds=leg['duration']['value'])

    last_time = last_time + duration

    directions_json['routes'][0]['legs']

    for step in leg['steps']:
        print "\t", remove_html_tags(step['html_instructions'])

    print "\n"
