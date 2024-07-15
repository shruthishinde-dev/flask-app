from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/echo', methods=['POST'])
def echo():
    user_input = request.form['user_input']
    return f"You entered: {user_input}"

if __name__ == "__main__":
    app.run(debug=True)