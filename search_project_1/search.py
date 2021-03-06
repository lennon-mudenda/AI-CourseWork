# search_project_1.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search_project_1.py, you will implement generic search_project_1 algorithms which are called by
Pacman agents (in searchAgents.py).
"""
import util


class SearchProblem:
    """
    This class outlines the structure of a search_project_1 problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search_project_1 problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search_project_1 tree first.

    Your search_project_1 algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search_project_1 algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search_project_1 problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    visited = []
    fringe = util.Stack()
    root = {
        "state": problem.getStartState(),
        "path": []
    }
    fringe.push(root)
    visited.append(root)
    while not fringe.isEmpty():
        node = fringe.pop()
        if problem.isGoalState(node["state"]):
            return node["path"]
        else:
            successors = problem.getSuccessors(node["state"])
            for next in successors:
                if next[0] in visited:
                    continue
                fringe.push({
                    "state": next[0],
                    "path": node["path"] + [next[1]]
                })
                visited.append(next[0])


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search_project_1 tree first."""
    "*** YOUR CODE HERE ***"
    visited = []
    fringe = util.Queue()
    root = {
        "state": problem.getStartState(),
        "path": []
    }
    visited.append(root["state"])
    fringe.push(root)
    while not fringe.isEmpty():
        node = fringe.pop()
        if problem.isGoalState(node["state"]):
            return node["path"]
        successors = problem.getSuccessors(node["state"])
        for next in successors:
            if next[0] in visited:
                continue
            fringe.push({
                "state": next[0],
                "path": node["path"] + [next[1]]
            })
            visited.append(next[0])


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    visited = []
    fringe = util.PriorityQueue()
    root = {
        "state": problem.getStartState(),
        "path": [],
        "cost": 0
    }
    visited.append(root["state"])
    fringe.push(root, 0)
    while not fringe.isEmpty():
        node = fringe.pop()
        if problem.isGoalState(node["state"]):
            return node["path"]
        successors = problem.getSuccessors(node["state"])
        for next in successors:
            if next[0] in visited:
                continue
            fringe.push({
                "state": next[0],
                "path": node["path"] + [next[1]],
                "cost": node["cost"] + next[2]
            }, node["cost"] + next[2])
            visited.append(next[0])


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    visited = []
    fringe = util.PriorityQueue()
    root = {
        "state": problem.getStartState(),
        "path": [],
        "cost": 0
    }
    visited.append(root["state"])
    fringe.push(root, 0)
    while not fringe.isEmpty():
        node = fringe.pop()
        if problem.isGoalState(node["state"]):
            return node["path"]
        successors = problem.getSuccessors(node["state"])
        for next in successors:
            if next[0] in visited:
                continue
            fringe.push({
                "state": next[0],
                "path": node["path"] + [next[1]],
                "cost": node["cost"] + next[2]
            }, node["cost"] + next[2] + heuristic(next[0], problem))
            visited.append(next[0])


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch

