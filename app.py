
from flask import Flask, jsonify, request

app = Flask(__name__)

# Home Route
@app.route('/')
def home():
    return "Welcome to my first API!"

# Student Route
@app.route('/student')
def get_student():
    return jsonify({
        "student_id": "2026-00251",
        "name": "Neca Mae Herbaliga",
        "program": "BSIT",
        "year": 3,
        "section": "B"
    })

# Hello Route
@app.route('/hello')
def say_hello():
    name = request.args.get('name', 'Student')
    return jsonify({
        "message": f"Hello, {name}!"
    })

# Skills Route
@app.route('/skills')
def say_skills():
    return jsonify({
        "skills": [
            "HTML",
            "CSS",
            "JavaScript",
            "Python",
            "Flask",
            "Database Management"
        ]
    })

if __name__ == '__main__':
    app.run(debug=True)
