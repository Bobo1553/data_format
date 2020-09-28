# -*- encoding: utf -*-
"""
Create on 2020/9/23 22:56
@author: Xiao Yijia
"""
import os


class Utils:

    @staticmethod
    def parse_filename_get_station_id(filename) -> str:
        filename = os.path.split(filename)[1]
        return str(filename.split("_")[0])


if __name__ == '__main__':
    print(Utils.parse_filename_get_station_id("E:\气象站点\江苏全部气象站点\肖一嘉大好人\position.csv"))
