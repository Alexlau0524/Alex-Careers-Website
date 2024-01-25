from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': 'Rs. 10,00,000'
}, {
    'id': 2,
    'title': 'Frontend Engineer',
    'location': 'Delhi, India',
    'salary': 'Rs. 12,00,000'
}, {
    'id': 3,
    'title': 'Data Engineer',
    'location': 'Remote',
    'salary': 'Rs. 15,00,000'
}, {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'San Francisco, USA',
    'salary': 'Rs. 20,00,000'
}]


@app.route('/')
def hello_alex():
  return render_template('home.html', jobs=JOBS, company_name='Alex')


@app.route("/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
