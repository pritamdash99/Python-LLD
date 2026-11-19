# Object Creations, Logic Executions happen here.

from weather_station import WeatherStation
from tv import TV_Display
from mobile import Mobile_Display
from desktop import Desktop_Display

ws = WeatherStation()
tv = TV_Display()
ws.add_Observer(tv)
ws.update_temperature(20)

# TV Temperature updated to  20

# Let's add more observers by creating their necesaary classes and adding them into list.
desktop = Desktop_Display()
mobile = Mobile_Display()

ws.add_Observer(desktop)
ws.add_Observer(mobile)
ws.update_temperature(35)

# TV Temperature updated to 35
# Desktop Temperature updated to 35
# Mobile Temperature updated to 35

ws.remove_Observer(tv)
ws.update_temperature(15)
# Desktop Temperature updated to 15
# Mobile Temperature updated to 15