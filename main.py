from flask import Flask, render_template, request, redirect
import subprocess

app = Flask(__name__)

pythonApp = "python.exe"

# Initialize the 'number' variable
number = 1
url = "https://google.com"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/update', methods=['POST'])
def update():
    global number
    global url
    new_number = request.form.get('number')
    new_url = request.form.get('url')
    if new_number and new_url:
        number = int(new_number)
        url = new_url
    return redirect('/run_script', code=307)

@app.route('/run_script', methods=['POST'])
def run_script():
    try:
        result = subprocess.run([pythonApp, 'site.py', str(number), url], capture_output=True, text=True, check=True)
        if result.returncode == 0:
            return render_template('success.html')
        else:
            return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error: {e}"

if __name__ == '__main__':
    app.run(debug=True)
