from flask import Flask
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h2>Disaster Dashboard</h2>
    <a href="/dashboard">Open Dashboard</a>
    '''

@app.route('/dashboard')
def dashboard():
    output = subprocess.getoutput("python dashboard.py")
    return f"<pre>{output}</pre>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
