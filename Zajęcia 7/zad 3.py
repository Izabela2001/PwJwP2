from flask import Flask, request, redirect, render_template_string
import sqlite3
import os

app = Flask(__name__)
DB_NAME = 'todo.db'

def init_db():
    if not os.path.exists(DB_NAME):
        with sqlite3.connect(DB_NAME) as conn:
            c = conn.cursor()
            c.execute('''
                CREATE TABLE Task (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    description TEXT NOT NULL,
                    done INTEGER DEFAULT 0
                )
            ''')
            conn.commit()

def get_tasks():
    with sqlite3.connect(DB_NAME) as conn:
        c = conn.cursor()
        c.execute("SELECT * FROM Task")
        return c.fetchall()

def add_task(description):
    with sqlite3.connect(DB_NAME) as conn:
        c = conn.cursor()
        c.execute("INSERT INTO Task (description) VALUES (?)", (description,))
        conn.commit()

def mark_done(task_id):
    with sqlite3.connect(DB_NAME) as conn:
        c = conn.cursor()
        c.execute("UPDATE Task SET done = 1 WHERE id = ?", (task_id,))
        conn.commit()

def delete_task(task_id):
    with sqlite3.connect(DB_NAME) as conn:
        c = conn.cursor()
        c.execute("DELETE FROM Task WHERE id = ?", (task_id,))
        conn.commit()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'description' in request.form:
            add_task(request.form['description'].strip())
        elif 'done_id' in request.form:
            mark_done(request.form['done_id'])
        elif 'delete_id' in request.form:
            delete_task(request.form['delete_id'])
        return redirect('/')

    tasks = get_tasks()
    return render_template_string('''
        <h1>Lista zadań</h1>
        <ul>
            {% for id, description, done in tasks %}
                <li>
                    {% if done %}
                        <s>{{ description }}</s>
                    {% else %}
                        {{ description }}
                        <form method="post" style="display:inline">
                            <input type="hidden" name="done_id" value="{{ id }}">
                            <button type="submit">✅ Zrobione</button>
                        </form>
                    {% endif %}
                    <form method="post" style="display:inline">
                        <input type="hidden" name="delete_id" value="{{ id }}">
                        <button type="submit">🗑 Usuń</button>
                    </form>
                </li>
            {% endfor %}
        </ul>

        <h2>Dodaj zadanie</h2>
        <form method="post">
            <input type="text" name="description" required>
            <button type="submit">Dodaj</button>
        </form>
    ''', tasks=tasks)


if __name__ == '__main__':
    init_db()
    app.run(debug=True)
