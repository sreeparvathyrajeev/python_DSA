#as an adjacency list
graph1 = {
    'A':[('B',4),('C',8)],
    'B':[('A',4),('C',5),('D',3),('E',1)],
    'C':[('A',8),('B',5),('E',9)],
    'D':[('B',3),('E',4),('F',2)],
    'E':[('B',1),('C',9),('D',4),('F',6)],
    'F':[('D',2),('E',6)]   
}

#find edge weight between two nodes
def find_edge_weight(graph, node1, node2):
    for neighbor, weight in graph[node1]:
        if neighbor == node2:
            return weight

weight_AC = find_edge_weight(graph1, 'A', 'C')
print(f"Edge weight between A and C: {weight_AC}")