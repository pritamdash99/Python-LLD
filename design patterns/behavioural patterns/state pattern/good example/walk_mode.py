from transport_mode import TransportMode

class WalkMode(TransportMode):

    def eta(self):
        print("Walking will take 30 mins")

    def give_direction(self):
        print("Walk right across bridge")
