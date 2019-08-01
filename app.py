from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        'author': 'author1',
        'title': 'Post 1',
        'content': 'First content',
        'date_posted': 'August 1, 2019'
    }, 
    {
        'author': 'author2',
        'title': 'Post 2',
        'content': 'Second content',
        'date_posted': 'August 1, 2019'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)