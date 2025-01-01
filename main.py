import agent
import othello
import game
from kkp56 import kkp56
import sys

def create_player(arg, depth_or_time, player_color):
    if arg == 'human':
        return agent.HumanPlayer(player_color)
    elif arg == 'random':
        return agent.RandomAgent(player_color)
    elif arg == 'minimax':
        return agent.MinimaxAgent(depth_or_time, player_color)
    elif arg == 'alphabeta':
        return agent.AlphaBeta(player_color, depth_or_time)
    elif arg == 'extra':
        return kkp56(player_color, depth_or_time)
    else:
        return agent.RandomAgent(player_color)

def get_arg(index, default=None):
    '''Returns the command-line argument, or the default if not provided'''
    return sys.argv[index] if len(sys.argv) > index else default

if __name__ == '__main__':
    initial_state = othello.State()
    depth_or_time = int(get_arg(3, 3))

    player1 = create_player(get_arg(1), depth_or_time, 'O')
    player2 = create_player(get_arg(2), depth_or_time, 'X')

    game_instance = game.Game(initial_state, player1, player2)
    game_instance.play()
