#Started 10/24/2021

from shipTypes import Battleship

class EssexClass(Battleship):
    ammount = 0

    FP = 315
    shields = 12500
    hull = 10000


    def __init__(self, hullnumber, name):
        super().__init__(hullnumber, name)

        EssexClass.ammount += 1

    def EssexBarrage(self):
        e = self.FP * 200
        print("Essex Barrage! Dmg:", e)


class AmagiClass(Battleship):
    ammount = 0

    FP = 305
    EVA = 40
    shields = 13000
    hull = 9500

    def __init__(self, hullnumber, name):
        super().__init__(hullnumber, name)

        AmagiClass.ammount += 1

