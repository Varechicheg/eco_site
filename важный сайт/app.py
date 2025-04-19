from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    hour = datetime.now().hour
    bg_color = "#d8f5d3" if hour < 18 else "#2e5939"
    return render_template("index.html", bg_color=bg_color)

@app.route('/eco-test', methods=['POST'])
def eco_test():
    try:
        q1 = int(request.form.get('q1', 0))
        q2 = int(request.form.get('q2', 0))
        q3 = int(request.form.get('q3', 0))
        q4 = int(request.form.get('q4', 0))
        q5 = int(request.form.get('q5', 0))
        score = q1 + q2 + q3 + q4 + q5
        percent = int((score / 150) * 100)
    except:
        percent = 0
    if percent >= 80:
        image = "images/супер.png"
    elif percent >= 50:
        image = "images/средне.png"
    else:
        image = "images/плохо.png"
    return render_template("result.html", percent=percent, image=image)

if __name__ == "__main__":
    app.run(debug=True)