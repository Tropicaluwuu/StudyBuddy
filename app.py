from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev'

tasks = []
study_logs = []


@app.route('/', methods=['GET', 'POST'])
def home():
    goal = None
    if request.method == 'POST':
        goal = request.form.get('daily_goal')
    return render_template('home.html', goal=goal)


@app.route('/add-task', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        course = request.form.get('course')
        title = request.form.get('title')
        due_date = request.form.get('due_date')
        priority = request.form.get('priority')

        tasks.append({
            'course': course,
            'title': title,
            'due_date': due_date,
            'priority': priority
        })

        return redirect(url_for('add_task'))

    return render_template('add_task.html', tasks=tasks)


@app.route('/study-log', methods=['GET', 'POST'])
def study_log():
    if request.method == 'POST':
        course = request.form.get('course')
        minutes = request.form.get('minutes')
        notes = request.form.get('notes')

        study_logs.append({
            'course': course,
            'minutes': minutes,
            'notes': notes
        })

        return redirect(url_for('study_log'))

    return render_template('study_log.html', study_logs=study_logs)


if __name__ == '__main__':
    app.run(debug=True)
