# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""#
# Import required modules up here and across multiple functions
from haversine import haversine, Unit
from floodsystem.utils import sorted_by_key


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


# Task 1D: rivers with a station(s) Part 1 - Olumide
def rivers_with_station(stations):
    
    # For every river in stations, check if there is a corresponsing station somehow
    # Make an empty list to contain the names of all the rivers
    rivers_list = []
    
    # Add the name of every river that corresponds to a station
    for station in stations:
        rivers_list.append (station.river)
    
    # Make a list of tuples of rivers and stations
    return rivers_list


# Task 1D: rivers with a station(s) Part 2 - Olumide
def stations_by_river(stations):
    
    # Define a method for adding river_names as keys and associated stations as corresponding values
    def add_values_in_dict(river_dictionary, key, stations_list):
        # If the key does not already exist in dictionary, add it to the dictionary keys
        if key not in river_dictionary:
            river_dictionary[key] = list()
            river_dictionary[key].append(stations_list)
        # If the key already exists in the dictionary, add the station to the list of values associated with that key
        elif key in river_dictionary:
            river_dictionary[key].append(stations_list)
        return river_dictionary
    
    # Initialise dictionary
    river_dictionary = {}

    # Iterate over very station and make lists of stations with the same river
    for station in stations:
        results_dictionary = add_values_in_dict (river_dictionary, station.river, station.name)
    return results_dictionary

# Task 1E: Xinze
def rivers_by_station_number(stations, N):
        # Make a dictionary with all the rivers and stations
    river_dictionary_all = stations_by_river(stations)

    river_to_station_no = []

    for i in range(len(list(river_dictionary_all.keys()))):
        river_to_station_no.append((list(river_dictionary_all.items())[i][0], len(list(river_dictionary_all.items())[i][1])))
    sorted_river_to_station = sorted_by_key(river_to_station_no, 1, True)
    output = sorted_river_to_station[:N]

    while True:
        if sorted_river_to_station[N - 1][0] == sorted_river_to_station[N][0]:
            output.append(sorted_river_to_station[N])
            N = N + 1
        else:
            break
    
    return output
