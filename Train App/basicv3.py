class MetroMap:
    def __init__(self):
        self.metro = {}

    def add_station(self, source, destination, distance):
        self.metro.setdefault(source, []).append((destination, distance))
        self.metro.setdefault(destination, []).append((source, distance))

class ShortestPathFinder:
    def __init__(self, map):
        self.map = map
        self.dist = {}
        self.pq = []
        self.shortest_paths = {}

    def dijkstra(self, source):
        for station in self.map.metro.keys():
            self.dist[station] = float('inf')

        self.dist[source] = 0
        self.pq.append((0, source))

        while self.pq:
            self.pq.sort()  # Sort the queue by distance
            u = self.pq[0][1]
            self.pq.pop(0)

            for neighbor, weight in self.map.metro[u]:
                if self.dist[u] + weight < self.dist[neighbor]:
                    self.pq.append((self.dist[u] + weight, neighbor))
                    self.dist[neighbor] = self.dist[u] + weight

    def find_shortest_path(self, source, destination):
        if source not in self.map.metro or destination not in self.map.metro:
            return "Invalid source or destination station."

        self.dijkstra(source)

        if self.dist[destination] == float('inf'):
            return f"No path found from {source} to {destination}."

        path = []
        current_station = destination
        while current_station != source:
            path.append(current_station)
            for neighbor, weight in self.map.metro[current_station]:
                if self.dist[current_station] == self.dist[neighbor] + weight:
                    current_station = neighbor
                    break
        path.append(source)
        path.reverse()

        return f"Shortest path from {source} to {destination}: {' -> '.join(path)}"

    def list_stations(self):
        return list(self.map.metro.keys())

map = MetroMap()
spf = ShortestPathFinder(map)

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

print("List of available stations:", spf.list_stations())

source = input("Select a source station (station1, station2, ..., station10): ")
destination = input("Select a destination station (station1, station2, ..., station10): ")

shortest_path = spf.find_shortest_path(source, destination)
print(shortest_path)
