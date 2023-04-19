
class mazeRunner:
    """
    Maze runner needs 3 inputs
    1. The maze itself
    2. The entrance point into the maze
    3. The exit point out of the maze
    """
    def __init__(self, maze: list) -> None:
        super(mazeRunner, self).__init__()
        self.maze = maze

    def tracePath(self, entrancePoint: list, exitPoint: list) -> None:
        self.entrance = entrancePoint
        self.exit = exitPoint
        self.fullPath = []
        self.dfs(*self.entrance)

    def dfs(self, *args, **kwargs) -> None:
        pass


if __name__ == "__main__":
    pass
