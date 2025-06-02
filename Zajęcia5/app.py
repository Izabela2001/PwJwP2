from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/profile")
def profile():
    return render_template("profile.html", username="Domyślny Profil")


@app.route("/user/<username>")
def user_profile(username):
    return render_template("user.html", username=username.capitalize())


if __name__ == "__main__":
    app.run(debug=True)
