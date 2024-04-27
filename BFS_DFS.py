from collections import deque

def bfs(graph, start, goal):
    visited = set()
    queue = deque([(start, [start])])

    while queue:
        print(f"BFS Queue: {[(n, path) for n, path in queue]}")
        node, path = queue.popleft()
        if node not in visited:
            visited.add(node)
            print(f"BFS Traversal: Visiting Node {node}")
            if node == goal:
                print(f"Path from {start} to {goal}: {', '.join(path)}")
                return
            neighbors = graph.get(node, [])
            for neighbor in neighbors:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))

def dfs(graph, start, goal):
    visited = set()
    stack = [(start, [start])]

    while stack:
        print(f"DFS Stack: {[(n, path) for n, path in stack]}")
        node, path = stack.pop()
        if node not in visited:
            visited.add(node)
            print(f"DFS Traversal: Visiting Node {node}")
            if node == goal:
                print(f"Path from {start} to {goal}: {', '.join(path)}")
                return
            neighbors = graph.get(node, [])
            for neighbor in neighbors:
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))

# Function to create the graph from user input
def create_graph():
    graph = {}
    num_nodes = int(input("Enter the number of nodes: "))

    for i in range(num_nodes):
        node = input(f"Enter node {i + 1}: ")
        connected_nodes = input(f"Enter nodes connected to {node} (separated by spaces): ").split()
        graph[node] = connected_nodes

    return graph

# Get user input for the graph
graph = create_graph()

start_node = input("Enter the start node: ")
goal_node = input("Enter the goal node: ")

bfs(graph, start_node, goal_node)
dfs(graph, start_node, goal_node)
