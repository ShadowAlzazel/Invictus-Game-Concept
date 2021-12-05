#RNG in km
#RLD in Seconds
#M, L, A, denote the guns radius in inches
#All batteries designed for a single case

class shipWeapon:
    gun_name = 'shipWeapon'
    #Attack, reload, hit, range, quantity, penetration, dissonannce
    gun_stats = {
        "ATK": 32, "RLD": 1, "HIT": 64, "RNG": 1, "QNT": 1, "PEN": 0, "DIS": 1
    }

    def __init__(self, vessel_ID, battery_turret_number):
        assert self.gun_stats["DIS"] != 0
        assert self.gun_stats["PEN"] >= 0
        assert self.gun_stats["RLD"] >= 1
        self.battery_ID = '-'.join([vessel_ID, battery_turret_number])
        self.gun_load_time = 100 #preloaded

    def reload_gun(self):
        if self.gun_load_time < self.gun_stats['RLD']:
            self.gun_load_time += 1
        else: 
            self.gun_load_time = self.gun_stats['RLD']
