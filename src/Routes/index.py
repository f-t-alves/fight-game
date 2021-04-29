from src.Routes.helpers import *

from src.Fight.fight import Fight

@app.route("/")
@login_required
def index():
    fight_instance = Fight()

    fight_instance.addRandomCharacter()

    return render_template("home.html", party_list=fight_instance.party.members)