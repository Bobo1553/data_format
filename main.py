# -*- encoding: utf -*-
"""
Create on 2020/9/23 22:06
@author: Xiao Yijia
"""
import os
import csv

from config.climate_config import ClimateConfig
from dao.records_of_station import RecordsOfStation
from dao.station import StationInfo


def get_full_stations():
    stations = {}
    with open(ClimateConfig.station_file_name, 'r') as station_file:
        station_reader = csv.reader(station_file)
        next(station_reader)
        for station_list in station_reader:
            station = StationInfo(station_list[0], station_list[1], station_list[2], station_list[3], station_list[4],
                                  station_list[5])
            stations[station.station_id] = station
    return stations


def format_station_data():
    ClimateConfig.parse_from_file("config/config.yml")

    stations = get_full_stations()

    files = os.listdir(ClimateConfig.climate_record_path)
    files.sort()

    total_records_of_station = []

    for climate_file_name in files:
        records_of_station = RecordsOfStation(climate_file_name, ClimateConfig.climate_record_path)
        total_records_of_station.append(records_of_station)

    for filed in ClimateConfig.need_fields:
        with open(os.path.join(ClimateConfig.output_path, filed + '.csv'), 'w', newline='') as output_filed_file:
            result_writer = csv.writer(output_filed_file)
            for records_of_station in total_records_of_station:
                station_id = records_of_station.station_id
                station = stations.get(station_id)
                if station is None:
                    continue
                info = station.station_info() + records_of_station.format_to_line(filed)
                print("linelength:" + str(len(info)))
                result_writer.writerow(info)


def format_grid_data():

    return


if __name__ == '__main__':
    format_station_data()
