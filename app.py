from flask import Flask, render_template, request, redirect, url_for
import datetime
import cabinet
app = Flask(__name__)


@app.route('/') # This is the page that is run if the person goes to the main page. Onboarding Library,
def run(): # Until unboarding code is ready communication method will be used through here.
    time = datetime.datetime.now()
    formatted_now = time.strftime("%A, %d %B, %Y at %X")
    print(formatted_now)
    content = "hello! Its " + formatted_now  # ontent = "Hello there, " + "MY NAME IS JACK" + "! It's " + formatted_now

    return content


@app.route('/addNewTask', methods=['POST', 'GET']) ## This adds a new task to the projects. Intergration Library.
def add_new_task():
    if request.method == 'POST': # If we were sent a POST REQUEST
        # return redirect(url_for('run'))

        email = request.form.get("email")
        nameOfPerson = request.form.get("personName")
        mission = request.form.get("mission")
        alloatedTime = request.form.get("alloatedTime")
        cabinet.add_new_task(email, nameOfPerson, mission, alloatedTime)
        return render_template('newIssue.html', statement=(
                "Email: " + email + " Name: " + nameOfPerson + " Mission: " + mission + " allotatedTime: " + alloatedTime))

    else:
        return render_template('newIssue.html', statement='Please name your task')


@app.route('/respond/<unique_id>/<answer>') # Answers a request -integration library
def change_task_status(unique_id, answer):
    cabinet.change_task(unique_id, 5)
    return render_template('newIssue.html', statement=f'{answer}')


@app.route('/task/<int:task_id>') # Answers a request -integration library
def open_task_page(task_id):
    return render_template('newIssue.html', statement=f'{task_id}')


if __name__ == '__main__':
    app.run()
