import random
import math

def get_exp_score(rating_a, rating_b):
    return 1.0 /(1 + 10**((rating_b - rating_a)/400.0))

def rating_adj(rating, exp_score, score, k=32):
    return rating + k * (score - exp_score)

class Player(object):
    def __init__(self, name, rating):
        self.rating = rating
        self.name = name

    def match(self, other, result, floor = None):

        exp_score_a = get_exp_score(self.rating, other.rating)

        if result > 0:
            self.rating = math.floor(rating_adj(self.rating, exp_score_a, 1))
            other.rating = math.floor(rating_adj(other.rating, 1 - exp_score_a, 0))
        elif result < 0:
            self.rating = math.floor(rating_adj(self.rating, exp_score_a, 0))
            other.rating = math.floor(rating_adj(other.rating, 1 - exp_score_a, 1))
        else:
            self.rating = math.floor(rating_adj(self.rating, exp_score_a, 0.5))
            other.rating = math.floor(rating_adj(other.rating, 1 - exp_score_a, 0.5))

        if floor:
            if self.rating < floor.rating:
                self.rating = floor.rating
            if other.rating < floor.rating:
                other.rating = floor.rating

    def equals(self,other):
        return other.name == self.name

    def __str__(self):
        return self.name+','+str(self.rating)


def create_match(players,player_a_index = None,fairness = 0.5, margin = 0.01):
    player_b_index = 1
    player_c_index = 1
    return_both = False

    if not player_a_index:
        player_a_index = random.randint(0,len(players)-1)
        if player_a_index+1 >= len(players):
            player_a_index = len(players)-2
        if player_a_index-1 < 0:
            player_a_index = 1
        player_b_index = player_a_index + 1
        player_c_index = player_a_index - 1
        return_both = True
    else:
        print("yes player a ",player_a_index)
        if player_a_index == 0:
            player_b_index = player_a_index + 1
            player_c_index = player_a_index + 2
        elif player_a_index == len(players)-1:
            player_b_index = player_a_index - 1
            player_c_index = player_a_index - 2
        else:
            player_b_index = player_a_index + 1
            player_c_index = player_a_index - 1


    player_a = players[player_a_index]
    player_b = players[player_b_index]
    player_c = players[player_c_index]

    print("finding match for ",player_a)

    while player_b_index < len(players)  and not (fairness-margin) <= get_exp_score(player_a.rating,player_b.rating) <= (fairness+margin):
        player_b_index += 1
        if player_b_index == len(players):
            break
        player_b = players[player_b_index]

    while player_c_index > 0 and not (fairness-margin) <= get_exp_score(player_a.rating,player_c.rating) <= (fairness+margin):
        player_c_index -= 1
        if player_c_index < 0:
            break
        player_c = players[player_c_index]

    if player_b_index >= len(players):
        print("No fair match was found bellow ",player_a)
        player_b_index = random.randint(0,len(players)-1)
        while player_b_index == player_a_index:
            player_b_index = random.randint(0,len(players)-1)
        player_b = players[player_b_index]

    if player_c_index <0:
        print("No fair match was found above ",player_a)
        player_c_index = random.randint(0,len(players)-1)
        while player_c_index == player_a_index:
            player_c_index = random.randint(0,len(players)-1)
        player_c = players[player_c_index]

    distance_ab = abs(fairness - get_exp_score(player_a.rating,player_b.rating))
    distance_ac = abs(fairness - get_exp_score(player_a.rating,player_c.rating))

    print("Calculating fairest match for ",player_a)
    rival = player_b if (distance_ab < distance_ac) else player_c
    rival_index = player_b_index if (distance_ab < distance_ac) else player_c_index

    if return_both:
        return player_a,rival,player_a_index,rival_index
    else:
        return rival,rival_index
