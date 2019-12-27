# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """

        def backtrack(cell=(0, 0), facing=0):
            visited.add(cell)
            robot.clean()

            for i in range(4):
                new_facing = (facing + i) % 4
                new_cell = (cell[0] + moves[new_facing][0],
                            cell[1] + moves[new_facing][1])

                if new_cell not in visited and robot.move():
                    backtrack(new_cell, new_facing)
                    go_back()

                robot.turnRight()

        def go_back():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()

        visited = set()
        moves = [(0, -1), (1, 0), (0, 1), (-1, 0)]

        backtrack()
