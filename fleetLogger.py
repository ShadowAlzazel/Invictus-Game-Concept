import sys
from shipClasses import *

#creates ships from fleet log
def launch_fleet(some_fleet):

    def get_some_class(class_name):
        return getattr(sys.modules[__name__], class_name)

    if some_fleet.preset:
        for i, x_ship_names in enumerate(some_fleet.fleet_logs['shipNames']):
            a_class = get_some_class(some_fleet.fleet_logs['shipClasses'][i])
            new_ship = a_class(some_fleet.fleet_logs['shipHullnumber'][i], x_ship_names, ''.join([some_fleet.fleet_command, 'S']), some_fleet.name)
            some_fleet.fleet_ships.append(new_ship)
        some_fleet.flagship = some_fleet.fleet_ships[0]