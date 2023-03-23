from flask import Flask, render_template
import backend.util

app = Flask(__name__)

# Connect to the database 

con = backend.util.Connector([
    'backend\data-store\messages-1-with-sentiment.csv',
    'backend\data-store\messages-2-with-sentiment.csv'
])

# Load the list of usernames 



@app.route("/moderate")
def moderate():
    # get the data - a specific message
    # data - engagment =?
    # pick the next message somehow 
    # message_id = 

    return render_template("index.html")

