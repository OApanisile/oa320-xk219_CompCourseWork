# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
# Import required modules up here and across multiple functions
from haversine import haversine, Unit

#Task 1B: sort stations by distance - Olumide
def stations_by_distance(stations, p):

    # Defining a list to contain the tuples of station and distance
    station_distance = []
    
    #A loop that iterates over every station from the stations list
    for station in stations:
        #Where do we get p from?
        # Use the haversine function to calculate the distance of the station from the coordinates
        distance = haversine(station.coord, p)
        # Add each element needed for Task1B into the station_distance list independently
        # Add the stations and respective distances to the list in a tuple format
        station_distance.append ((station.name, station.town, distance))
        
    # Return the sorted list as the output
    return station_distance

# Task 1C: stations within radius - Olumide
def stations_within_radius(stations, centre, r):

    # Make a list to contain all the required station information
    radius_list = []
    
    # Use the haversine function to calculate the distance between each station and centre
    for station in stations:
        distance = haversine(station.coord, centre, unit=Unit.KILOMETERS)
        
        # If that distance is less than r then add the corresponding station to the list
        if distance < r:
            radius_list.append((station.name))
    
    #The list with all the stations within the radius r        
    return radius_list 




