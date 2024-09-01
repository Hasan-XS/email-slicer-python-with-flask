from flask import Flask, render_template, request
from config import SQLALCHEMY_DATABASE_URI
from extention import *

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
db.init_app(app)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        email = request.form.get("email")
        print(email)
        return render_template("index.html", emails=email)
        
    else:
        return render_template("index.html")


with app.app_context():
    db.create_all()
if __name__ == "__main__":
    app.run(debug=True)