# Greedy Search Algortihm(Prims Algorithm)
def prim(graph, start_node):
    mst = []  
    visited = set([start_node])  
    edges = []  
    total_cost = 0
    
    for neighbor, weight in graph[start_node]:
        edges.append((weight, start_node, neighbor))
    
    while edges:
        edges.sort()  
        weight, parent, node = edges.pop(0) 
        
        if node not in visited:
            visited.add(node)
            total_cost += weight
            mst.append((parent, node, weight))
            
            for neighbor, edge_weight in graph[node]:
                if neighbor not in visited:
                    edges.append((edge_weight, node, neighbor))
    
    return mst, total_cost

graph = {}
n = int(input("Enter number of edges: "))
for _ in range(n):
    u, v, w = input("Enter edge (node1 node2 weight): ").split()
    w = int(w)
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append((v, w))
    graph[v].append((u, w))

start_node = input("Enter start node: ")
mst, cost = prim(graph, start_node)
print("Minimum Spanning Tree:", mst)
print("Total Cost:", cost)
