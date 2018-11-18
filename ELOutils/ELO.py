import random
import math

class Player(object):
    def __init__(self, name, rating):
        self.rating = rating
        self.name = name
        self.verification = random.randint(0,10000)

    # used for locating players
    def __eq__(self,other):
        return other.name == self.name and other.rating == self.rating and other.verification == self.verification
    
    # used for comparisons/orderings
    def __lt__(self,other):
        if not self.rating == other.rating:
            return self.rating < other.rating
        elif not self.name == other.name:
            return self.name < other.name
        else:
            return self.verification < other.verification

    def __gt__(self,other):
        if not self.rating == other.rating:
            return self.rating > other.rating
        elif not self.name == other.name:
            return self.name > other.name
        else:
            return self.verification > other.verification

    def __le__(self,other):
        if self == other:
            return True
        elif not self.rating == other.rating:
            return self.rating < other.rating
        elif not self.name == other.name:
            return self.name < other.name
        else:
            return self.verification < other.verification

    def __ge__(self,other):
        if self == other:
            return True
        elif not self.rating == other.rating:
            return self.rating > other.rating
        elif not self.name == other.name:
            return self.name > other.name
        else:
            return self.verification > other.verification

    def __str__(self):
        return 'Player({0},{1})'.format(self.name,self.rating)
    
    def __repr__(self):
        return str(self)

def get_exp_score(rating_a, rating_b,max_diference=1.0):
    return max_diference * (1.0 /(1 + 10**((rating_b - rating_a)/400.0)))

def rating_adj(rating, exp_score, score, k=32):
    return rating + k * (score - exp_score)

def match_result(player, challenger, result, floor = None):
        exp_score_a = get_exp_score(player.rating, challenger.rating)

        if result > 0:
            player.rating = math.floor(rating_adj(player.rating, exp_score_a, 1))
            challenger.rating = math.floor(rating_adj(challenger.rating, 1 - exp_score_a, 0))
        elif result < 0:
            player.rating = math.floor(rating_adj(player.rating, exp_score_a, 0))
            challenger.rating = math.floor(rating_adj(challenger.rating, 1 - exp_score_a, 1))
        else:
            player.rating = math.floor(rating_adj(player.rating, exp_score_a, 0.5))
            challenger.rating = math.floor(rating_adj(challenger.rating, 1 - exp_score_a, 0.5))

        if floor:
            if player.rating < floor:
                player.rating = floor
            if challenger.rating < floor:
                challenger.rating = floor

def create_match(players, player, win_ratio= 1, fairness= 0.5, margin= 0.01, max_diference= 1):
    if not players or not player:
        raise ValueError("There must be a list of players and a player to have as reference")

    # Garantee that the list is sorted
    players.sort()

    # Helper variables
    index = players.index(player)
    weaker = True if win_ratio < 0.5 else False
    rival = index-1 if weaker else index+1
    change_rate = -1 if weaker else 1

    # limits of fairness
    lower_bound = (fairness-margin) * max_diference
    higher_bound = (fairness+margin) * max_diference

    # search for a rival
    while lower_bound <= get_exp_score(player.rating, players[rival].rating) <= higher_bound:
        rival += change_rate
        if not -1 < rival < len(players):
            break
    
    # Fixing in case of small list or quirks of search
    if not -1 < rival < len(players) or not lower_bound < get_exp_score(player.rating, players[rival].rating) < higher_bound:
        rival -= change_rate
    if rival == index:
        rival += change_rate
    
    return players[rival]