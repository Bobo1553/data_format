# -*- encoding: utf -*-
"""
Create on 2020/9/23 22:06
@author: Xiao Yijia
"""
import csv
import os

from config.climate_config import ClimateConfig
from config.grid_config import GridConfig
from dao.climate import Climate
from dao.records_of_station import RecordsOfStation
from dao.station import StationInfo
from util.utils import Utils


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
        station_id = Utils.parse_filename_get_station_id(climate_file_name)
        records_of_station = RecordsOfStation(station_id)
        records_of_station.add_climate_records_by_file(climate_file_name, ClimateConfig.climate_record_path)
        total_records_of_station.append(records_of_station)

    for filed in ClimateConfig.need_fields:
        with open(os.path.join(ClimateConfig.output_path, filed + '.csv'), 'w', newline='') as output_filed_file:
            result_writer = csv.writer(output_filed_file)
            for records_of_station in total_records_of_station:
                station_id = records_of_station.station_id
                station = stations.get(station_id)
                if station is None:
                    continue
                info = station.station_info() + records_of_station.to_string(filed)
                print("linelength:" + str(len(info)))
                result_writer.writerow(info)


def one_station_one_day_info_fill(stations, climate_index, station_index, field_name, field_value, station_append, climate_append):

    if station_append:
        stations.append(RecordsOfStation(station_index + 1))

    if climate_append:
        year, day = Utils.index_to_year_and_day(climate_index + 1, 2020, 0)
        stations[station_index].add_single_climate(Climate(year, day))

    stations[station_index].climate_records[climate_index].__setattr__(field_name, field_value)
    return stations


def one_day_info_fill(stations, climate_index, field_file_name, field_name, station_append, climate_append):
    if field_file_name.endswith("_cov.grd") or not (field_file_name.endswith(".grd")):
        return stations

    print(field_file_name)
    with open(field_file_name, 'r') as field_file:

        for i in range(6):
            next(field_file)


        station_index = 0
        for row in field_file:
            climates = row.rstrip().replace("-9999.0", "").split(" ")
            # climates = row..split(" ")

            for climate_info in climates:
                if climate_info == '':
                    continue
                # print(climate_info)
                stations = one_station_one_day_info_fill(stations, climate_index, station_index, field_name, float(climate_info), station_append, climate_append)
                station_index += 1

    return stations


def fill_single_field(stations, field_path, field_name, climate_append):
    field_file_list = get_field_file_list(field_path)

    climate_index = 0
    for field_file_name in field_file_list:
        if not stations:
            station_append = True
        else:
            station_append = False

        # with open(os.path.join(field_path, field_file_name), 'r') as field_file:
        #     print(field_file_name)
        stations = one_day_info_fill(stations, climate_index, os.path.join(field_path, field_file_name), field_name,
                                     station_append, climate_append)
        climate_index += 1

    return stations


def get_field_file_list(field_path):
    field_file_list = [field_file_name for field_file_name in os.listdir(field_path) if
                       field_file_name.endswith(".grd") and not field_file_name.endswith("_cov.grd")]
    field_file_list.sort(key=lambda x: int(x[:-4]))
    return field_file_list


def format_grid_data():
    GridConfig.parse_from_file("config/config.yml")

    stations = []

    climate_append = True
    for field_path in GridConfig.field_paths:
        field_name = Utils.parse_path_get_field_name(field_path)
        stations = fill_single_field(stations, field_path, field_name, climate_append)
        print("finish " + field_name)
        climate_append = False

    for station in stations:
        station.export_to_csv(GridConfig.output_path)

    return


if __name__ == '__main__':
    # format_station_data()
    format_grid_data()
