from ntpath import join
import re
import pandas as pd

## Worked with Jack Johnson 


# Part 1
readings = pd.read_csv('readings.csv')
stations = pd.read_csv('stations.csv')
sensors = pd.read_csv('sensors.csv')

#print(readings)
#print(stations)

# Part 2
readings = pd.DataFrame(readings)
stations = pd.DataFrame(stations)
sensors = pd.DataFrame(sensors)
print(readings.columns)
print(stations.columns)

# Part 3
joined = readings.join(stations,how='inner',lsuffix=' readings')
print(joined)

# Stretch goal
inner_join = joined.join(sensors, how = 'inner', lsuffix = ' sensors')

left_join = readings.join(stations,how='left',lsuffix=' readings')
left_join = left_join.join(sensors, how = 'left', lsuffix = ' sensors')

right_join = readings.join(stations,how='right',lsuffix=' readings')
right_join = right_join.join(sensors, how = 'right', lsuffix = ' sensors')

outer_join = readings.join(stations,how='outer',lsuffix=' readings')
outer_join = outer_join.join(sensors, how = 'outer', lsuffix = ' sensors')

print('Inner Join')
print(inner_join)

print('Left Join')
print(left_join)

print('Right Join')
print(right_join)

print('Outer Join')
print(outer_join)