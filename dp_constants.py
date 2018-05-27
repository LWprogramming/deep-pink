# constants for engines, evaluation etc.
import random

CHECKMATE_SCORE = 1e6 # in negamax
max_depth = random.randint(1, 2)  # max depth for deep pink
secs = random.random()  # max seconds for sunfish
num_games = 5 # number of games to simulate when we run play.py