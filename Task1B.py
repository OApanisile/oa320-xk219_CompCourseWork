# Olumide 
# Trying to import the stations_by_distance function from the geo.py file
from .geo import stations_by_distance
# Not sure what coordinates to set as the Cambridge_coordinates
cambridge_coordinates = ()
# Sort the list of stations according to their distance from the Cambridge_coordinates
organised_stations_list = stations_by_distance (station , cambridge_coordinates)
# Make list of the closest and furthest stations from Cambridge according to the stations_by_distance couple
closest_list = []
furthest_list = []
closest_list.append(stations_by_distance[:10])
furthest_list.append(stations_by_distance[:-10])
# Learn how to insert an element into a tuple --> From (station, distance) to (station, cambridge, distance)