from flask import render_template, request, jsonify, Blueprint
from iGirls.models import Player
from iGirls import db
from iGirls.vote.utils import get_players

report_blueprint = Blueprint('report', __name__)

@report_blueprint.route("/report", methods=["POST"])
def report():
    player = request.form["report"]
    player = Player.query.filter_by(username=player).first()
    if player.reports == None and player.reports != int:
        player.reports = 1
    else:
        player.reports = player.reports + 1

    db.session.commit()
    
    _players = get_players()
    player1 = _players[0]
    player2 = _players[1]
    return jsonify('', render_template("update.html", player1=player1, player2=player2))
