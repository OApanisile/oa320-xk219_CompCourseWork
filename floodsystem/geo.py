# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
from .utils import sorted_by_key

#Task 1B: sort stations by distance - Olumide
def stations_by_distance(stations, p):

    # Defining a list to contain the tuples of station and distance
    station_distance = []
    
    #A loop that iterates over every station from the stations list
    for station in stations:
        #Where do we get p from?
        # Use the haversine function to calculate the distance of the station from the coordinates
        from haversine import haversine, Unit
        distance = haversine(station.coord, p)
        
        # Add the stations and respective distances to the list in a tuple format
        station_distance.append (station, distance)
        
        # Use the sorted_by_key function to sort the list according to distance
        sorted_by_key (station_distance, distance)

    # Return the sorted list as the output
    return station_distance

# Task 1C: stations within radius - Olumide
def stations_within_radius(stations, centre, r):
    # Use the haversine function to calculate the distance between each station and centre
    # If that distance is less than r then add the corresponding station to the list
    return #The list with all the stations within the radius r

# Task 1D: rivers with a station(s) Part 1 - Olumide
def rivers_with_station(stations):
    # For every river in stations, check if there is a corresponsing station somehow
    # Make a list of tuples of rivers and stations
    return

# Task 1D: rivers with a station(s) Part 2 - Olumide
def stations_by_river(stations):
    # Use the list obtained from rivers_with_stations to make a dictionary of form river: stations