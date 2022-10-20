from collections import deque


class Problem:
    def __init__(self, init_state, goal_state):
        self.initial_state = init_state
        self.goal_state = goal_state
        self.state_space = {'Arad': {'R1': 'Zerind', 'R2': 'Sibiu', 'R3': 'Timisoara'},
                            'Zerind': {'R1': 'Oradea', 'R2': 'Arad'}, 'Oradea': {'R1': 'Sibiu', 'R2': 'Zerind'},
                            'Timisoara': {'R1': 'Lugoj', 'R2': 'Arad'}, 'Lugoj': {'R1': 'Timisoara', 'R2': 'Mehandia'},
                            'Drobeta': {'R1': 'Mehandia', 'R2': 'Craiova'},
                            'Craiova': {'R1': 'Drobeta', 'R2': 'Rimnicu Vilcea', 'R3': 'Pitesti'},
                            'Rimnicu Vilcea': {'R1': 'Sibiu', 'R2': 'Pitesti', 'R3': 'Craiova'},
                            'Sibiu': {'R1': 'Arad', 'R2': 'Fagaras', 'R3': 'Oradea', 'R4': 'Rimnicu Vilcea'},
                            'Fagaras': {'R1': 'Sibiu', 'R2': 'Bucharest'},
                            'Pitesti': {'R1': 'Rimnicu Vilcea', 'R2': 'Craiova', 'R3': 'Bucharest'},
                            'Bucharest': {'R1': 'Fagaras', 'R2': 'Pitesti', 'R3': 'Giurgiu', 'R4': 'Urziceni'},
                            'Giurgiu': {'R1': 'Bucharest'},
                            'Urziceni': {'R1': 'Bucharest', 'R2': 'Valsui', 'R3': 'Hirsova'},
                            'Hirsova': {'R1': 'Eforie', 'R2': 'Urziceni'}, 'Eforie': {'R1': 'Hirsova'},
                            'Valsui': {'R1': 'Urziceni', 'R2': 'Iasi'}, 'Iasi': {'R1': 'Valsui', 'R2': 'Neamt'},
                            'Neamt': {'R1': 'Iasi'}, 'Mehandia': {'R1': 'Lugoj', 'R2': 'Drobeta'}}

        self.step_cost = {'Arad': {'R1': 75, 'R2': 140, 'R3': 118}, 'Zerind': {'R1': 71, 'R2': 75},
                          'Oradea': {'R1': 152, 'R2': 71}, 'Timisoara': {'R1': 111, 'R2': 118},
                          'Lugoj': {'R1': 111, 'R2': 70}, 'Drobeta': {'R1': 75, 'R2': 120},
                          'Craiova': {'R1': 120, 'R2': 146, 'R3': 138},
                          'Rimnicu Vilcea': {'R1': 80, 'R3': 97, 'R4': 146},
                          'Sibiu': {'R1': 140, 'R2': 99, 'R3': 151, 'R4': 80}, 'Fagaras': {'R1': 99, 'R2': 211},
                          'Pitesti': {'R1': 97, 'R2': 138, 'R3': 101},
                          'Bucharest': {'R1': 211, 'R2': 101, 'R3': 90, 'R4': 85}, 'Giurgiu': {'R1': 90},
                          'Urziceni': {'R1': 85, 'R2': 142, 'R3': 98}, 'Hirsova': {'R1': 86, 'R2': 98},
                          'Eforie': {'R1': 86}, 'Valsui': {'R1': 142, 'R2': 92}, 'Iasi': {'R1': 92, 'R2': 87},
                          'Neamt': {'R1': 87}, 'Mehandia': {'R1': 70, 'R2': 75}}

    def Actions(self, state):
        lst = self.state_space[state].keys()
        return lst

    def Result(self, state, action):
        return self.state_space[state][action]

    def Goal_test(self, state):
        return state == self.goal_state

    def Path_cost(self, state, action):
        return self.step_cost[state][action]


# ------------------------------------------------------

class Node:

    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost

    def __repr__(self):
        return "-> {} {}".format(self.state, self.path_cost)

    # def __lt__(self, node):
    #     return isinstance(node, Node) and self.state < node.state
    #
    # def __eq__(self, other):
    #     return isinstance(other, Node) and self.state == other.state


# ------------------------------------------------------

def child_node(problem, parent, action):
    next_state = problem.Result(parent.state, action)
    step_cost = problem.Path_cost(parent.state, action)
    next_node = Node(next_state, parent, action, parent.path_cost + int(step_cost))
    return next_node


def solution(node):
    path_back = []
    while node:
        path_back.append(node)
        node = node.parent
    for n in reversed(path_back):
        print(n)


# ------------------------------------------------------

def DFS(problem):
    node = Node(problem.initial_state)
    if problem.Goal_test(node.state):
        return solution(node)
    frontier = deque()
    frontier.append(node)
    explored = []
    while True:
        if not frontier:
            return print('Failure')
        node = frontier.pop()
        explored.append(node.state)
        for action in problem.Actions(node.state):
            child = child_node(problem, node, action)
            if child.state not in explored and child not in frontier:
                if problem.Goal_test(child.state):
                    return solution(child)
                frontier.append(child)


# ------------------------------------------------------

p = Problem('Arad', 'Bucharest')
DFS(p)
