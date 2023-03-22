'''The data obtained from the plots suggests that the 5 stations most at risk of flooding are:
   Blackstones Farm, Sheffield Carr Brook Screen, Whaddon, Cam and Days Lock in order of 
   highest risk of flooding to lowest risk of flooding'''

# Blackstones Farm has had a sudden spike in relative water levels far exceeding the expected maximum value in recent times
# Sheffield Carr Brook Screen has had consistently relative water levels recently but this value seems to remain constant
# Whaddon has relative water levels higher than the expected maximum but the water level seems to be decreasing and increasing periodically 
# Cam has high relative water levels but these are comparatively close to the expected maximum water levels
# Days Lock relative water levels has barely exceeded the expected maximum water levels recently and seems to be decreasing back to the expected values region

import datetime
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_highest_rel_level

def run():
    # Build list of stations
    stations = build_station_list()
    
    # Update latest level data for all stations
    update_water_levels(stations) 

    # Building a list of the 5 stations with the highest relative water level using stations_highest_rel_level
    top_five_stations = stations_highest_rel_level(stations, 5)

    # Plot water level data and best-fit polynomial for each top station
    for station in top_five_stations:
        dt = 2
        dates, levels = fetch_measure_levels(station[0].measure_id, dt=datetime.timedelta(days=dt))
        print (levels)
        sum_of_all_levels = 0
        counter = 0
        # Calculate the average_level of the stations within the same time range
        for level in levels:
            sum_of_all_levels += level
            counter += 1
        average_level = sum_of_all_levels/counter
        risk_measurement = []
        risk_measurement.append((station, average_level - station[0].typical_range[1]))
        # Compare the risk_measurement values for each of the 5 stations and order them from greatest to least
        for tuple in risk_measurement


if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()