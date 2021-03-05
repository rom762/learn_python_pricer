from flask import Flask, render_template


app = Flask(__name__)

menu = {
    'Home': '/',
    'News': '/news',
    'Weather': '/weather',
    'Register': '/register',
}


@app.route('/')
def index():
    title = 'Pricer web-service'
    return render_template('index.html', page_title=title, menu=menu)


if __name__ == "__main__":
    app.run(debug=True)