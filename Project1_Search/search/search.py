# search.py
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
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
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
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    
    discoveredStates = []                  #we hold all discovered states, in order to avoid them
    searchStack = util.Stack()              #we save nodes that will be discovered in this stack.  node=(state,action)
    startState =  problem.getStartState()  #gives us start state
    if problem.isGoalState(startState):    #checking if we reached our goal state
        return actions
    startNode = (startState, [])           #start node = start state + empty list of actions
    searchStack.push(startNode)           

    while searchStack.isEmpty()==False:
        currentNode = searchStack.pop()     #checking the last node saved in our stack
        currentState = currentNode[0]
        actions = currentNode[1]
        
        if problem.isGoalState(currentState):    #checking if we reached our goal state
            return actions
        
        if currentState not in discoveredStates:      #if we haven't reached this state yet, we register it as discovered
            discoveredStates.append(currentState)
        
            successors = problem.getSuccessors(currentState) #we use the list of possible successor nodes
            # returns successor states, the actions they require, and a cost of 1 
            for successor in successors:
                successorState = successor[0]
                successorAction = successor[1]
                newAction = actions + [successorAction]
                nextNode = (successorState, newAction)
                searchStack.push(nextNode)       #saving all successors in our stack
    return actions
    

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    discoveredStates = []                  #we hold all discovered states, in order to avoid them
    searchQueue = util.Queue()              #we save nodes that will be discovered in this queue.  node=(state,action)
    startState =  problem.getStartState()  #gives us start state
    if problem.isGoalState(startState):    #checking if we reached our goal state
        return actions
    startNode = (startState, [])           #start node = start state + empty list of actions
    searchQueue.push(startNode)           

    while searchQueue.isEmpty()==False:
        currentNode = searchQueue.pop()     #checking the last node saved in our queue
        currentState = currentNode[0]
        actions = currentNode[1]
        
        if problem.isGoalState(currentState):    #checking if we reached our goal state
            return actions
        
        if currentState not in discoveredStates:      #if we haven't reached this state yet, we register it as discovered
            discoveredStates.append(currentState)
        
            successors = problem.getSuccessors(currentState) #we use the list of possible successor nodes
            # returns successor states, the actions they require, and a cost of 1 
            for successor in successors:
                successorState = successor[0]
                successorAction = successor[1]
                newAction = actions + [successorAction]
                nextNode = (successorState, newAction)
                searchQueue.push(nextNode)       #saving all successors in our queue
    return actions


def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    discoveredStates = []                  #we hold all discovered states, in order to avoid them
    searchPriorityQueue = util.PriorityQueue()              #we save nodes that will be discovered in this PriorityQueue.  
    startState =  problem.getStartState()  #gives us start state
    if problem.isGoalState(startState):    #checking if we reached our goal state
        return actions
    startNode = (startState, [], 0)           #start node = start state + empty list of actions
    searchPriorityQueue.push(startNode, 0)           

    while searchPriorityQueue.isEmpty()==False:
        currentNode = searchPriorityQueue.pop()     #checking the last node saved in our PriorityQueue
        currentState = currentNode[0]
        actions = currentNode[1]
        currentCost = currentNode[2]

        if problem.isGoalState(currentState):    #checking if we reached our goal state
            return actions
       
        if currentState not in discoveredStates:      #if we haven't reached this state yet, we register it as discovered
            discoveredStates.append(currentState)

            successors = problem.getSuccessors(currentState) #we use the list of possible successor nodes
             
            for successor in successors:
                successorState = successor[0]
                successorAction = successor[1]
                successorCost = successor[2]
                newAction = actions + [successorAction]
                newCost = currentCost + successorCost
                nextNode = (successorState, newAction, newCost)
                searchPriorityQueue.push(nextNode, newCost)       #saving all successors in our PriorityQueue
    return actions


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    discoveredStates = []                  #we hold all discovered states, in order to avoid them
    searchPriorityQueue = util.PriorityQueue()              #we save nodes that will be discovered in this PriorityQueue.  
    startState =  problem.getStartState()  #gives us start state
    if problem.isGoalState(startState):    #checking if we reached our goal state
        return actions
    startNode = (startState, [], 0)           #start node = start state + empty list of actions
    searchPriorityQueue.push(startNode, 0)           

    while searchPriorityQueue.isEmpty()==False:
        currentNode = searchPriorityQueue.pop()     #checking the last node saved in our PriorityQueue
        currentState = currentNode[0]
        actions = currentNode[1]
        currentCost = currentNode[2]

        if problem.isGoalState(currentState):    #checking if we reached our goal state
            return actions
       
        if currentState not in discoveredStates:      #if we haven't reached this state yet, we register it as discovered
            discoveredStates.append(currentState)

            successors = problem.getSuccessors(currentState) #we use the list of possible successor nodes
            
            for successor in successors:
                successorState = successor[0]
                successorAction = successor[1]
                successorCost = successor[2]
                newAction = actions + [successorAction]
                newCost = currentCost + successorCost
                heuristicCost = newCost + heuristic(successorState,problem)
                nextNode = (successorState, newAction, newCost)
                searchPriorityQueue.push(nextNode, heuristicCost)       #saving all successors in our PriorityQueue
    return actions


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
