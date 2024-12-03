# multiAgents.py
# --------------
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


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent
from pacman import GameState

class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """


    def getAction(self, gameState: GameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState: GameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        "*** YOUR CODE HERE ***"
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPacmanPos = successorGameState.getPacmanPosition()
       
        score = 0

        #initializing distance from food and ghost
        foodLimit = float("inf")
        ghostLimit = float("inf")

        #min distance from food
        newFood = successorGameState.getFood().asList()
        for food in newFood:
            foodDistance = manhattanDistance(newPacmanPos, food)
            foodLimit = min(foodLimit, foodDistance)
        # we add 1/its_min_distance_from_the_food 
        score += 1 / foodLimit

        #min distance from a ghost
        newGhostPos = successorGameState.getGhostPositions()
        for ghost in newGhostPos:
            ghostDistance = manhattanDistance(newPacmanPos, ghost)
            ghostLimit = min (ghostLimit, ghostDistance)
        #if this distance is smaller than 5, we need to send pacman far away. we show this by decreasing the score by 100 as a signal!
        if ghostLimit < 5:
            score -= 200

        score += successorGameState.getScore()

        return score

def scoreEvaluationFunction(currentGameState: GameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 2)
    """

    def getAction(self, gameState: GameState):
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing minimax.

        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

        gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

        gameState.getNumAgents():
        Returns the total number of agents in the game

        gameState.isWin():
        Returns whether or not the game state is a winning state

        gameState.isLose():
        Returns whether or not the game state is a losing state
        """
        "*** YOUR CODE HERE ***"
        action = self.minimaxDecision(gameState)
        return action
        
        
    def minimaxDecision(self, gameState):
        depth = 0
        agentIndex = 0
        return self.maxValue(gameState, depth, agentIndex)[1]


    def minimaxFunction(self, gameState, depth, agentIndex):
        if self.terminalTest(gameState, depth, agentIndex) == True:
            return self.evaluationFunction(gameState)
        elif agentIndex >= 1:  #if it is a ghost
            return self.minValue(gameState, depth, agentIndex)[0]
        elif agentIndex == 0: #if it is pacman
            return self.maxValue(gameState, depth, agentIndex)[0]


    def terminalTest(self, gameState, depth, agentIndex):          #returns True if this is terminal state  //  returns False if not
        if gameState.getLegalActions(agentIndex)==0:
            return True
        elif gameState.isLose():
            return True
        elif gameState.isWin():
            return True
        elif depth ==  self.depth * gameState.getNumAgents():
            return True

        return False

        
    def minValue(self, gameState, depth, agentIndex):
        v = float("inf")
        actions = gameState.getLegalActions(agentIndex)
        numAgents = gameState.getNumAgents()
        currentAgentIndex = (depth + 1) % numAgents
        for action in actions:
            minimax = self.minimaxFunction(gameState.generateSuccessor(agentIndex,action), depth+1, currentAgentIndex)
            #find min value returned from minimaxFunction in order to find the node with the min value
            if minimax == v:
                bestAction = action
            elif minimax < v:
                v = minimax
                bestAction = action

        return v, bestAction


    def maxValue(self, gameState, depth, agentIndex):
        v = -float("inf")
        actions = gameState.getLegalActions(agentIndex)
        numAgents = gameState.getNumAgents()
        currentAgentIndex = (depth + 1) % numAgents
        for action in actions:
            minimax = self.minimaxFunction(gameState.generateSuccessor(agentIndex,action), depth+1, currentAgentIndex)
            #find max value returned from minimaxFunction in order to find the node with the max value
            if minimax == v:
                bestAction = action
            elif minimax > v:
                v = minimax
                bestAction = action
            
        return v, bestAction


class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState: GameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        action = self.abSearch(gameState)
        return action

    
    def abSearch(self, gameState):
        depth = 0
        agentIndex = 0
        a = -float("inf")
        b = float("inf")
        return self.maxValue(gameState, depth, agentIndex, a, b)[1]
    
    
    def terminalTest(self, gameState, depth, agentIndex):          #returns True if this is terminal state  //  returns False if not
        if gameState.getLegalActions(agentIndex)==0:
            return True
        elif gameState.isLose():
            return True
        elif gameState.isWin():
            return True
        elif depth ==  self.depth * gameState.getNumAgents():
            return True

        return False

    def abFunction(self, gameState, depth, agentIndex, a, b):
        if self.terminalTest(gameState, depth, agentIndex) == True:
            return self.evaluationFunction(gameState)
        elif agentIndex >= 1:  #if it is a ghost
            return self.minValue(gameState, depth, agentIndex, a, b)[0]
        elif agentIndex == 0: #if it is pacman
            return self.maxValue(gameState, depth, agentIndex, a, b)[0]
    

    def minValue(self, gameState, depth, agentIndex, a, b):
        v = float("inf")
        actions = gameState.getLegalActions(agentIndex)
        numAgents = gameState.getNumAgents()
        currentAgentIndex = (depth + 1) % numAgents
        for action in actions:
            ab = self.abFunction(gameState.generateSuccessor(agentIndex,action), depth+1, currentAgentIndex, a, b)
             #find min(v,ab)
            if ab == v:
                bestAction = action
            elif ab < v:
                v = ab
                bestAction = action
            # prunning
            if v < a:
                return v, bestAction
            b= min(b, v)

        return v, bestAction


    def maxValue(self, gameState, depth, agentIndex, a, b):
        v = -float("inf")
        actions = gameState.getLegalActions(agentIndex)
        numAgents = gameState.getNumAgents()
        currentAgentIndex = (depth + 1) % numAgents
        for action in actions:
            ab = self.abFunction(gameState.generateSuccessor(agentIndex,action), depth+1, currentAgentIndex, a, b)
            #find max(v,ab)
            if ab == v:
                bestAction = action
            elif ab > v:
                v = ab
                bestAction = action
            # prunning
            if v > b:
                return v, bestAction
            a =  max(a, v)
            
        return v, bestAction


class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState: GameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction

        All ghosts should be modeled as choosing uniformly at random from their
        legal moves.
        """
        "*** YOUR CODE HERE ***"

        action = self.maxValue(gameState,0,0)[1]
        return action


    def expectiMaxFunction(self, gameState, depth, agentIndex):
        if self.terminalTest(gameState, depth, agentIndex) == True:
            return self.evaluationFunction(gameState)
        elif agentIndex == 0:  #if it is pacman
            return self.maxValue(gameState, depth, agentIndex)[0]
        else: #if it is ghost
            return self.expectiValue(gameState, depth, agentIndex)



    def terminalTest(self, gameState, depth, agentIndex):          #returns True if this is terminal state  //  returns False if not
        if gameState.getLegalActions(agentIndex)==0:
            return True
        elif gameState.isLose():
            return True
        elif gameState.isWin():
            return True
        elif depth ==  self.depth * gameState.getNumAgents():
            return True

        return False


    def maxValue(self, gameState, depth, agentIndex):
        v = -float("inf")
        numAgents = gameState.getNumAgents()
        actions = gameState.getLegalActions(agentIndex)
        for action in actions:
            currentAgentIndex = (depth + 1) % numAgents
            expecti = self.expectiMaxFunction(gameState.generateSuccessor(agentIndex,action), depth+1, currentAgentIndex)
            
            if expecti == v:
                bestAction = action
            elif expecti > v:
                v = expecti
                bestAction = action
            
        return v, bestAction

    def expectiValue(self, gameState, depth, agentIndex):
        numOfactions = 0
        sumOfExpecti = 0
        actions = gameState.getLegalActions(agentIndex)
        numAgents = gameState.getNumAgents()
        currentAgentIndex = (depth + 1) % numAgents
        for action in actions:
            numOfactions += 1
            expecti = self.expectiMaxFunction(gameState.generateSuccessor(agentIndex,action), depth+1, currentAgentIndex)
            sumOfExpecti += expecti
        #find average of node's children value
        average = sumOfExpecti / numOfactions    #this is our chance node expected value
        return average



