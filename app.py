from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main():
    return render_template ("main.html")

@app.route("/gallery")
def gallery():
    links = open("linknotes.txt", "r")
    return render_template ("gallery.html", "linknotes.txt")

@app.route("/add")
def add():
    return render_template("add.html")

@app.route("/linknotes", methods = ["POST"])
def linknotes():
    links = open("linknotes.txt", "r")
    linknotes.write(str(links))
    # или просто r хватит?
    return render_template("linknotes.txt")