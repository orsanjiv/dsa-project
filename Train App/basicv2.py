from queue import PriorityQueue

class MetroMap:
    def __init__(self):
        self.metro = {}

    def add_station(self, source, destination, distance):
        self.metro.setdefault(source, []).append((destination, distance))
        self.metro.setdefault(destination, []).append((source, distance))

class ShortestPathFinder:
    def dijkstra(self, map, source):
        dist = {}
        pq = PriorityQueue()

        for station in map.metro.keys():
            dist[station] = float('inf')

        dist[source] = 0
        pq.put((0, source))

        while not pq.empty():
            u = pq.get()[1]

            for neighbor, weight in map.metro[u]:
                if dist[u] + weight < dist[neighbor]:
                    pq.put((dist[u] + weight, neighbor))
                    dist[neighbor] = dist[u] + weight

        return dist

map = MetroMap()
spf = ShortestPathFinder()

map.add_station("station1", "station2", 5)
map.add_station("station2", "station3", 4)
map.add_station("station1", "station4", 10)
map.add_station("station4", "station5", 3)
map.add_station("station5", "station3", 6)
map.add_station("station3", "station6", 7)
map.add_station("station6", "station7", 2)
map.add_station("station7", "station8", 8)
map.add_station("station3", "station9", 12)
map.add_station("station9", "station10", 5)

source = input("Select a source station (station1, station2, ..., station10): ")

if source not in map.metro:
    print("Invalid source station.")
else:
    shortest_paths = spf.dijkstra(map, source)

    print(f"Shortest distances from source {source} to other stations:")
    for station, distance in shortest_paths.items():
        print(f"Station {station}: {distance} units away")
