from flask import Flask, render_template, request
import random

# Initialize Flask app
app = Flask(__name__)

# ---------------- Home Page ----------------
@app.route('/')
def home():
    return render_template('index.html')

# ---------------- Details Page ----------------
@app.route('/details')
def details():
    return render_template('details.html')

# ---------------- Result Page ----------------
@app.route('/result', methods=['POST'])
def result():
    # Retrieve data from the form
    gender = request.form.get('gender')
    job = request.form.get('job')
    absence = request.form.get('absence')
    activities = request.form.get('activities')
    studyHours = request.form.get('studyHours')

    # Subject marks
    math = float(request.form.get('math', 0))
    physics = float(request.form.get('physics', 0))
    biology = float(request.form.get('biology', 0))
    history = float(request.form.get('history', 0))
    chemistry = float(request.form.get('chemistry', 0))
    english = float(request.form.get('english', 0))
    geography = float(request.form.get('geography', 0))

    # Total and average score calculation
    total = math + physics + biology + history + chemistry + english + geography
    average = total / 7

    # Dummy AI Logic (for now)
    # You can later replace this part with ML model predictions
    careers = [
        ("Teacher", round(random.uniform(0.6, 0.9), 2)),
        ("Data Scientist", round(random.uniform(0.1, 0.5), 2)),
        ("Engineer", round(random.uniform(0.1, 0.4), 2)),
        ("Doctor", round(random.uniform(0.2, 0.6), 2)),
        ("Artist", round(random.uniform(0.1, 0.5), 2))
    ]

    # Sort by probability (highest first)
    careers = sorted(careers, key=lambda x: x[1], reverse=True)

    # Send results to HTML
    return render_template('result.html', total=total, average=average, careers=careers)

# ---------------- Run the Flask app ----------------
if __name__ == '__main__':
    app.run(debug=True)
