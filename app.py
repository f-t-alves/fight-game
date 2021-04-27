from flask import Flask

from src.fight import Fight


app = Flask(__name__)

@app.route("/")
def hello():
    fight_instance = Fight()

    fight_instance.addRandomCharacter()

    return str(fight_instance.party.members[0].abilities)

if __name__ == "__main__":
  app.run()