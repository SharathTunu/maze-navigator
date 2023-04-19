# Maze Navigator
Maze navigator navigates from the entrance of a maze to the only exit using Depth First Search(DFS) using Python. The source code for the mazeRunner is present in the "src" directory.

Depth-first search (DFS) is an algorithm for searching a graph or tree data structure. The algorithm starts at the root (top) node of a tree and goes as far as it can down a given branch (path), then backtracks until it finds an unexplored path, and then explores it. The algorithm does this until the entire graph has been explored. Many problems in computer science can be thought of in terms of graphs. For example, analyzing networks, mapping routes, scheduling, and finding spanning trees are graph problems. To analyze these problems, graph-search algorithms like depth-first search are useful.

For a bit more deeper reading please refer to: https://brilliant.org/wiki/depth-first-search-dfs/

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

* Move to all the adjacent nodes and continue this loop until there is no unmarked adjacent node while memorizing the path.


### Story 3:
Find a way into and out of rooms.
### Implementation:
Multiple hallways stacked together becomes a room or to put it simply multiple hallways with dead ends form a room. To navigate out of it we need to figure out where the dead ends are and what alternate routes can be found. To achieve this we need to:

* Fill up the path travelled with a walls and check for a new dead ends i.e., the bookmark the current position and propogate forward

* Open up the filled path i.e., undo the bookmark in a memory efficient way


### Story 4:
Follow winding paths.
### Implementation:
Its the same as rooms i.e., hallways hallways stacked together but instead of being side to side they are linked end to end. But the implementation approach for story 3 holds true for the story 4 as well


### Story 5:
Reach the end of the maze, even if there are dead ends.
### Implementation:
Compounded rooms (snaking hallways or rooms) will become a maze or and exit of one rooms will be entrance of the other. The DFS method of searching till a dead end, backtracking and looking for alternatives will pass through one room after another till reaches the exit. So looping step 3 until we reach the exit gives us the route out of the maze.