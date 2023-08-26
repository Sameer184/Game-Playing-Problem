Title: Game Playing Problem

Description: Task is to build an agent to play a modified version of nim (called red-blue nim against a human player). The game consists of two piles of marbles (red and blue). On each players turn they pick a pile and remove one marble from it. If on their turn, either pile is empty then they win. The amount they win is dependent on the number of marbles left (2 for every red marble and 3 for every blue marble). So if on the computer player turn, it has 0 red marbles and 3 blue marbles, it wins 9 points.

Programming Language used: Python

Code Structure:
main - The primary function that executes the entire program is this one.
mab_common - To determine whether action is better (basically best move)
mab_helper_1 - Helper method for setting negative values while pruning is being started in the negative case
mab_helper_2 - Helper method to start pruning in the positive case when setting positive values.
mab_func - The alpha-beta pruning process was started by this function.


Steps to run the code:
1. Navigate the current working directory where all the project files have been extracted.
2. Open the command prompt in the same current path.
3. Run the following commands:
> python Red_Blue_Nim.py 2 4
> python Red_Blue_Nim.py 2 4 computer
> python Red_Blue_Nim.py 2 4 human
> python Red_Blue_Nim.py 2 6 computer 5