# -*- encoding: utf -*-
"""
Create on 2020/9/23 22:10
@author: Xiao Yijia
"""


class Climate:

    def __init__(self, year, day, radn, maxt, mint, rain) -> None:
        super().__init__()
        self.year = year
        self.day = day
        self.radn = radn
        self.maxt = maxt
        self.mint = mint
        self.rain = rain
