# -*- encoding: utf -*-
"""
Create on 2020/9/23 22:06
@author: Xiao Yijia
"""

import configparser


class ClimateConfig:
    climate_record_path = None
    station_file_name = None
    output_path = None
    need_fields = None

    @staticmethod
    def parse_from_file(filename):
        conf = configparser.ConfigParser()
        conf.read(filename, encoding='utf-8')

        ClimateConfig.climate_record_path = conf['climate']['climate_record_path']
        ClimateConfig.station_file_name = conf['climate']['station_file_name']
        ClimateConfig.output_path = conf['climate']['output_path']
        ClimateConfig.need_fields = conf['climate']['needfields'].split(";")
