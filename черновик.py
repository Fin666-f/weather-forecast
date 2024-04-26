from pyowm import OWM

owm = OWM('a99967bc9ee70d5b4bd387902982f400')
mgr = owm.weather_manager()
observation = mgr.weather_at_place('Springfield, US').weather

temp_dict_kelvin = observation.temperature('celsius')
temp_dict_kelvin['temp_min']
temp_dict_kelvin['temp_max']
temp_dict_fahrenheit = observation.temperature('fahrenheit')  # a dict in Fahrenheit units
temp_dict_celsius = observation.temperature('celsius')  # guess?
print(temp_dict_kelvin)

wind_dict_in_meters_per_sec = observation.wind()   # Default unit: 'meters_sec'
wind_dict_in_meters_per_sec['speed']
print(wind_dict_in_meters_per_sec)

rain_dict = observation.detailed_status
print(rain_dict)

pressure_dict = observation.barometric_pressure(unit='inHg')
#pressure_dict['sea_level']
print(pressure_dict)

humi = observation.humidity
print(humi, '%')

sunrise_unix = observation.sunrise_time()
sunrise_date = observation.sunrise_time(timeformat='date')
sunrset_unix = observation.sunset_time()
sunrset_date = observation.sunset_time(timeformat='date')
sunrise = str(sunrise_date).split()[1].split(':')[0]
sunrset = str(sunrset_date).split()[1].split(':')[0]
print(sunrise, sunrset)
