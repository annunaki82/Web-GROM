from flask import Flask, render_template

app = Flask(__name__)

# Úvodní stránka
@app.route("/")
def home():
    return render_template("index.html")

# Stránka Koně
@app.route("/kone")
def kone():
    return render_template("kone.html")

# Stránka Kontakt
@app.route("/kontakt")
def kontakt():
    return render_template("kontakt.html")

if __name__ == "__main__":
    app.run(debug=True)
