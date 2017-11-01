"""
A* Pathfinding on an exhaustive rectangular grid

TODO: change map representation to planets + in-between points for long distances, 20 unit radius for each ship
"""

import collections
import heapq

class Queue:
    """
    A data structure used by the algorithm to determine which order to process the locations
    """

    def __init__(self):
        self.elements = collections.deque()

    def empty(self):
        return len(self.elements) == 0

    def put(self, x):
        self.elements.append(x)

    def get(self):
        return self.elements.popleft()


class SimpleGraph:
    """
    A data structure that identifies the neighbors for each location
    """

    def __init__(self):
        self.edges = {}

    def neighbors(self, id):
        return self.edges[id]


class SquareGrid:
    """
    A data structure that defines a square (rectangular) grid as a series of locations
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.walls = []

    def in_bounds(self, id):
        (x, y) = id
        return 0 <= x < self.width and 0 <= y < self.height

    def passable(self, id):
        return id not in self.walls

    def neightbors(self, id):
        (x, y) = id
        results = [(x + 1, y), (x, y - 1), (x - 1, y), (x, y + 1)]
        if (x + y) % 2 == 0: results.reverse()  # aesthetics
        results = filter(self.in_bounds, results)
        results = filter(self.passable, results)
        return results


class GridWithWeights(SquareGrid):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.weights = {}

    def cost(self, from_node, to_node):
        return self.weights.get(to_node, 1)

class PriorityQueue:
    def __int__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappush(self.elements)[1]


# TODO start implementation at 1.3.3 SEARCH

# example_graph = SimpleGraph()
# example_graph.edges = {
#     'A': ['B'],
#     'B': ['A', 'C', 'D'],
#     'C': ['A'],
#     'D': ['E', 'A'],
#     'E': ['B'],
# }

g = SquareGrid(30, 15)
g.walls =


def breadth_first_search_1(graph, start):
    # print out what we find
    frontier = Queue()
    frontier.put(start)
    came_from = {}
    came_from[start] = None

    while not frontier.empty():
        current = frontier.get()

        if current == goal():
            break

        for next in graph.neighbors(current):
            if next not in came_from:
                frontier.put(next)
                came_from[next] = True

    return came_from


breadth_first_search_1(example_graph, "A")
