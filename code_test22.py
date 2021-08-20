import time

class Vehicle:
    def __init__(self, m, c):
        self.model = m
        self.color = c
        self.speed = 0
        self.meter = 0

    def info(self):
        print('車種' + self.model)
        print('色' + self.color)
        print('速度 {}km/h'.format(self.speed))


CAR_DATA = [
    ['コンパクトカー', '赤'],
    ['スポーツカー', '黄'],
    ['クラシックカー', '黒'],
    ['マイクロバス', '青'],
    ['ダンプカー', '緑']
]

veh = [None] * 5
for i in range(5):
    veh[i] = Vehicle(CAR_DATA[i][0], CAR_DATA[i][1])
    veh[i].info()

