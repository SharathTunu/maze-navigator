
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
        """
        1.  a. Start from the entrance and mark the node in memory.
            b. Move to all the adjacent nodes and continue this loop until there is no unmarked adjacent node.
        2. Finding the alternate routes to dead ends i.e., explore hallways. 
            a. Fill up the path travelled with a wall and check for a new dead ends
            b. Open up the filled path
        3. Compounded rooms will become a maze and exit of one rooms will be entrance of the other
        """
        # 1a.
        i, j = args

        # 1b.
        # No need to look further if exit is reached..
        if (i, j) == (self.exit[0], self.exit[1]):
            return
        else:
            self.dfs(i - 1, j)  # check top
            self.dfs(i + 1, j)  # check bottom
            self.dfs(i, j + 1)  # check right
            self.dfs(i, j - 1)  # check left
        return


if __name__ == "__main__":
    pass
