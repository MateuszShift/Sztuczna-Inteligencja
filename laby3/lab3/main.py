import copy, sys
from exceptions import AgentException

class MinMaxAgent:
    def __init__(self, my_token, depth=4,heuristic_func=None):
        self.my_token = my_token
        self.depth = depth
        self.heuristic_func = heuristic_func
 
    def decide(self, connect4):
        if connect4.who_moves != self.my_token:
            raise AgentException("not my round")
        moves = connect4.possible_drops()
        best_move, best_score = self.minmax(connect4, self.depth, True)
        if best_move not in moves:
            best_move = moves[0]
        return best_move
 
    def minmax(self, connect4, depth, maximizing):
        if depth == 0 or connect4.game_over:
            return None, self.heuristic_func(connect4, self.my_token)

        if maximizing:
            best_score = -sys.maxsize 
            best_move = None
            for move in connect4.possible_drops():
                connect4_copy = copy.deepcopy(connect4) 
                connect4_copy.drop_token(move)
                _, score = self.minmax(connect4_copy, depth - 1, False)
                if score > best_score:
                    best_score = score
                    best_move = move
            return best_move, best_score

        else:  
            best_score = sys.maxsize 
            best_move = None
            for move in connect4.possible_drops():
                connect4_copy = copy.deepcopy(connect4)
                connect4_copy.drop_token(move)
                _, score = self.minmax(connect4_copy, depth - 1, True)
                if score < best_score:
                    best_score = score
                    best_move = move
            return best_move, best_score
        
        
    def basic_static_eval(connect4, player):
        if connect4.wins == player:
            return sys.maxsize
        if connect4.wins == 'x' if player == 'o' else 'o':
            return -sys.maxsize
        opponent = 'o' if player == 'x' else 'x' 
        score = 0
        score_enemy = 0
        for fours in connect4.iter_fours():
            if fours.count(player) == 3:
                score += 100
            elif fours.count(opponent) == 3:
                score_enemy += 100 
        return score - score_enemy
    
    
    
    



    def advanced_static_eval(connect4, player):
            score = 0
            for fours in connect4.iter_fours(): #sprawdzanie rzedow
                consecutive_count = 0
                empty_slots = 0
                for cell in fours:
                    if cell == player: #sprawdzanie czy znak jest taki sam jak gracz
                        consecutive_count += 1 #zliczanie ilosci znakow w rzedzie
                    elif cell == '_':
                        empty_slots += 1
                    else:
                        consecutive_count = 0
                        empty_slots = 0

                #dodawanie punktów w zależności od ilości znaków w rzedzie
                if consecutive_count == 4: 
                    return sys.maxsize  
                elif consecutive_count == 3 and empty_slots == 1: 
                    score += 200  
                elif consecutive_count == 2 and empty_slots == 2:
                    score += 50 
            
            
            opponent = 'x' if player == 'o' else 'o' #przeciwnik
            #sprawdzanie rzedow przeciwnika
            for fours in connect4.iter_fours():
                consecutive_count = 0
                empty_slots = 0
                for cell in fours:
                    if cell == opponent:
                        consecutive_count += 1
                    elif cell == '_':
                        empty_slots += 1
                    else:
                        consecutive_count = 0
                        empty_slots = 0
                #odejmowanie punktów gracza w zależności od ilości znaków w rzedzie przeciwnika
                if consecutive_count == 4:
                    score -= sys.maxsize 
                elif consecutive_count == 3 and empty_slots == 1:
                    score -= 150 
                elif consecutive_count == 2 and empty_slots == 2:
                    score -= 25
            #dodawanie punktów w zależności od ilości pustych miejsc w środkowej kolumnie
            center_column = connect4.center_column()
            empty_slots = center_column.count('_')
            score -= empty_slots * 20  

            return score
            
            
        