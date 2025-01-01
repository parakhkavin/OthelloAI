# Author: Kavin Parakh, kkp56
# Date: 02/19/2024
# Purpose: This program implements the kkp56 AI agent for playing the Othello board game.
#          It features a class that enables the agent to make strategic moves within a specified time constraint, using iterative deepening and alpha-beta pruning techniques.
#          The focus is on maximizing the search depth within the given time limit to enhance the agent's performance in competitive scenarios.

import time
import game
import othello


## kkp56 AI Agent
# Inherits from the game.Player class to provide an AI agent that uses a time-constrained search algorithm.
class kkp56(game.Player):
    
    ## The constructor for kkp56 class.
    # @param color Color of the agent ('O' for black, 'X' for white).
    # @param time_limit_ms Time limit for the agent to make a move, in milliseconds.
    def __init__(self, color, time_limit_ms):
        self.color = color
        self.time_limit_ms = time_limit_ms
        
    ## Evaluate the current board state.
    # @param state The current state of the Othello board.
    # @return The score of the board as evaluated by the state's scoring function.
    def evaluate_board(self, state):
        return state.score()
    
    
    ## Recursive function to perform a depth-limited search with alpha-beta pruning within a time limit.
    # @param state The current state of the Othello board.
    # @param depth Current depth level of the search.
    # @param alpha Alpha value for alpha-beta pruning.
    # @param beta Beta value for alpha-beta pruning.
    # @param maximizing_player Boolean to indicate if the current search is maximizing or minimizing.
    # @param start_time The start time of the search to calculate elapsed time.
    # @return A tuple of the best score found and the associated move, or (None, None) if time limit is exceeded.
    def search_with_time_limit(self, state, depth, alpha, beta, maximizing_player, start_time):
        if time.time() * 1000 - start_time >= self.time_limit_ms:
            return None, None
        if depth == 0 or state.game_over():
            return self.evaluate_board(state), None

        if maximizing_player:
            value = float('-inf')
            best_move = None
            for move in state.generateMoves():
                new_state = state.applyMoveCloning(move)
                child_value, _ = self.search_with_time_limit(new_state, depth - 1, alpha, beta, False, start_time)
                if child_value is not None and child_value > value:
                    value = child_value
                    best_move = move
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
            return value, best_move
        else:
            value = float('inf')
            best_move = None
            for move in state.generateMoves():
                new_state = state.applyMoveCloning(move)
                child_value, _ = self.search_with_time_limit(new_state, depth - 1, alpha, beta, True, start_time)
                if child_value is not None and child_value < value:
                    value = child_value
                    best_move = move
                beta = min(beta, value)
                if beta <= alpha:
                    break
            return value, best_move
    
    
    ## Choose the best move for the current player given the state of the game.
    # @param state The current state of the Othello board.
    # @return The best move determined by the search algorithm within the time limit.
    def choose_move(self, state):
        best_move = None
        depth = 1
        best_value = float('-inf') if self.color == 'O' else float('inf')
        start_time = time.time() * 1000

        while time.time() * 1000 - start_time < self.time_limit_ms:
            value, move = self.search_with_time_limit(state, depth, float('-inf'), float('inf'), True, start_time)
            if move is None:
                break
            best_move = move
            best_value = value
            depth += 1
        
        return best_move
