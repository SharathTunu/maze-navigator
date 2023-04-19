import os
import sys

TEST_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(TEST_DIR + "/../src")
from mazeNavigator import mazeRunner


os.makedirs(TEST_DIR + "/visualizations", exist_ok= True)


def test_maze_navigator(maze, start, end, image_path):
    maze1 = mazeRunner(maze)
    maze1.tracePath(start, end, image_path)
    print("Correct path:", maze1.solution)
    print("-----------------------------------")

def test_story2():
    
    maze = [[1, 1, 0, 1],
            [1, 1, 0, 1],
            [1, 1, 0, 1],
            [1, 1, 0, 1]]
    test_maze_navigator(maze, [0, 2], [3, 2], os.path.join(TEST_DIR, "visualizations/test_story2.gif"))

def test_story3():
    maze = [[1, 0, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 1, 1, 0, 1]]

    test_maze_navigator(maze, [0, 1], [3, 3], os.path.join(TEST_DIR, "visualizations/test_story3.gif"))

def test_story4():
    maze = [[1, 0, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 1, 1, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 1, 1, 0, 1]]

    test_maze_navigator(maze, [0, 1], [6, 3], os.path.join(TEST_DIR, "visualizations/test_story4.gif"))

def test_story5():
    maze = [[1, 0, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 1, 1, 1],
            [1, 0, 0, 0, 0],
            [1, 0, 1, 0, 1],
            [1, 1, 1, 0, 1]]

    test_maze_navigator(maze, [0, 1], [5, 3], os.path.join(TEST_DIR, "visualizations/test_story5.gif"))

def test_main_maze():
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

    test_maze_navigator(maze, [0, 4], [9, 7], os.path.join(TEST_DIR, "visualizations/main_maze.gif"))

if __name__ == "__main__":

    test_story2()
    test_story3()
    test_story4()
    test_story5()
    test_main_maze()

    # Add any kind of maze with proper entrnace and exit values and the right path along with the visualized out will be genretaed.