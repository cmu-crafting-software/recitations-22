#Luis Viornery
#Nikole Chetty

import pandas as pd

readings = pd.read_csv('readings.csv',index_col='id')
stations = pd.read_csv('stations.csv',index_col='id')
sensors = pd.read_csv('sensors.csv',index_col='id')
stations_sensors = pd.read_csv('stations_sensors.csv',index_col='station_id')

print(readings)
print(stations)
print(readings.columns)
print(stations.columns)

inner_join_readings_stations = readings.join(stations, on='station_id', how='inner')

print(inner_join_readings_stations.sort_values('id'))

for method in ['inner','outer','left','right']:

    join_readings_stations = readings.join(stations, on='station_id', how=method)

    join_readings_stations_stationsensors = join_readings_stations.join(stations_sensors, on='station_id', how=method)

    omni_join = join_readings_stations_stationsensors.join(sensors, on='sensor_id', how=method)

    print(omni_join)