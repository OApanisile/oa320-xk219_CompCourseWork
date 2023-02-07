# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
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
        # Add each element needed for Task1B into the station_distance list independently
        # Add the stations and respective distances to the list in a tuple format
        station_distance.append ((station.name, station.town, distance))
        
    # Return the sorted list as the output
    return station_distance



