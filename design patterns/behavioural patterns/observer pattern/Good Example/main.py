# Object Creations, Logic Executions happen here.

from observer import Observer
from weather_station import WeatherStation
from tv import TV_Display

ws = WeatherStation()
tv = TV_Display()
ws.add_Observer(tv)
ws.update_temperature(20)

# TV Temperature updated to  20