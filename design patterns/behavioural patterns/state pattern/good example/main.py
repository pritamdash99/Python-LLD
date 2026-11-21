#We execute all the necessary logics here

from transport_service import TransportService
from bike_mode import BikeMode
from walk_mode import WalkMode
use_bike_mode = BikeMode()
use_walk_mode = WalkMode()

services = TransportService(use_bike_mode)
services.use_eta()
services.use_directions()

# Bike will take 10 mins
# Go left to road

services.set_mode(use_walk_mode)
services.use_directions()
services.use_eta()
# Walk right across bridge
# Walking will take 30 mins
