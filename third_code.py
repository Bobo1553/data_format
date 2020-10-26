# -*- encoding: utf -*-
"""
Create on 2020/10/17 16:35
@author: Xiao Yijia
"""
# from config.shp_config import ShpConfig
from dao.shp import Shp

soil_shp_name = r"F:\数据库\ClimateSoilPoint.shp"
soil_file_name = r''

class ThirdCode(object):
    soil_info = {}

    def get_soil_info(self, file_name):
        with open(file_name, 'r') as soil_file:
            for line in soil_file:
                print(line)
        pass

    def step1(self, shp_name):
        soil_shp = Shp(shp_name)
        soil_list = soil_shp.fetch_data_list(["SHAPE@X", "SHAPE@Y", "SoilProfil", "RASTERVALU"])
        soil_list.sort(key=lambda x: (x[1], x[0]))
        for i in range(len(soil_list)):

        print(soil_list)
        print(len(soil_list))
        pass


def main():
    third_code = ThirdCode()
    third_code.step1(soil_shp_name)


if __name__ == '__main__':
    main()
