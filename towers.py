from dataclasses import dataclass

@dataclass
class Prices:
    pa1: int
    pa2: int
    pa3: int
    pa4: int
    pa5: int
    pb1: int
    pb2: int
    pb3: int
    pb4: int
    pb5: int
    pc1: int
    pc2: int
    pc3: int
    pc4: int
    pc5: int


class MediumBananaFarm(Prices):
    def __init__(self):
        super().__init__(
                500,600,3000,19000,115000,
                300,800,3650,7200,100000,
                250,400,2700,15000,70000)
