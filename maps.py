import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='AIzaSyCJpb2JVK2wSqXfxuwiS0Rb0vYB8sv_BHw')

# Geocoding an address
#geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

# Look up an address with reverse geocoding
#reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

# Request directions via public transit
now = datetime.now()
directions_result = gmaps.directions("14 Hay Avenue St.andrews manitoba canada",
                                     "1095 Concordia avenue winnipeg manitoba canada",
                                     mode="driving",
                                     departure_time=now)
path = (49.97754526858086, -97.06984191194228)
#road = gmaps.nearest_roads(path)
#print(road)

#speed_limit = gmaps.speed_limits('ChIJ8Zd5N_hv6lIRidqYHQQDdew')
#print(speed_limit)
print("directions_result")
print(directions_result)

