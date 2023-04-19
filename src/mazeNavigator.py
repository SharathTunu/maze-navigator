from visualize import visualize
from copy import deepcopy


class mazeRunner(visualize):
    """
    Maze runner needs 3 inputs
    1. The maze itself
    2. The entrance point into the maze
    3. The exit point out of the maze
    """
    def __init__(self, maze: list) -> None:
        super(mazeRunner, self).__init__()
        self.maze = maze

    def tracePath(self, entrancePoint: list, exitPoint: list, save_path: str) -> None:
        self.entrance = entrancePoint
        self.exit = exitPoint
        self.fullPath = []
        self.dfs(*self.entrance)
        self.save(save_path)

    def dfs(self, *args, **kwargs) -> None:
        """
        1.  a. Start from the entrance and mark the node in memory.
            b. Move to all the adjacent nodes and continue this loop until there is no unmarked adjacent node.
        2. Finding the alternate routes to dead ends i.e., explore hallways. 
            a. If we've already been there or there is a wall, quit
            b. Fill up the path travelled with a wall and check for a new dead ends
        3. Compounded rooms will become a maze and exit of one rooms will be entrance of the other
        """
        # 1a.
        i, j = args
        if i < 0 or j < 0 or i > len(self.maze)-1 or j > len(self.maze[0])-1:
            return
        # 2a.
        if (i, j) in self.fullPath or self.maze[i][j] > 0:
            return
        # 2b.
        self.fullPath.append((i, j))
        self.maze[i][j] = 2
        self.drawMaze(self.fullPath)

        # 1b.
        # No need to look further if exit is reached..
        if (i, j) == (self.exit[0], self.exit[1]):
            self.solution = deepcopy(self.fullPath)
            for animate in range(10):
                if animate % 2 == 0:
                    self.drawMaze(self.fullPath)
                else:
                    self.drawMaze()
            self.fullPath.pop()
            return
        else:
            self.dfs(i - 1, j)  # check top
            self.dfs(i + 1, j)  # check bottom
            self.dfs(i, j + 1)  # check right
            self.dfs(i, j - 1)  # check left
        
        self.fullPath.pop()
        self.drawMaze(self.fullPath)
        return


if __name__ == "__main__":
    maze = [[1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
            [1, 1, 1, 0, 0, 0, 0, 1, 0, 1],
            [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
            [1, 1, 1, 0, 0, 0, 1, 0, 0, 1],
            [1, 0, 1, 1, 1, 0, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
            [1, 1, 0, 1, 1, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 0, 1, 1]]

    maze1 = mazeRunner(maze)
    maze1.tracePath([0, 4], [9, 7], "../main_maze.gif")
    print(maze1.solution)
