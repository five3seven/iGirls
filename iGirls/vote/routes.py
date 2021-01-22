from flask import render_template, request, jsonify, Blueprint
from iGirls.models import Player
from iGirls import db
from iGirls.vote.utils import Elo, get_players
import random

vote_blueprint = Blueprint('vote', __name__)

@vote_blueprint.route('/vote', methods=["POST"])
def vote():
    try:
        player1 = request.form["player1"]
        player2 = request.form["player2"]
        winner = request.form["winner"]

        player1 = Player.query.filter_by(username=player1).first()
        player2 = Player.query.filter_by(username=player2).first()
        e = Elo()

        e.addPlayer(player1.username, rating=player1.score)
        e.addPlayer(player2.username, rating=player2.score)
            
        if winner == '1':
            e.recordMatch(player1.username, player2.username, winner=player1.username)
        elif winner == '2':
            e.recordMatch(player1.username, player2.username, winner=player2.username)


        player1_score = e.getPlayerRating(player1.username)
        player2_score = e.getPlayerRating(player2.username)
        
        if player1_score < 0:
            player1_score = 0
        elif player2_score < 0:
            player2_score = 0

        player1.score = player1_score
        player2.score = player2_score
        
        db.session.commit()
    except:
        pass

    _players = get_players()
    try:
        while player1.username == _players[0].username and player2.username == _players[1].username:
            _players = get_players()
    except:
        pass
    
    player1 = _players[0]
    player2 = _players[1]
    return jsonify('', render_template("update.html", player1=player1, player2=player2))
    