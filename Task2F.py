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
        if dates != None and levels != None:
            plot_water_level_with_fit(station, dates, levels, 4)

if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()