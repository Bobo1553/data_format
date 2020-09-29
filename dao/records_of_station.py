# -*- encoding: utf -*-
"""
Create on 2020/9/23 22:22
@author: Xiao Yijia
"""
import csv
import os

from dao.climate import Climate


class RecordsOfStation:

    def __init__(self, station_id, climate_records=None) -> None:
        super().__init__()
        self.station_id = station_id
        self.climate_records = climate_records

    def add_climate_records_by_file(self, filename, file_path='', ) -> None:
        if file_path != '':
            filename = os.path.join(file_path, filename)

        with open(filename, 'r') as climates_file:
            next(climates_file)
            next(climates_file)
            for line in climates_file:
                climate_info = [i for i in line.split(" ") if i != ""]
                if int(climate_info[0]) < 2020:
                    continue
                climate_record = Climate(climate_info[0], climate_info[1], climate_info[2], climate_info[3], climate_info[4],
                                         climate_info[5])
                self.climate_records.append(climate_record)
        print("climate-records:" + str(len(self.climate_records)))

    def add_single_climate(self, climate_record) -> None:
        if self.climate_records is None:
            self.climate_records = []
        self.climate_records.append(climate_record)

    def to_string(self, field_name):
        format_result = []
        for climate_record in self.climate_records:
            format_result.append(climate_record.__getattribute__(field_name))

        return format_result

    def export_to_csv(self, output_path):
        if not os.path.exists(output_path):
            os.mkdir(output_path)

        with open(os.path.join(output_path, str(self.station_id) + '.txt'), 'w') as output_file:
            output_file.writelines("Date Rain Tmax Tmin SARD\n")
            for climate_record in self.climate_records:
                output_file.writelines(climate_record.to_string() + "\n")


if __name__ == '__main__':
    test = RecordsOfStation(5)
    climate = Climate(2015, 35)
    test.add_single_climate(climate)
    climate = Climate(2085, 35)
    test.add_single_climate(climate)
    climate = Climate(2018, 35)
    test.add_single_climate(climate)
    test.export_to_csv(r'E:\test')
