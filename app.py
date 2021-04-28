from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from cs50 import SQL

#from helpers import login_required

from src.fight import Fight

app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure SQLite database
db = SQL("sqlite:///main_db.db")

from src.helpers import *

@app.route("/")
@login_required
def index():
    fight_instance = Fight()

    fight_instance.addRandomCharacter()

    return render_template("home.html", party_list=fight_instance.party.members)


if __name__ == "__main__":
  app.run()