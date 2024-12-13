from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def first():
    return render_template("main.html")
@app.route("/second/")
def second():
    return render_template("cofelavka.html")
@app.route("/second/third/")
def third():
    return render_template("third_page.html")

if __name__ == "__main__":
    app.run()
