##This is the function for 2B (Xinze Kang)##


def stations_level_over_threshold(stations, tol):
    over_tol_list = []
    for station in stations:
        if station.relative_water_level() is not None and station.relative_water_level() > float(tol):
            over_tol_list.append((station,station.relative_water_level()))
    
    over_tol_list.sort(reverse=True ,key=lambda a: a[1])
    return over_tol_list



def stations_highest_rel_level(stations, N):
    latest_level_list = []
    for station in stations:
        if station.relative_water_level() is not None:
            latest_level_list.append((station, station.relative_water_level()))
    latest_level_list.sort(reverse=True, key=lambda a: a[1])
    N_risk_stations=[]
    for i in range(N):
        N_risk_stations.append(latest_level_list[i])
    return N_risk_stations



