from flask import Flask
from nba_api.live.nba.endpoints import scoreboard

app = Flask(__name__)


@app.route("/scoreboard")
def test():
    # Today's Score Board
    games = scoreboard.ScoreBoard()

    # json
    return games.get_json()
