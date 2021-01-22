from flask import render_template, Blueprint
from iGirls.models import Player
import random

play_blueprint = Blueprint('play', __name__)

@play_blueprint.route('/play')
def play():
    players = Player.query.all()
    player1 = random.choice(players)
    player2 = random.choice(players)

    while player1 == player2:
        player2 = random.choice(players)

    return render_template('index.html', player1=player1, player2=player2)
