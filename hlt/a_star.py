"""
A* Pathfinding on an exhaustive rectangular grid

TODO: change map representation to planets + in-between points for long distances, 20 unit radius for each ship
"""

class SimpleGraph:
    def __init__(self):
        self.edges = {}

        def neighbors(self, id):
            return self.edges[id]

