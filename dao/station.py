# -*- encoding: utf -*-
"""
Create on 2020/9/23 22:12
@author: Xiao Yijia
"""


class StationInfo:

    def __init__(self, object_id, station_id, name, point_x, point_y, height) -> None:
        super().__init__()
        self.object_id = object_id
        self.station_id = station_id
        self.name = name
        self.point_x = point_x
        self.point_y = point_y
        self.height = height

    def station_info(self):
        return [self.station_id, self.point_x, self.point_y, self.height]
