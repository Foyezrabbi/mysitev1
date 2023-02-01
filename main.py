from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")


@app.route("/about")
def abouts():
    return render_template("about.html")


@app.route("/content")
def content():
    return render_template("content.html")


@app.route("/chatot")
def chatot():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
