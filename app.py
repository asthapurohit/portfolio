from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/thoughts")
def thoughts():
    return render_template("thoughts.html")

if __name__ == "__main__":
    app.run(debug=True)