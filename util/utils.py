# -*- encoding: utf -*-
"""
Create on 2020/9/23 22:56
@author: Xiao Yijia
"""
import os
import time
from typing import Tuple


class Utils:

    @staticmethod
    def parse_filename_get_station_id(filename) -> str:
        filename = os.path.split(filename)[1]
        return str(filename.split("_")[0])

    @staticmethod
    def parse_path_get_field_name(path_name) -> str:
        field_name = os.path.split(path_name)[-1]
        return str(field_name)

    @staticmethod
    def index_to_year_and_day(index, start_year, start_day) -> Tuple[int, int]:
        end_day = start_day + index
        while True:
            if Utils.is_leap_year(start_year) and end_day > 366:
                end_day -= 366
                start_year += 1
            elif not (Utils.is_leap_year(start_year)) and end_day > 365:
                end_day -= 365
                start_year += 1
            else:
                break
        return start_year, end_day

    @staticmethod
    def is_leap_year(year):
        if (year % 4) == 0:
            if (year % 100) == 0:
                if (year % 400) == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False


if __name__ == '__main__':
    print(Utils.parse_filename_get_station_id("E:\气象站点\江苏全部气象站点\肖一嘉大好人\position.csv"))
    print(Utils.parse_path_get_field_name(r"E:\radn"))
    print(Utils.is_leap_year(2020))
    print(Utils.index_to_year_and_day(500, 2020, 0))
