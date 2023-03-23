from flask import Flask, render_template
import backend.util

app = Flask(__name__)

# Connect to the database

con = backend.util.Connector([
    'backend\data-store\messages-1-with-sentiment.csv',
    'backend\data-store\messages-2-with-sentiment.csv'
])


@app.route("/")
def dashboard():
    return render_template("dashboard.html")


@app.route("/moderate")
def moderate():
    # get the data - a specific message
    # data - engagment =?
    # pick the next message somehow 

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
