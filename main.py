from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    students = {
        1: {
            'name': 'taras',
            'age': 20,
            'uni': 'KPI'
        },
        2: {
            'name': 'taras',
            'age': 20,
            'uni': 'KPI'
        },
        3: {
            'name': 'taras',
            'age': 20,
            'uni': 'KPI'
        },
    }

    return render_template('main.html', students=students.values())


@app.route('/about-us')
def about_us():
    return render_template(
        'about-us.html',
        title='About Us',
        name='red',
        age=20,
        university='KPI',
        languages=['php', 'py', 'c', 'c++', 'java']
    )


@app.route('/contact')
def contact():
    return render_template('main.html')


@app.route('/blog')
def blog():
    return render_template('blog.html')


if __name__ == '__main__':
    app.run(debug=True)