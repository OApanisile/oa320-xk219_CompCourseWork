from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold


#execute test#
def test_stations_level_over_threshold():
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    over_tol_list = stations_level_over_threshold(stations, float(0.2))
