# Olumide

# Import the function for calling the class -stations- since it could be useful for testing some of the functions
from floodsystem.stationdata import build_station_list

# Create an instance of the -stations- class to use for testing
stations = build_station_list()

# Import the haversine function to test the stations_by_distance function
from haversine import haversine, Unit

# Import all the functions made in geo.py submodule below this comment
from floodsystem.geo import stations_by_distance
from floodsystem.geo import stations_within_radius
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.geo import rivers_by_station_number

from floodsystem.utils import sorted_by_key

# Set a value n to use as a parameter for how many elements within the stations class are to be tested
n = 10

# Check that all the above functions do something with appropriate respective inputs

# Test that stations_by_distance returns the correct first 2 tuples
def test_function_no_1():
    x = stations_by_distance(stations[:n], (0,0) )
    print(x)
    y = []
    for station in stations[:n]:
        y.append((station.name, station.town, haversine(station.coord, (0,0))))
    print(y)
    assert x == y

# Test that stations_within_radius returns the correct list of the first n stations within the 10 km of (0,0)
def test_function_no_2():
    x = stations_within_radius(stations[:n], (0,0), 10)
    y = []
    for station in stations[:n]:
        distance = haversine(station.coord, (0,0), unit=Unit.KILOMETERS)
        if distance < 10:
            y.append(station.name)
    assert x == y

# Test that rivers_with_station returns the correct list of the first n rivers that have at least one station monitoring them
def test_function_no_3():
    x = rivers_with_station(stations[:n])
    y = []
    for station in stations[:n]:
        y.append(station.river)
    assert x == y

# Test that stations_by_river returns the correct dictionary of rivers: [list_of_stations] for the first n stations
def test_function_no_4():
    x = stations_by_river(stations[:n])
    y = {}

    # Unfortunately can't figure out any other way to call the dictionary sorting function to this module than to copy and paste
    # Define a method for adding river_names as keys and associated stations as corresponding values
    def add_values_in_dict(river_dictionary, key, stations_list):
        
        # If the key does not already exist in dictionary, add it to the dictionary keys
        if key not in river_dictionary:
            river_dictionary[key] = list()
            river_dictionary[key].append(stations_list)
        
        # If the key already exists in the dictionary, add the station to the list of values associated with that key
        elif key in river_dictionary:
            river_dictionary[key].append(stations_list)

        # Output the river_dictionary containing the list of stations associated with each river
        return river_dictionary
    
    for station in stations[:n]:
        z = add_values_in_dict (y, station.river, station.name)
    assert x == z

# Use appropriate test values to check that the functions work properly



# Test for function(rivers_by_station_number) of Task E


def test_rivers_by_station_number():
    a=rivers_by_station_number(stations[:10], 5)

    river_dictionary_all = stations_by_river(stations[:10])

    river_to_station_no = []

    for i in range (10) :
        river_to_station_no.append((list(river_dictionary_all.items())[i][0], len(list(river_dictionary_all.items())[i][1])))
    sorted_river_to_station = sorted_by_key(river_to_station_no, 1 , True)
    output = sorted_river_to_station[:5]

    N=4
    while True:
        if sorted_river_to_station[N][1] == sorted_river_to_station[N][1]:
            output.append(sorted_river_to_station[N])
            N = N + 1
        else:
            break
    assert a == output





    

