from flask import Flask
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h2>Disaster Processing System</h2>
    <a href="/run">Click here to Run Project</a>
    '''

@app.route('/run')
def run_project():
    output = subprocess.getoutput("python main.py")
    return f"<pre>{output}</pre>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
