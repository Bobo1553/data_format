# -*- encoding: utf -*-
"""
Create on 2020/9/23 22:06
@author: Xiao Yijia
"""

import configparser


class GridConfig:

    radn_path = None
    rain_paht = None
    tmax_path = None
    tmin_path = None
    output_path = None

    @staticmethod
    def parse_from_file(filename):
        conf = configparser.ConfigParser()
        conf.read(filename, encoding='utf-8')

        GridConfig.radn_path = conf['grid']['radn_path']
        GridConfig.rain_paht = conf['grid']['rain_paht']
        GridConfig.tmax_path = conf['grid']['tmax_path']
        GridConfig.tmin_path = conf['grid']['tmin_path']
        GridConfig.output_path = conf['grid']['output_path']
