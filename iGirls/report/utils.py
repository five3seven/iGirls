from iGirls.models import Player
import random

def get_players():
    players = Player.query.all()
    _player1 = random.choice(players)
    _player2 = random.choice(players)

    while _player1 == _player2:
        _player2 = random.choice(players)
    return [_player1, _player2]