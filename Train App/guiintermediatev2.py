import tkinter as tk

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

# Add stations to the map (same as your existing code)
map.add_station("Munshi Pulia", "Indira Nagar", 5)
map.add_station("Indira Nagar", "Bhootnath Market", 4)
map.add_station("Bhootnath Market", "Lekhraj Market", 10)
map.add_station("Lekhraj Market", "Badshah Nagar", 3)
map.add_station("Badshah Nagar", "IT Chauraha", 6)
map.add_station("IT Chauraha", "Vishwavidyalaya", 7)
map.add_station("Vishwavidyalaya", "KD Singh Stadium", 2)
map.add_station("KD Singh Stadium", "Hazratganj", 8)
map.add_station("Hazratganj", "Sachivalaya", 12)
map.add_station("Sachivalaya", "Husain Ganj", 5)
map.add_station("Husain Ganj", "Charbagh", 8)
map.add_station("Charbagh", "Durgapuri", 7)
map.add_station("Durgapuri", "Mawalya", 2)
map.add_station("Mawalya", "Alambagh Bus Station", 8)
map.add_station("Alambagh Bus Station", "Alambagh", 12)
map.add_station("Alambagh", "Singer Nagar", 5)
map.add_station("Singer Nagar", "Krishna Nagar", 26)
map.add_station("Krishna Nagar", "Transport Nagar", 21)
map.add_station("Transport Nagar", "Amausi", 26)
map.add_station("Amausi", "CCS Airport", 0)

# Create a function for the "List stations" action
def list_stations():
    stations = spf.list_stations()
    station_list.delete(0, tk.END)
    for station in stations:
        station_list.insert(tk.END, station)

# Create a function for the "Find shortest path" action
def find_shortest_path():
    source = source_entry.get()
    destination = destination_entry.get()
    shortest_path = spf.find_shortest_path(source, destination)
    result_label.config(text=shortest_path)

# Create the main GUI window
root = tk.Tk()
root.title("Metro Map Shortest Path Finder")

# Create a frame for the list of stations
stations_frame = tk.Frame(root)
stations_frame.pack(side=tk.LEFT, padx=10)
tk.Label(stations_frame, text="List of available stations:").pack()
station_list = tk.Listbox(stations_frame)
station_list.pack()

# Create a frame for the shortest path action
action_frame = tk.Frame(root)
action_frame.pack(side=tk.LEFT, padx=10)
tk.Label(action_frame, text="Source Station:").pack()
source_entry = tk.Entry(action_frame)
source_entry.pack()
tk.Label(action_frame, text="Destination Station:").pack()
destination_entry = tk.Entry(action_frame)
destination_entry.pack()
find_button = tk.Button(action_frame, text="Find Shortest Path", command=find_shortest_path)
find_button.pack()
result_label = tk.Label(action_frame, text="", wraplength=200)
result_label.pack()

# Create a frame for the exit button
exit_frame = tk.Frame(root)
exit_frame.pack(pady=20)
exit_button = tk.Button(exit_frame, text="Exit", command=root.destroy)
exit_button.pack()

# Create a function to update the station list when the GUI is initialized
def update_station_list():
    list_stations()

update_station_list()

# Start the GUI main loop
root.mainloop()
