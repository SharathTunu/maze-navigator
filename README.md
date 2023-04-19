# Maze Navigator
Maze navigator navigates from the entrance of a maze to the only exit using Depth First Search(DFS) using Python. The source code for the mazeRunner is present in the "src" directory.

Depth-first search (DFS) is an algorithm for searching a graph or tree data structure. The algorithm starts at the root (top) node of a tree and goes as far as it can down a given branch (path), then backtracks until it finds an unexplored path, and then explores it. The algorithm does this until the entire graph has been explored. Many problems in computer science can be thought of in terms of graphs. For example, analyzing networks, mapping routes, scheduling, and finding spanning trees are graph problems. To analyze these problems, graph-search algorithms like depth-first search are useful.

For a bit more deeper reading please refer to: https://brilliant.org/wiki/depth-first-search-dfs/

## Setup and Install

### Prerequisites
* python >= 3.8
* Linux OS (preferable)
* python3-pip
* Internet access to download and install pypi packages

### Installtion
clone the repo by using:
```
git clone https://github.com/SharathTunu/maze-navigator.git
```

Go the root dir off the repo maze-navigator and install the requirements:
```
cd maze-navigator/scripts
python3 -m pip install -r requirements.txt
```

To run the tests which will print out the desired output in the terminal and outputs in the maze-navigator/tests/visualizations:
```
cd ../tests
python3 unitTest.py

cd visualizations
ll
```
### How to run custom tests:
#### Option a:
You'd have to edit the tests/unitTest.py and add a new funtion with the following template:

```
def test_<random_name>():
    
    maze = [[1, 1, 0, 1], 
            [1, 1, 0, 1],
            [1, 1, 0, 1],
            [1, 1, 0, 1]] # A list of lists with m*n shape where 1s are walls and 0s are open spaces...

    entry = [0, 2]  # i, j are the row, column positions for the maze
    exit = [3, 2]  # i, j are the row, column positions for the maze
    im_path = os.path.join(TEST_DIR, "visualizations/test_<random_name>.gif")
    test_maze_navigator(maze, entry, exit, im_path)
```
If the custom data follows the main assumpltions stated below a gif will be created at the path im_path described in the function.

#### Option b:
Edit the main function in the src/mazeNavigator.py file and provide the required information. And then run the script.

```
cd maze-navigator/src

vi mazeNavigator.py
# Replace the existing test data with new data

python3 mazeNavigator.py

```

## Objective
An algorithm that can solve simple mazes.

## Understanding, Implementation and Assumptions

### Main assumptions:
There is ONLY 1 entrance and ONLY 1 exit and they are SEPERATE.
The whole maze is already described. i.e., maze DOES NOT shift.

### Story 1:
Find the “empty” space in a single-row input.
### Assumption:
The "walls" of the maze are denoted by "1" and "empty" spaces that make up the pathways are denoted by "0"


### Story 2:
Walk through a “hallway” maze.
### Implementation:
To find hallways we would have to find all the empty spaces around the current pick the element with lower index and commit it to the cache and move forward until we hit a dead end. That's achieved in 2 steps

* Start from the entrance and mark the node in memory.

* Move to all of the adjacent nodes and continue this loop until there is no unmarked adjacent node while memorizing the path.


### Story 3:
Find a way into and out of rooms.
### Implementation:
Multiple hallways stacked together becomes a room or to put it simply multiple hallways with dead ends form a room. To navigate out of it we need to figure out where the dead ends are and what alternate routes can be found. To achieve this we need to:

* Fill up the path travelled with a walls and check for a new dead ends i.e., the bookmark the current position and propogate forward

* Open up the filled path i.e., undo the bookmark in a memory efficient way


### Story 4:
Follow winding paths.
### Implementation:
Its the same as rooms i.e., hallways stacked together but instead of being side to side they are linked end to end. But the implementation approach for story 3 holds true for the story 4 as well


### Story 5:
Reach the end of the maze, even if there are dead ends.
### Implementation:
Compounded rooms (snaking hallways or rooms) will become a maze or and exit of one rooms will be entrance of the other. The DFS method of searching till a dead end, backtracking and looking for alternatives will pass through one room after another till reaches the exit. So looping step 3 until we reach the exit gives us the route out of the maze.



## Analysis

### Analysis Story 1
At this point, you may have created a general-purpose solver. If not, try to identify some types of mazes that your algorithm would not solve correctly.
### Response
Yes, the code in this repo can solve most of the mazes. The exceptions being the mazes where the path ways loop with no exits, and some times it provides a longer exit path if there are more than 2 routes to exit.

###  Analysis Story 2
If you kept things simple, it is likely that your algorithm may not be as efficient as possible. Describe the solution’s complexity and approaches that could be used to optimize it further.
### Response
Complexity values: Without visualization the solution's both time and space complexties are O(m*n), where m and n are the dimensions of the maze, when all the braches are traversed.

Optimization method: Instead of looking dead end using DFS its easier to implement BFS where we only pick the nodes that connected to the row below (directly or indirectly) which would significamtly reduce the time complexity unlike DFS where in this scenario the complexity is always at max.

### Analysis Story 3
Moving robots isn’t as simple as moving a 1x1 pixel through a maze. Instead, we must plan a path while avoiding obstacles using a collision model. We can approximate this by plotting a path for a 1x3 “ship” through a maze. In addition to moving “backward” and “forward” the ship can also rotate around its center of gravity provided it is in the center of a 3x3
Do not code a solution, but instead describe an approach for decomposing this problem into incremental stories as done for the maze problem above.

### Response

### Story 1:
Find the rows with open spaces

### Story 2:
Find paths that a minumum of 3 cells long horizontally or vertically

### Story 3:
At the end of the path way should open up to 3*3 "room" so that the object can fit horizonatlly or vertically in to 1 of the 6 postions. Use this distiction to disqalify and path ways that obsturct the transtition of the end effector in to its next turn.

### Story 4:
Repeat the above steps till the "1*3" end effector reaches the exit

