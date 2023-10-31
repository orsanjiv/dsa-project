#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <limits>

using namespace std;

const int INF = numeric_limits<int>::max();

class MetroMap {
public:
    map<string, vector<pair<string, int>> > metro;

    void addStation(const string& source, const string& destination, int distance) {
        metro[source].push_back(make_pair(destination, distance));
        metro[destination].push_back(make_pair(source, distance));
    }
};

class ShortestPathFinder {
public:
    map<string, int> dijkstra(const MetroMap& map, const string& source) {
        map<string, int> dist;
        set<pair<int, string>> pq;

        for (const auto& station : map.metro) {
            const string& node = station.first;
            dist[node] = INF;
        }

        dist[source] = 0;
        pq.insert(make_pair(0, source));

        while (!pq.empty()) {
            const string& u = pq.begin()->second;
            pq.erase(pq.begin());

            for (const auto& neighbor : map.metro.at(u)) {
                const string& v = neighbor.first;
                int weight = neighbor.second;

                if (dist[u] + weight < dist[v]) {
                    pq.erase(make_pair(dist[v], v));
                    dist[v] = dist[u] + weight;
                    pq.insert(make_pair(dist[v], v));
                }
            }
        }

        return dist;
    }
};

int main() {
    MetroMap map;
    ShortestPathFinder spf;

    map.addStation("station1", "station2", 5);
    map.addStation("station2", "station3", 4);
    map.addStation("station1", "station4", 10);
    map.addStation("station4", "station5", 3);
    map.addStation("station5", "station3", 6);
    map.addStation("station3", "station6", 7);
    map.addStation("station6", "station7", 2);
    map.addStation("station7", "station8", 8);
    map.addStation("station3", "station9", 12);
    map.addStation("station9", "station10", 5);

    string source;

    cout << "Select a source station (station1, station2, ..., station10): ";
    cin >> source;

    if (map.metro.find(source) == map.metro.end()) {
        cout << "Invalid source station." << endl;
        return 1;
    }

    map<string, int> shortestPaths = spf.dijkstra(map, source);

    cout << "Shortest distances from source " << source << " to other stations:" << endl;

    for (const auto& station : shortestPaths) {
        cout << "Station " << station.first << ": " << station.second << " units away" << endl;
    }

    return 0;
}
