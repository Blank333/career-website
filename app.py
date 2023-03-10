from flask import Flask, render_template, jsonify
app = Flask(__name__)

JOBS = [
  {
    "id": 1,
    "title": "Data Scientist",
    "location": "Bengaluru, India",
    "salary": "$150,000"
  },
  {
    "id": 2,
    "title": "Data Analyst",
    "location": "Bengaluru, India",
    "salary": "$110,000"
  },
  {    
    "id": 1,
    "title": "Front-End Developer",
    "location": "Pune, India",
    "salary": "$100,000"
  },
  {
    "id": 1,
    "title": "Back-End Developer",
    "location": "California, USA",
    "salary": "$170,000"
  }
]

@app.route("/")
def show_home():
  return render_template("home.html", jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)
  
if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)