# -*- encoding: utf -*-
"""
Create on 2020/9/23 22:22
@author: Xiao Yijia
"""
import os

from dao.climate import Climate
from util.utils import Utils


class RecordsOfStation:

    def __init__(self, filename, file_path='') -> None:
        super().__init__()
        if file_path != '':
            filename = os.path.join(file_path, filename)

        self.station_id = Utils.parse_filename_get_station_id(filename)
        self.climate_records = []

        with open(filename, 'r') as climates_file:
            next(climates_file)
            next(climates_file)
            for line in climates_file:
                climate_info = [i for i in line.split(" ") if i != ""]
                if int(climate_info[0]) < 2020:
                    continue
                climate = Climate(climate_info[0], climate_info[1], climate_info[2], climate_info[3], climate_info[4],
                                  climate_info[5])
                self.climate_records.append(climate)
        print("climate-records:" + str(len(self.climate_records)))

    def format_to_line(self, field='maxt'):
        format_result = []
        for climate in self.climate_records:
            format_result.append(climate.__dict__[field])

        return format_result
