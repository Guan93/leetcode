import collections


class UndergroundSystem:

    def __init__(self):
        self.checked_in = dict()
        self.travel_time = collections.defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checked_in[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, start_time = self.checked_in.pop(id)
        self.travel_time[(start_station, stationName)].append(t - start_time)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        t = self.travel_time[(startStation, endStation)]
        return sum(t) / len(t)

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)