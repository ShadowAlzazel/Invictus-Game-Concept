import sys
from shipClasses import *

#creates ships from fleet log
def launch_fleet(some_fleet):

    def get_some_class(class_name):
        return getattr(sys.modules[__name__], class_name)

    if some_fleet.preset:
        n = 0
        for x_ships in some_fleet.fleet_logs['shipNames']:
            a_class = get_some_class(some_fleet.fleet_logs['shipClasses'][n])
            new_ship = a_class(some_fleet.fleet_logs['shipHullnumber'][n], x_ships)
            new_ship.command = ''.join([some_fleet.fleet_command, 'S'])
            some_fleet.fleet_ships.append(new_ship)
            n += 1
        some_fleet.flagship = some_fleet.fleet_ships[0]