def betterEvaluationFunction(currentGameState: GameState):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION: <write something here so we know what you did>
    something :/
    """
    "*** YOUR CODE HERE ***"
    newPacmanPos = currentGameState.getPacmanPosition()
    score = currentGameState.getScore()

    #initializing distance from food and ghost
    foodLimit = float("+inf")
    ghostLimit = float("+inf")

    #min distance from food
    newFood = currentGameState.getFood().asList()
    for food in newFood:
        foodDistance = manhattanDistance(newPacmanPos, food)
        foodLimit = min(foodLimit, foodDistance)
    #if pacman is near its food, we add 1/its_min_distance_from_the_food
    score += 1 / foodLimit

    #min distance from a ghost
    newGhostPos = currentGameState.getGhostPositions()
    for ghost in newGhostPos:
        ghostDistance = manhattanDistance(newPacmanPos, ghost)
        ghostLimit = min (ghostLimit, ghostDistance)
    #if this distance is smaller than 1, we need to send pacman far away. we show this by decreasing the score by 100 as a signal!
    if ghostLimit < 1:
        score -= 200
    #how many capsules, left
    numOfCapsules=0
    newCapsules = currentGameState.getCapsules()
    for capsule in newCapsules:
        numOfCapsules +=1
    score -= numOfCapsules * 10 # for every sigle capsule that you didn't eat, you have a penalty

    if currentGameState.isWin() == True:
        score += 10000
    elif currentGameState.isLose() == True:
        score += -10000
   
    return score
# Abbreviation
better = betterEvaluationFunction
