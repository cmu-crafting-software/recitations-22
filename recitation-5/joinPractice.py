import pandas as pd
#Taryn and Shilin

#part 1
readings = pd.read_csv('readings.csv', index_col='id')
sensors = pd.read_csv('sensors.csv', index_col='id')
stations_sensors = pd.read_csv('stations_sensors.csv')
stations = pd.read_csv('stations.csv', index_col='id')

readings = pd.DataFrame(readings)
# print(readings)
sensors = pd.DataFrame(sensors)
#print(sensors)
stations_sensors = pd.DataFrame(stations_sensors)
#print(readings)
stations = pd.DataFrame(stations)
#print(readings)

#part 2
# print(readings.columns)
# print(sensors.columns)
# print(stations_sensors.columns)
# print(stations.columns)

#part 3
joined_df = readings.join(stations, 'station_id', 'inner', '_readings', sort = True)

#print(joined_df.sort_values('id'))

#part 4

join_all = joined_df.join([stations_sensors, stations], how = 'inner', 'extra_',sort = True)
print(join_all)


