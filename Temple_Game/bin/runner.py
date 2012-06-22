import sys
sys.path.append("michael-lennons-macbook:python michaellennon$")
import ex43rooms


class Engine(object):
    def __init__(self, todays_map):
        self.todays_map = todays_map

    def play(self):
        next = self.todays_map.start()
        
        while True:
            print "\n-----------------\n"
            room = getattr(self.todays_map, next.play())
            next = room()


todays_map = ex43rooms
engine = Engine(todays_map)
engine.play()

