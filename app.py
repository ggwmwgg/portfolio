import os
from flask import Flask, flash, redirect, render_template, request
from flask_session import Session
import requests
import datetime
import sqlite3


# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


# Apply "export tokentg=XXXXXXXXXX:YYYYYYYYYYYYYYYYYYYYYYYYY" before start
if not os.environ.get("tokentg"):
    raise RuntimeError("tokentg not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


def insend(lang, name, email, subject, message, date):

    # Database connection and execution
    conn = sqlite3.connect('ggwm.db')
    c = conn.cursor()
    ex = f"INSERT INTO news (name, email, subject, message, date) VALUES(?, ?, ?, ?, ?)"
    c.execute(ex,(name, email, subject, message, date))

    # Commit changes to sqlite3 and close connection
    conn.commit()
    conn.close()

    # Telegram Message to the channel
    token = os.environ.get("tokentg")
    if lang == "en":
        msg = f"<u><b><i>You've got a new message</i></b></u>%0A%0A<b>From:</b> {name} %0A<b>Email:</b> {email} %0A<b>Subject is:</b> {subject} %0A<b>Message:</b> {message}"
    else:
        msg = f"<u><b><i>У тебя новое сообщение!</i></b></u>%0A%0A<b>От:</b> {name} %0A<b>Почта:</b> {email} %0A<b>Тема:</b> {subject} %0A<b>Сообщение:</b> {message}"
    kok = f"https://api.telegram.org/bot{token}/sendMessage?chat_id=@yumplay&parse_mode=HTML&text={msg}"
    requests.get(kok)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about",)
def about():
    return render_template("about.html")


@app.route("/port",)
def port():
    return render_template("portfolio.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":

        lang = "en"
        name = request.form.get("name")
        email = request.form.get("email")
        subject = request.form.get("subject")
        message = request.form.get("message")
        date = datetime.datetime.now()

        # Inserting in database and sending the message to @yumplay Telegram Channel
        insend(lang, name, email, subject, message, date)
        flash("Successfully sent!")
        return redirect("/contact")

    else:

        # TODO: Display the entries in the database on index.html
        return render_template("c.html")


@app.route("/hello")
def hello():

    # Database connection
    conn = sqlite3.connect('ggwm.db')
    c = conn.cursor()
    query = c.execute("SELECT * FROM news")
    # Creating a dict
    colname = [d[0] for d in query.description]
    messages = [dict(zip(colname, r)) for r in query.fetchall()]
    conn.close()

    return render_template("kek.html", messages=messages)

@app.route("/ru")
def indexru():
    return render_template("indexru.html")

@app.route("/ru/about",)
def aboutru():
    return render_template("aboutru.html")


@app.route("/ru/port",)
def portru():
    return render_template("portfolioru.html")

@app.route("/ru/contact", methods=["GET", "POST"])
def contactru():
    if request.method == "POST":

        lang = "ru"
        name = request.form.get("name")
        email = request.form.get("email")
        subject = request.form.get("subject")
        message = request.form.get("message")
        date = datetime.datetime.now()

        # Inserting in database and sending the message to @yumplay Telegram Channel
        insend(lang, name, email, subject, message, date)

        flash("Успешно отправлено!")
        return redirect("/ru/contact")

    else:

        # TODO: Display the entries in the database on index.html
        return render_template("cru.html")

