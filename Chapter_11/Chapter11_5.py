def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    previous_nodes = {node: None for node in graph}
    
    unvisited = list(graph.keys())

    while unvisited:
        current_node = None
        current_distance = float('inf')
        for node in unvisited:
            if distances[node] < current_distance:
                current_distance = distances[node]
                current_node = node
        
        if current_node is None:
            break

        for neighbor, weight in graph[current_node].items():
            new_distance = distances[current_node] + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous_nodes[neighbor] = current_node

        unvisited.remove(current_node)
    
    return distances, previous_nodes


def get_path(previous_nodes, start, target):
    path = []
    node = target
    while node is not None:
        path.insert(0, node)
        node = previous_nodes[node]
    if path and path[0] == start:
        return path
    else:
        return None

print(" *** Dijkstra's shortest path ***")

graph = { 
    'A': {'B': 1, 'C': 2},
    'B': {'D': 12, 'A': 1}, 
    'C': {'D': 9, 'F': 3, 'A': 2}, 
    'D': {'C': 9, 'E': 7, 'G': 1},
    'E': {'G': 5, 'D': 7}, 
    'F': {'G': 4}, 
    'G': {'D': 1, 'E': 5, 'F': 4}
}

start, target = input("Enter start and target vertex : ").split()

distances, previous_nodes = dijkstra(graph, start)
path = get_path(previous_nodes, start, target)

if path is None:
    print(f"No path found from {start} to {target}")
else:
    print(f"Shortest distance is {distances[target]}")
    print(f"And the path is {path}")

# กำหนดกราฟรูปหนึ่งดังนี้

# graph = { 'A':{'B':1,'C':2},'B':{'D':12,'A':1}, 'C':{'D':9,'F':3,'A':2}, 'D':{'C':9,'E':7,'G':1},\
#          'E':{'G':5,'D':7}, 'F':{'G':4}, 'G':{'D':1,'E':5,'F':4} }


# ให้เขียนโปรแกรมเพื่อหา shortest path โดยใส่ข้อมูล เป็น vertex เริ่มต้น และ vertex สุดท้าย

#  *** Dijkstra's shortest path ***
# Enter start and target vertex : A D
# Shortest distance is 10
# And the path is ['A', 'C', 'F', 'G', 'D']


#  *** Dijkstra's shortest path ***
# Enter start and target vertex : B G
# Shortest distance is 10
# And the path is ['B', 'A', 'C', 'F', 'G']