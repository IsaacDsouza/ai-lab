def dfs(node, graph, visited, component):
    component.append(node)
    visited[node] = True

    for child in graph[node]:
        if not visited[child]:
            dfs(child, graph, visited, component)


if __name__ == "__main__":
# Graph of nodes
    graph = {
    0: [2],
    1: [2, 3],
    2: [0, 1, 4],
    3: [1, 4],
    4: [2, 3]
    }
    node = 0 # Starting node
    visited = [False]*len(graph) # Make all nodes to False initially
    component = []
    dfs(node, graph, visited, component) # Traverse to each node of a graph
    print(f"Following is the Depth-first search: {component}")