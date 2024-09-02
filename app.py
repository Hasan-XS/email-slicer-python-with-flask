from sqlalchemy.exc import IntegrityError
from flask import Flask, render_template, request, redirect, url_for
from config import SQLALCHEMY_DATABASE_URI
from extention import *
from model.email import Email
from flask_migrate import Migrate

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
migrate = Migrate(app, db)
db.init_app(app)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        email = request.form.get("email", None)
        
        username = email[:email.index('@')]
        domain = email[email.index('@') + 1:]

        email_user = Email(username=username, domain=domain, email=email)

        try:
            db.session.add(email_user)
            db.session.commit()
        except IntegrityError:
            return "Not Uniq"

        return redirect(url_for("home"))
    else:
        email = Email.query.all()
        return render_template("index.html", email=email)


@app.route("/remove-email")
def remove_email():
    id = request.args.get('id-rem')
    email_user = Email.query.filter(Email.id == id).first_or_404()

    db.session.delete(email_user)
    db.session.commit()
    return redirect(url_for('home'))
    


with app.app_context():
    db.create_all()
if __name__ == "__main__":
    app.run(debug=True)