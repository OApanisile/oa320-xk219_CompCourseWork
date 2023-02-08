# Olumide

# Import the stations_within_radius function
from floodsystem.geo import stations_within_radius

# Import the build_station_list like in 1A
from floodsystem.stationdata import build_station_list

# Set Cambridge_coordinates to the ones provided on tasks webpage
cambridge_coordinates = (52.2053, 0.1218)

def run():
    
    # Build list of stations
    stations = build_station_list()
    
    # Make a list of stations and distances within the radius
    organised_radius_list = []
    organised_radius_list = stations_within_radius (stations, cambridge_coordinates, 10)
    
    # Sort the results of the function in alphabetical order
    sorted_radius_list = sorted (organised_radius_list)
    
    # Output a list of the results
    print(sorted_radius_list)

# Run the program in main branch...I think
if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()