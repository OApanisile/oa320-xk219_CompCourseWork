
from datetime import datetime
import datetime

from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list
from floodsystem.plot import plot_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels

def run():
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    five_stations = stations_highest_rel_level(stations, 5)

    for station in five_stations:
        dt = 10
        dates, levels = fetch_measure_levels(station[0].measure_id, dt=datetime.timedelta(days=dt))
        plot_water_levels(station, dates, levels)




    



if __name__ == "__main__":
    print("*** Task 2D: CUED Part IA Flood Warning System ***")
    run()
