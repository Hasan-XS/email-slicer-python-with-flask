from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        email = request.form.get("email")
        print(email)
        return render_template("index.html", emails=email)
        
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)