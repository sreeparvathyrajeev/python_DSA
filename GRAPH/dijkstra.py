import heapq
import math

# find shortest paths from start_node to all other nodes in a weighted graph
# create a previous_nodes map for path reconstruction

def dijkstra(graph,start_node):
    #initialize distances to all nodes as infinity
    distances = {node: math.inf for node in graph}
    #shortest distance to start node is 0
    distances[start_node] = 0
    #breadcrumb tracker
    previous_nodes = {}
    #priority queue to process nodes
    priority_queue = [(0,start_node)]
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        #skip if we found a better path already
        if current_distance > distances[current_node]:
            continue
        #explore neighbors
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            #only consider this new path if its better
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
                previous_nodes[neighbor] = current_node
    return distances, previous_nodes

def reconstruct_shortest_path(previous_nodes, start_node, end_node):
    path = []
    current_node = end_node
    while current_node != start_node:
        path.append(current_node)
        current_node=previous_nodes[current_node]
    path.append(start_node)
    path.reverse()
    return path