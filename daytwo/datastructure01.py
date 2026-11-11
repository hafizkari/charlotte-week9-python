pressure_reading_list = [3150,2780,3040,2510,2815]

temp_reading_tup = (186,172,195,180,187,166)

sensor_active_set={True,False}

well_readings = {
    'presssure' :pressure_reading_list,
    'temperature' :temp_reading_tup,
    'sensor_active' :sensor_active_set
}

"""print(pressure_reading_list, temp_reading_tup, sensor_active_set, well_readings)"""

#indexing
print(pressure_reading_list[0])