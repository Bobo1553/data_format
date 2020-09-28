# -*- encoding: utf -*-
"""
Create on 2020/9/23 22:06
@author: Xiao Yijia
"""

import configparser


class GridConfig:
    field_paths = None
    output_path = None

    @staticmethod
    def parse_from_file(filename):
        conf = configparser.ConfigParser()
        conf.read(filename, encoding='utf-8')

        GridConfig.field_paths = conf['grid']['field_paths'].split(";")
        GridConfig.output_path = conf['grid']['output_path']
