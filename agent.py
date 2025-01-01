# Author: Kavin Parakh, kkp56
# Date: 02/19/2024
# Purpose: This program implements various AI agents for playing the Othello game. It includes the HumanPlayer class,
#          which allows a human to play the game by choosing moves interactively. The RandomAgent class represents an
#          AI that selects moves randomly. The MinimaxAgent class uses the Minimax algorithm to choose moves based
#          on a depth-first search strategy, and the AlphaBeta class improves upon this with Alpha-Beta pruning to
#          reduce the search space.

import math
import random
import game


## HumanPlayer class
#  Inherits from game.Player and represents a human player in the Othello game.
class HumanPlayer(game.Player):
    
    ## The constructor for the HumanPlayer class.
    #  @param color The color ('O' or 'X') representing the player.
    def __init__(self, color):
        self.color = color
        
    ## Method to allow a human player to choose a move.
    #  @param state The current state of the Othello game.
    #  @return The chosen move as an integer index.
    def choose_move(self, state):
        moves = state.generateMoves()
        for i, action in enumerate(moves):
            print(f'{i}: {action}')
        response = input('Please choose a move: ')
        return moves[int(response)]

## RandomAgent class
#  Inherits from game.Player and represents an AI player that chooses random moves.
class RandomAgent(game.Player):
    
    ## The constructor for the RandomAgent class.
    #  @param color The color ('O' or 'X') representing the AI player.
    def __init__(self, color):
        self.color = color
    
    ## Method to choose a move randomly.
    #  @param state The current state of the Othello game.
    #  @return A random move from the list of available moves.
    def choose_move(self, state):
        available_moves = state.generateMoves()
        if not available_moves:
            return None
        return random.choice(available_moves)

## MinimaxAgent class
#  Inherits from game.Player and represents an AI player that uses the Minimax algorithm.
class MinimaxAgent(game.Player):
    
    ## The constructor for the MinimaxAgent class.
    #  @param depth The maximum depth to search in the game tree.
    #  @param color The color ('O' or 'X') representing the AI player.
    def __init__(self, depth, color):
        self.color = color
        self.depth = depth

    ## Method to evaluate the current board state.
    #  @param state The current state of the Othello game.
    #  @return The score of the board state from the perspective of the AI player's color.
    def evaluate_board(self, state):
        score = state.score()
        return score if self.color == 'O' else -score
    
    ## Minimax search algorithm.
    #  @param state The current state of the Othello game.
    #  @param depth The current depth in the search tree.
    #  @param maximizing_player A boolean indicating if the current player is maximizing or minimizing.
    #  @return The best score found for the current move and depth.
    def minimax(self, state, depth, maximizing_player):
        if depth == 0 or state.game_over():
            return self.evaluate_board(state)

        if maximizing_player:
            max_eval = float('-inf')
            for move in state.generateMoves():
                new_state = state.applyMoveCloning(move)
                evaluation = self.minimax(new_state, depth - 1, False)
                max_eval = max(max_eval, evaluation)
            return max_eval
        else:
            min_eval = float('inf')
            for move in state.generateMoves():
                new_state = state.applyMoveCloning(move)
                evaluation = self.minimax(new_state, depth - 1, True)
                min_eval = min(min_eval, evaluation)
            return min_eval
    
    ## Method to choose the best move based on the Minimax algorithm.
    #  @param state The current state of the Othello game.
    #  @return The best move found by the Minimax algorithm.
    def choose_move(self, state):
        best_move = None
        best_value = float('-inf')
        for move in state.generateMoves():
            new_state = state.applyMoveCloning(move)
            move_evaluation = self.minimax(new_state, self.depth, False)
            if move_evaluation > best_value:
                best_value = move_evaluation
                best_move = move
        return best_move

## AlphaBeta class
#  Inherits from game.Player and represents an AI player that uses the Alpha-Beta pruning algorithm.
class AlphaBeta(game.Player):
    
    ## The constructor for the AlphaBeta class.
    #  @param color The color ('O' or 'X') representing the AI player.
    #  @param depth The maximum depth to search in the game tree.
    def __init__(self, color, depth):
        self.color = color
        self.depth = depth
        
    ## Method to evaluate the current board state.
    #  @param state The current state of the Othello game.
    #  @return The score of the board state from the perspective of the AI player's color.
    def evaluate_board(self, state):
        score = state.score()
        return score if self.color == 'O' else -score

    ## Alpha-Beta pruning search algorithm.
    #  @param state The current state of the Othello game.
    #  @param depth The current depth in the search tree.
    #  @param alpha The alpha value for pruning.
    #  @param beta The beta value for pruning.
    #  @param maximizing_player A boolean indicating if the current player is maximizing or minimizing.
    #  @return The best value found using Alpha-Beta pruning and the corresponding move.
    def alpha_beta_search(self, state, depth, alpha, beta, maximizing_player):
        if depth == 0 or state.game_over():
            return self.evaluate_board(state)

        if maximizing_player:
            value = float('-inf')
            for move in state.generateMoves():
                new_state = state.applyMoveCloning(move)
                value = max(value, self.alpha_beta_search(new_state, depth - 1, alpha, beta, False))
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
            return value
        else:
            value = float('inf')
            for move in state.generateMoves():
                new_state = state.applyMoveCloning(move)
                value = min(value, self.alpha_beta_search(new_state, depth - 1, alpha, beta, True))
                beta = min(beta, value)
                if beta <= alpha:
                    break
            return value
        
    ## Method to choose the best move based on the Alpha-Beta pruning algorithm.
    #  @param state The current state of the Othello game.
    #  @return The best move found by the Alpha-Beta pruning algorithm.
    def choose_move(self, state):
        best_move = None
        best_value = float('-inf')
        alpha = float('-inf')
        beta = float('inf')
        for move in state.generateMoves():
            new_state = state.applyMoveCloning(move)
            move_value = self.alpha_beta_search(new_state, self.depth, alpha, beta, True)
            if move_value > best_value:
                best_value = move_value
                best_move = move
        return best_move
