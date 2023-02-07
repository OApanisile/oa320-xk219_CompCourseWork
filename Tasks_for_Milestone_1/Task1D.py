# Olumide

# Part 1

# Import the rivers_with_station function from the geo.py file
from floodsystem.geo import rivers_with_station

# Import the build_station_list like in 1A
from floodsystem.stationdata import build_station_list

def run():
    
    # Build list of stations
    stations = build_station_list()
    
    # Make a set to contain the results of the rivers_with_station function
    initial_river_list = []
    initial_river_list = rivers_with_station(stations)
    set_of_river_list = set(initial_river_list)
   
    # Print the number of items in the set
    print(f'{len(set_of_river_list)} stations')
    
    # Sort the results of the function in alphabetical order
    sorted_river_list = sorted (set_of_river_list)
    
    # Print a list of the first 10 items in the list
    print (sorted_river_list[:10])
 
# Run the program in main branch...I think
if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()

# Part 2

# Import the stations_by_river function from the geo.py file
from floodsystem.geo import stations_by_river

def run():
    
    # Build list of stations
    stations = build_station_list()

    # Make a dictionary with all the rivers and stations
    river_dictionary_all = stations_by_river (stations)

    #Extract the list of stations associated with the specified rivers and sort them alphabetically
    river_name = str(input('Enter River name: '))
    river_list = river_dictionary_all[river_name]
    sorted_river_list = sorted (river_list)
    print(sorted_river_list[:10])

# Run the program in main branch...I think
if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()
