from queue import PriorityQueue

def uniform_cost_search(start_node, goal_node, graph):
    frontier = PriorityQueue()
    frontier.put((0, start_node))
    explored = set()

    while not frontier.empty():
        current_cost, current_node = frontier.get()
        if current_node == goal_node:
            return current_cost
        explored.add(current_node)

        for neighbor, cost in graph[current_node].items():
            if neighbor not in explored:
                new_cost = current_cost + cost
                frontier.put((new_cost, neighbor))
    
    return -1

graph = {
'A': {'B': 5, 'C': 3},
'B': {'D': 2},
'C': {'D': 4},
'D': {}
}
start_node = 'A'
goal_node = 'D'
print(uniform_cost_search(start_node, goal_node, graph))