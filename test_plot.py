from datetime import datetime
import datetime

from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list
from floodsystem.plot import plot_water_levels


# Execution test

def test_plot_water_levels():
    stations= build_station_list()
    dt = 2
    dates, levels = fetch_measure_levels(stations[0].measure_id, dt=datetime.timedelta(days=dt))
    a=plot_water_levels(stations, dates, levels)


