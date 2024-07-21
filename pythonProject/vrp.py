import argparse
import math
from collections import defaultdict, deque

from typing import Dict, List


class Location:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Load:
    def __init__(self, load_id: int, pickup_location: Location, drop_off_location: Location):
        self.id = load_id
        self.pickup_location: Location = pickup_location
        self.drop_off_location: Location = drop_off_location


class ClosestLoadPoint:
    def __init__(self, load_id: int, distance: float):
        self.load_id: int = load_id
        self.distance: float = distance


class Driver:
    def __init__(self, driver_number: int):
        self.driver_number: int = driver_number
        self.loads: List[Load] = []
        self.total_distance: float = 0.0
        self.current_location: Location = Location(0, 0)


class VRP:

    def __init__(self, path: str):
        self.depot_location = Location(0, 0)
        self.path = path
        self.load_map: Dict[int, Load] = self.create_load_map()
        self.nearest_pickup_points: Dict[int, List[ClosestLoadPoint]] = self.create_nearest_pickup_points()
        self.unprocessed_loads: List[int] = list(self.load_map.keys())
        self.processed_loads: List[int] = []
        self.drivers_list: List[Driver] = []

    def solve(self):

        while self.unprocessed_loads:
            driver: Driver = self.create_new_driver(len(self.drivers_list) + 1)
            self.drivers_list.append(driver)

        number_of_drivers: int = len(self.drivers_list)
        total_distance: float = sum(driver.total_distance for driver in self.drivers_list)

        for driver in self.drivers_list:
            schedule_list = [load.id for load in driver.loads]
            print(schedule_list)

        total_cost: float = 500 * number_of_drivers + total_distance

    def create_new_driver(self, driver_number: int):
        driver: Driver = Driver(driver_number)
        load_list: List[Load] = []
        self.add_route_schedule_for_driver(driver, self.nearest_pickup_points[0], load_list)
        driver.loads = load_list
        driver.total_distance += self.calculate_euclidean_distance(driver.current_location, self.depot_location)
        return driver

    def add_route_schedule_for_driver(self, driver: Driver, nearest_pickup_to_origin: List[ClosestLoadPoint],
                                      load_list: List[Load]):
        for i in nearest_pickup_to_origin:
            load_id: int = i.load_id
            if load_id not in self.processed_loads:
                load: Load = self.load_map[load_id]
                if self.check_feasibility(driver, load):
                    load_list.append(load)
                    self.processed_loads.append(load_id)
                    self.unprocessed_loads.remove(int(load_id))
                    self.add_route_schedule_for_driver(driver, self.nearest_pickup_points[load_id], load_list)

    def check_feasibility(self, driver: Driver, load: Load) -> bool:
        current_to_pickup: float = self.calculate_euclidean_distance(driver.current_location, load.pickup_location)
        pickup_to_drop_off: float = self.calculate_euclidean_distance(load.pickup_location, load.drop_off_location)
        drop_off_to_depot: float = self.calculate_euclidean_distance(load.drop_off_location, self.depot_location)
        trip_distance: float = current_to_pickup + pickup_to_drop_off + drop_off_to_depot
        if (720 - (trip_distance + driver.total_distance)) >= 0:
            driver.total_distance += current_to_pickup + pickup_to_drop_off
            driver.current_location = load.drop_off_location
            return True
        return False

    def create_load_map(self) -> Dict[int, Load]:
        load_map: Dict[int, Load] = {}
        with open(self.path, 'r') as file:
            for i, line in enumerate(file):
                if i == 0:
                    continue
                parts = line.strip().split()
                load_id = int(parts[0])
                pickup_coords: List[str] = parts[1][1:-1].split(',')
                drop_off_coords: List[str] = parts[2][1:-1].split(',')
                pickup_location: Location = Location(float(pickup_coords[0]), float(pickup_coords[1]))
                drop_off_location: Location = Location(float(drop_off_coords[0]), float(drop_off_coords[1]))
                load_map[load_id] = Load(load_id, pickup_location, drop_off_location)
        return load_map

    def create_nearest_pickup_points(self) -> Dict[int, List[ClosestLoadPoint]]:
        queue = deque()
        queue.append(Load(0, Location(0, 0), Location(0, 0)))

        for load in self.load_map.values():
            queue.append(load)

        nearest_pickup_points: Dict[int, List[ClosestLoadPoint]] = defaultdict(list)

        while queue:
            load_value: Load = queue.popleft()
            closest_pickup_loads_list: List[ClosestLoadPoint] = []

            for load in self.load_map.values():
                if load.id != load_value.id:
                    distance: float = self.calculate_euclidean_distance(load_value.drop_off_location,
                                                                        load.pickup_location)
                    closest_pickup_loads_list.append(ClosestLoadPoint(load.id, distance))

            closest_pickup_loads_list.sort(key=lambda x: x.distance)
            nearest_pickup_points[load_value.id] = closest_pickup_loads_list

        return nearest_pickup_points

    def calculate_euclidean_distance(self, loc1, loc2) -> float:
        return math.sqrt((loc2.x - loc1.x) ** 2 + (loc2.y - loc1.y) ** 2)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('dest')
    args = parser.parse_args()
    file_path = args.dest
    vrp = VRP(file_path)
    vrp.solve()
