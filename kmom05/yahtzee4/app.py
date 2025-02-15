#!/usr/bin/env python3
"""
Yahtzee app
"""
# Importera relevanta moduler
import re
import os
import traceback
from flask import Flask, render_template, session, url_for, redirect, request
from src.hand import Hand
from src.scoreboard import Scoreboard

app = Flask(__name__)
app.secret_key = re.sub(r"[^a-z\d]", "", os.path.realpath(__file__))

@app.route("/")
def main():
    """ Main route """

    if (
            "hand" not in session
            and "sb" not in session
            and "rolls" not in session
            and "error_msg" not in session
        ):
        set_session(Hand(), Scoreboard(), 0, False)
    hand, scoreboard, rolls, error_msg = get_session()

    return render_template(
            "index.html",
            hand = hand,
            scoreboard = scoreboard,
            rolls = rolls,
            error_msg = error_msg
    )

def get_session():
    """ Get the session """
    return (Hand(session["hand"]),
            Scoreboard.from_dict(session["sb"]),
            session["rolls"],
            session["error_msg"] if "error_msg" in session else False
    )

def set_session(hand, scoreboard, rolls, error_msg):
    """ Set values in session, use None as arg to ignore setting a value """
    if hand is not None:
        session["hand"] = hand.to_list()
    if scoreboard is not None:
        session["sb"] = scoreboard.points
    if rolls is not None:
        session["rolls"] = rolls
    if error_msg is not None:
        session["error_msg"] = error_msg

@app.route("/about")
def about():
    """ About route """
    return render_template("about.html")

@app.route("/roll", methods=["POST"])
def roll():
    """ Roll selected dice. """
    hand, _, rolls, _ = get_session()

    # limit to 2 rerolls
    if rolls <= 1:
        selected = request.form.getlist("die")
        reroll_list = []
        for die in selected:
            reroll_list.append(int(die))
        # full reroll when pressing roll with nothing selected
        hand.roll([0, 1, 2, 3, 4] if not reroll_list else reroll_list)
        set_session(hand, None, rolls + 1, False)

    return redirect(url_for('main'))

@app.route("/score", methods=["POST"])
def score():
    """ Handle picking a rule and scoring """
    selected_rule = request.form.get('score_choice')
    hand, scoreboard, _, _ = get_session()
    try:
        scoreboard.add_points(selected_rule, hand)
        # refresh hand, roll, store score, get rid of errors
        set_session(Hand(), scoreboard, 0, False)

    except ValueError:
        session["error_msg"] = "Rule already used!"
    except KeyError:
        session["error_msg"] = "Select a rule!"

    return redirect(url_for("main"))

@app.route("/reset")
def reset():
    """ Reset session """
    _ = [session.pop(key) for key in list(session.keys())]

    return redirect(url_for('main'))

@app.errorhandler(404)
def page_not_found(e):
    """
    Handler for page not found 404
    """
    #pylint: disable=unused-argument
    return "Flask 404 here, but not the page you requested."

@app.errorhandler(500)
def internal_server_error(e):
    """
    Handler for internal server error 500
    """
    #pylint: disable=unused-argument
    return "<p>Flask 500<pre>" + traceback.format_exc()

if __name__ == "__main__":
    app.run()
