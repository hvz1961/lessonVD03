from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_date = now.strftime("%Y-%m-%d")
    return render_template('index.html',
                           time=current_time, date=current_date)

if __name__ == "__main__":
    app.run(debug=True)
