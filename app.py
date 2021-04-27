from flask import Flask

from src.fight import Fight


app = Flask(__name__)

@app.route("/")
def hello():
    fight_instance = Fight()

    return str(fight_instance.player.abilities)

if __name__ == "__main__":
  app.run()