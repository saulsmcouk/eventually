from flask import Flask, render_template

app = Flask(__name__)

# Connect to the database 
# Load the list of usernames 


@app.route("/moderate")
def moderate():
    # get the data - a specific message
    # data - engagment =?
    # pick the next message somehow 
    # message_id =

    



    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)