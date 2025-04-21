from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
from flask import Flask, render_template

app = Flask(__name__)

# Global list to store To-Do items
todo_list = []


@app.route('/')
def index():
    return render_template('index.html', todos=todo_list)


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request, redirect

app = Flask(__name__)

todo_list = []


@app.route('/')
def index():
    return render_template('index.html', todos=todo_list)


@app.route('/submit', methods=['POST'])
def submit():
    task = request.form['task']
    email = request.form['email']
    priority = request.form['priority']

    # Validate input
    if priority not in ['Low', 'Medium', 'High']:
        return redirect('/')

    # Add the new task to the list
    todo_list.append({"task": task, "email": email, "priority": priority})
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)


@app.route('/clear', methods=['POST'])
def clear():
    todo_list.clear()
    return redirect('/')
