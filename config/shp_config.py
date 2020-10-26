# -*- encoding: utf -*-
"""
Create on 2020/10/16 17:15
@author: Xiao Yijia
"""


import configparser


class ShpConfig:
    source_file = None
    result_file = None
    soil_shp = None

    @staticmethod
    def parse_from_file(filename):
        conf = configparser.ConfigParser()
        conf.read(filename, encoding='utf-8')

        ShpConfig.source_file = conf['shp']['source_file']
        ShpConfig.result_file = conf['shp']['result_file']
        ShpConfig.soil_shp = conf['shp']['soil_shp']
