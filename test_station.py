# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation
from floodsystem.station import inconsistent_typical_range_stations


from floodsystem.stationdata import build_station_list

# Create an instance of the -stations- class to use for testing
stations = build_station_list()



def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town



def test_inconsistent_typical_range_stations():
    a = inconsistent_typical_range_stations(stations[:2])
    inconsistent_stations = []
    if stations[0].typical_range_consistent() is False:
        inconsistent_stations.append(stations[0].name)
    if stations[1].typical_range_consistent() is False:
        inconsistent_stations.append(stations[1].name)
    inconsistent_stations.sort()
    assert inconsistent_stations == a
    return inconsistent_stations
