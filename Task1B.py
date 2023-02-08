# Olumide 

# Trying to import the stations_by_distance function from the geo.py file
from floodsystem.geo import stations_by_distance

# Import the build_station_list like in 1A
from floodsystem.stationdata import build_station_list

# Set Cambridge_coordinates to the ones provided on tasks webpage
cambridge_coordinates = (52.2053, 0.1218)

def run():
    
    # Sort the list of stations according to their distance from the Cambridge_coordinates
    # Build list of stations
    stations = build_station_list()
    
    # Use stations_by_distance function to make list of stations and distances from cambridge coordinates
    organised_stations_list = stations_by_distance (stations , cambridge_coordinates)
    
    # From utils.py submodule, import the sorted_by_key function
    from floodsystem.utils import sorted_by_key
    
    # Use the sorted_by_key function to sort the list according to distance
    organised_stations_list = sorted_by_key (organised_stations_list, 2)
    
    # Make list of the closest and furthest stations from Cambridge according to the stations_by_distance couple
    closest_list = []
    furthest_list = []
    closest_list.append(organised_stations_list[:10])
    furthest_list.append(organised_stations_list[:-10])
    
    #print the list of closest and furthest stations from the coordinates provided
    print(closest_list)
    print(furthest_list)
    
# Run the program in main branch...I think
if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()