from exceptions import GameplayException
from connect4 import Connect4
from randomagent import RandomAgent
from main import MinMaxAgent
from alphabetaagent import AlphaBetaAgent

test = 6
if test == 1:
    connect4 = Connect4(width=7, height=6)
    agent1 = MinMaxAgent('o',heuristic_func=MinMaxAgent.basic_static_eval)
    agent2 = RandomAgent('x')
    while not connect4.game_over:
        connect4.draw()
        try:
            if connect4.who_moves == agent1.my_token:
                n_column = agent1.decide(connect4)
            else:
                n_column = agent2.decide(connect4)
            connect4.drop_token(n_column)
        except (ValueError, GameplayException):
            print('invalid movehdushaudh')
        
    connect4.draw()

if test == 2:
    connect4 = Connect4(width=7, height=6)
    agent1 = MinMaxAgent('x',4,heuristic_func=MinMaxAgent.basic_static_eval)
    agent2 = RandomAgent('o')
    while not connect4.game_over:
        connect4.draw()
        try:
            if connect4.who_moves == agent1.my_token:
                n_column = agent1.decide(connect4)
            else:
                n_column = agent2.decide(connect4)
            connect4.drop_token(n_column)
        except (ValueError, GameplayException):
            print('invalid move')
        
    connect4.draw()


if test == 3:
    connect4 = Connect4(width=7, height=6)
    agent1 = AlphaBetaAgent('o',4,heuristic_func=MinMaxAgent.basic_static_eval)
    agent2 = RandomAgent('x')
    while not connect4.game_over:
        connect4.draw()
        try:
            if connect4.who_moves == agent1.my_token:
                n_column = agent1.decide(connect4)
            else:
                n_column = agent2.decide(connect4)
            connect4.drop_token(n_column)
        except (ValueError, GameplayException):
            print('invalid move')
        
    connect4.draw()
    
if test == 4:
    connect4 = Connect4(width=7, height=6)
    agent1 = AlphaBetaAgent('x',4,heuristic_func=MinMaxAgent.basic_static_eval)
    agent2 = RandomAgent('o')
    while not connect4.game_over:
        connect4.draw()
        try:
            if connect4.who_moves == agent1.my_token:
                n_column = agent1.decide(connect4)
            else:
                n_column = agent2.decide(connect4)
            connect4.drop_token(n_column)
        except (ValueError, GameplayException):
            print('invalid move')
        
    connect4.draw()

if test == 5:
    connect4 = Connect4(width=7, height=6)
    agent1 = AlphaBetaAgent('x',4,heuristic_func=MinMaxAgent.basic_static_eval)
    agent2 = AlphaBetaAgent('o',4,heuristic_func=MinMaxAgent.advanced_static_eval)
    while not connect4.game_over:
        connect4.draw()
        try:
            if connect4.who_moves == agent1.my_token:
                n_column = agent1.decide(connect4)
            else:
                n_column = agent2.decide(connect4)
            connect4.drop_token(n_column)
        except (ValueError, GameplayException):
            print('invalid move')
        
    connect4.draw()
if test == 6:
    connect4 = Connect4(width=7, height=6)
    agent1 = AlphaBetaAgent('o',4,heuristic_func=MinMaxAgent.basic_static_eval)
    agent2 = AlphaBetaAgent('x',4,heuristic_func=MinMaxAgent.advanced_static_eval)
    while not connect4.game_over:
        connect4.draw()
        try:
            if connect4.who_moves == agent1.my_token:
                n_column = agent1.decide(connect4)
            else:
                n_column = agent2.decide(connect4)
            connect4.drop_token(n_column)
        except (ValueError, GameplayException):
            print('invalid move')
        
    connect4.draw()