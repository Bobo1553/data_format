# -*- encoding: utf -*-
"""
Create on 2020/10/16 17:42
@author: Xiao Yijia
"""

import arcgisscripting
import arcpy


class Shp:

    def __init__(self, shp_name):
        self.shp_name = shp_name

    @staticmethod
    def make_shp(inTxt, inSep, strms, coordination):
        # Create geoprocessing dispatch object
        gp = arcgisscripting.create()

        # Run tool
        gp.CreateFeaturesFromTextFile(inTxt, inSep, strms, coordination)

    def fetch_data_list(self, field_list):
        cursor = arcpy.da.SearchCursor(self.shp_name, field_list)
        data = []

        for row in cursor:
            data.append((row[0], -row[1], row[2], row[3]))

        return data


if __name__ == '__main__':
    Shp.make_shp(r"F:\XYJ烦人\result1016\ClimateSoil.txt", ".", r"F:\XYJ烦人\result1016\ClimateSoil.shp",
                 "WGS 1984 World Mercator")

