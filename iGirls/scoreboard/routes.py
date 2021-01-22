from flask import render_template, request, jsonify, Blueprint
from iGirls.models import Player

scoreboard_blueprint = Blueprint('scoreboard', __name__)

@scoreboard_blueprint.route('/scoreboard', methods=["GET", "POST"])
def scoreboard():
    players = Player.query.order_by("score")[:-11:-1]
    if request.method == "POST":
        return jsonify('', render_template("update_scoreboard.html", rows=players))
    return render_template("scoreboard.html", rows=players)
    