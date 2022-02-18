import pandas as pd

readings = pd.read_csv('readings.csv')
sensors = pd.read_csv('sensors.csv')
stations_sensors = pd.read_csv('stations_sensors.csv')
stations = pd.read_csv('stations.csv')

print('Tables')
print('\n')
print(readings)
print('\n')
print(sensors)
print('\n')
print(stations_sensors)
print('\n')
print(stations)

print('\n')
print('Columns')
print(readings.columns)
print(stations.columns)

merged = readings.join(stations,on='station_id',how = 'inner',rsuffix = 'duplicate')
print(merged)

nextmerge = readings.join([stations,stations_sensors,sensors],on='')