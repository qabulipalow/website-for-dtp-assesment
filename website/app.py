from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/add', methods=['GET', 'POST'])
def add():
    name = request.form.get('name')
    return render_template('home.html', title=name)

if __name__ == '__main__':
    app.run(debug=True)