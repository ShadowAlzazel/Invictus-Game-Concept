#RNG in km
#RLD in Seconds
#M, L, A, denote the guns radius in inches
#All batteries designed for a single case

class shipWeapon:
    gunName = 'shipWeapon'
    #Attack, reload, hit, range, quantity, penetration, dissonannce
    gun_stats = {
        "ATK": 32, "RLD": 1, "HIT": 64, "RNG": 1, "QNT": 1, "PEN": 0, "DIS": 1
    }

    def __init__(self, vesse_ID, batteryNumber):
        assert self.gun_stats["DIS"] != 0
        assert self.gun_stats["PEN"] >= 0
        assert self.gun_stats["RLD"] >= 1
        self.battery_ID = '-'.join([vesse_ID, batteryNumber])
        self.gun_load_time = 100 #preloaded

    def reload_gun(self):
        if self.gun_load_time < self.gun_stats['RLD']:
            self.gun_load_time += 1
        else: 
            self.gun_load_time = self.gun_stats['RLD']
