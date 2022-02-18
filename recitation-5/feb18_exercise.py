#Dom and Morgan

import pandas as pd

csv_readings = pd.read_csv("readings.csv")
csv_stations = pd.read_csv("stations.csv")

# print(csv_readings.head(0))
# print(csv_stations.head(0))

joined_readings_stations = csv_readings.join(csv_stations.set_index("id"), on = "station_id", how = "inner")

#print(joined_readings_stations)

#joined_readings_stations_sensors 
