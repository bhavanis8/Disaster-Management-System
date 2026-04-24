from flask import Flask
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return "Disaster Processing System Running"

@app.route('/run')
def run_script():
    result = subprocess.getoutput("python main.py")
    return f"<pre>{result}</pre>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
