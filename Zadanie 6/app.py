from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Globalna lista zadań
tasks = []
task_id_counter = 1

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/tasks', methods=['GET', 'POST'])
def task_list():
    global task_id_counter
    if request.method == 'POST':
        title = request.form['title']
        tasks.append({'id': task_id_counter, 'title': title, 'done': False})
        task_id_counter += 1
        return redirect(url_for('task_list'))
    return render_template('tasks.html', tasks=tasks)

@app.route('/delete/<int:id>')
def delete(id):
    global tasks
    tasks = [task for task in tasks if task['id'] != id]
    return redirect(url_for('task_list'))

@app.route('/done/<int:id>')
def mark_done(id):
    for task in tasks:
        if task['id'] == id:
            task['done'] = True
    return redirect(url_for('task_list'))

if __name__ == '__main__':
    app.run(debug=True)
