# -*- encoding: utf -*-
"""
Create on 2020/9/23 22:10
@author: Xiao Yijia
"""


class Climate:

    def __init__(self, year, day, radn=0, maxt=0, mint=0, rain=0) -> None:
        super().__init__()
        self.year = year
        self.day = day
        self.radn = radn
        self.maxt = maxt
        self.mint = mint
        self.rain = rain

    def to_string(self):
        return "{0}{1:03d} {2} {3} {4} {5}".format(str(self.year)[-2:], self.day, self.rain, self.maxt, self.mint, self.radn)


if __name__ == '__main__':
    climate = Climate(2015, 1, 0, 0, 0, 0)
    climate.__setattr__('maxt', 5.56)
    print(climate.to_string())
