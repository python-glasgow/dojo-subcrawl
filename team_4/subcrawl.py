#!/usr/bin/env python
import requests
import pprint
import datetime

places = [
    {'lat': '55.875833', 'lng': '-4.292222', 'station': 'Hillhead'},
    {'lat': '55.874167', 'lng': '-4.280556', 'station': 'Kelvinbridge'},
    {'lat': '55.871944', 'lng': '-4.269722', 'station': "St George's Cross"},
    {'lat': '55.868333', 'lng': '-4.259167', 'station': 'Cowcaddens'},
    {'lat': '55.86245659999999', 'lng': '-4.2534051', 'station': 'Buchanan St'},
    {'lat': '55.856944', 'lng': '-4.255833', 'station': 'St Enoch'},
    {'lat': '55.851667', 'lng': '-4.258611', 'station': 'Bridge Street'},
    {'lat': '55.85', 'lng': '-4.265278', 'station': 'West Street'},
    {'lat': '55.850278', 'lng': '-4.274444', 'station': "Shield's Road"},
    {'lat': '55.850833', 'lng': '-4.288056', 'station': 'Kinning Park'},
    {'lat': '55.8525', 'lng': '-4.295833', 'station': 'Cessnock'},
    {'lat': '55.854444', 'lng': '-4.305278', 'station': 'Ibrox'},
    {'lat': '55.8625', 'lng': '-4.311389', 'station': 'Govan'},
    {'lat': '55.8698', 'lng': '-4.3092', 'station': 'Partick'},
    {'lat': '55.871111', 'lng': '-4.300556', 'station': 'Kelvinhall'},
]

for place in places:
    ll = "%s,%s" % (place['lat'], place['lng'])
    payload = {'client_id': 'HCSE30GAMDOJLUBDYY54CJBJHXDJYANTDSYQZV4A5X3AJZPX',
                      'client_secret': 'TOQSG40N2N5Q00H0J1RZVNVBDBRE5GT1VQ03JUTUB1AYDMW5',
                      'll': ll,
                      'categoryId': '4bf58dd8d48988d11b941735',
                      'radius': '400'}
    r = requests.get("https://api.foursquare.com/v2/venues/explore", params=payload)

    result = r.json()

    pubs = []
    for item in result['response']['groups'][0]['items']:
        venue = item['venue']
        # print "%s - %s - %s" % (venue['name'], venue['stats']['checkinsCount'], venue['location']['distance'])
        pubs.append((venue['name'], venue['stats']['checkinsCount']))
    pubs = sorted(pubs, key=lambda x: x[1])
    if len(pubs) > 0:
        top_pub = pubs[-1][0]
    else:
        top_pub = "No pub for this location! Run Away!"
    print u"%s, %s" % (place['station'], top_pub)