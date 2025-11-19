inp = input("Enter : ").split(',')
graph = {}

for path in inp:
    node = path.strip().split()
    if len(node) == 2:
        key, value = node
        if key in graph:
            graph[key].append(value)
        else:
            graph[key] = [value]

nodes = set(graph.keys())
for values in graph.values():
    nodes.update(values)  

nodes = sorted(nodes)

node_index = {node: idx for idx, node in enumerate(nodes)}

size = len(nodes)
matrix = [[0] * size for _ in range(size)]

for src, destinations in graph.items():
    for dst in destinations:
        i = node_index[src]
        j = node_index[dst]
        matrix[i][j] = 1

print("    " + "  ".join(nodes))
for i, row in enumerate(matrix):
    print(f"{nodes[i]} : " + ", ".join(map(str, row)))

# รับ input เป็น list คู่อันดับ(เช่น A B,B C = A ไปหา B ได้ และ B ไปหา C ได้) ให้สร้าง Directed Graph จากนั้นให้แสดงผล adjacency metrix ของ graph 

