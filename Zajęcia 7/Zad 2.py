from flask import Flask, request, redirect, render_template_string
import sqlite3
import os

app = Flask(__name__)
DATABASE = 'teachers.db'

def setup_database():
    if not os.path.exists(DATABASE):
        with sqlite3.connect(DATABASE) as conn:
            cur = conn.cursor()
            cur.execute('''
                CREATE TABLE Teacher (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    subject TEXT NOT NULL,
                    time TEXT NOT NULL
                )
            ''')
            cur.executemany('''
                INSERT INTO Teacher (name, subject, time)
                VALUES (?, ?, ?)
            ''', [
                ("Anna Kowalska", "Matematyka", "08:00"),
                ("Jan Nowak", "Fizyka", "09:00"),
                ("Maria Wiśniewska", "Chemia", "10:00")
            ])
            conn.commit()

def fetch_teachers():
    with sqlite3.connect(DATABASE) as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM Teacher")
        return cur.fetchall()

def insert_teacher(name, subject, time):
    if name and subject and time:
        with sqlite3.connect(DATABASE) as conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO Teacher (name, subject, time) VALUES (?, ?, ?)", (name, subject, time))
            conn.commit()

def remove_teacher(teacher_id):
    with sqlite3.connect(DATABASE) as conn:
        cur = conn.cursor()
        cur.execute("DELETE FROM Teacher WHERE id = ?", (teacher_id,))
        conn.commit()

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if 'delete_id' in request.form:
            remove_teacher(request.form['delete_id'])
        else:
            insert_teacher(
                request.form.get('name', '').strip(),
                request.form.get('subject', '').strip(),
                request.form.get('time', '').strip()
            )
        return redirect('/')

    teachers = fetch_teachers()
    return render_template_string('''
        <html>
        <head>
            <title>Nauczyciele</title>
        </head>
        <body>
            <h1>Aktualna lista nauczycieli</h1>
            <ul>
                {% for id, name, subject, time in teachers %}
                    <li>
                        {{ name }} — {{ subject }} ({{ time }})
                        <form method="post" style="display:inline">
                            <input type="hidden" name="delete_id" value="{{ id }}">
                            <button type="submit">🗑 Usuń</button>
                        </form>
                    </li>
                {% endfor %}
            </ul>

            <h2>Dodaj nowego nauczyciela</h2>
            <form method="post">
                <label>Imię i nazwisko:</label><br>
                <input type="text" name="name" required><br>
                <label>Przedmiot:</label><br>
                <input type="text" name="subject" required><br>
                <label>Godzina:</label><br>
                <input type="text" name="time" required><br><br>
                <button type="submit">➕ Dodaj</button>
            </form>
        </body>
        </html>
    ''', teachers=teachers)

if __name__ == '__main__':
    setup_database()
    app.run(debug=True)
