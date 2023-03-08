from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from random import randint, choice, sample
app = Flask(__name__)

app.config['SECRET_KEY'] = "chicken"
debug = DebugToolbarExtension(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0')

@app.route('/form2')
def show_form_2():
    return render_template("form2.html")

@app.route('/greet2')
def get_greet_2():
    username = request.args["username"]
    wants = request.args.get("wants_compliments")
    snice_things = sample(COMPLEMENTS, 3)
    return render_template("greet2.html", username=username, wants_compliments=wants, compliment=snice_things)

@app.route('/')
def homepage():
    return render_template('home.html')

COMPLEMENTS = ["cool", "nice", "hot", "fun", "so tall"]

@app.route('/spell/<word>')
def spell_word(word):
    caps_word = word.upper()
    return render_template("spell.html", word=caps_word)

@app.route('/lucky')
def lucky_number():
    num = randint(1,5)
    return render_template("lucky.html", lucky_num = num, msg="you are so lucky")

@app.route('/hello/<name>')
def say_hello(name):
   
    return render_template("hello.html")

@app.route('/goodbye')
def say_bye():
    return render_template('bye.html')

@app.route('/form')
def show_form():
    return render_template('form.html')

@app.route('/greet')
def get_greeting():
    username = request.args("username")
    nice_thing = random.choice(COMPLEMENTS)
    return render_template('greet.html', username = username, comps=nice_thing)

@app.route('/search')
def search():
    term = request.args["term"]
    sort = request.args["sort"]
    #user term to find reulsts in DB
    return f"<h1>Search Results For: {term}</h1> <p>Sorting by:{sort}"

# @app.route("/post", methods=["POST"])
# def post_demo():
#     return "YOU MADE A POST REQUEST"


# @app.route("/post", methods=["GET"])
# def get_demo():
#     return "YOU MADE A GET REQUEST"

@app.route('/add-comment')
def add_comment_form():
    return"""
    <h1> Search Here</h1>
    <form method="POST">
        <input type="text" placeholder='comment' name='comment'/>
        <input type='text' placeholder='username' name='username'/>
        <button type="submit">Submit</button>
    </form>
    """
@app.route('/add-comment', methods=["POST"])
def save_comment():
    comment =request.form["comment"]
    username = request.form["username"]
    return f"""
    <h1>{username} your comment '{comment}' was not necessary</h1>
    """

@app.route('/r/<subreddit>')
def show_subreddit(subreddit):
    return f"<h1> Browsing {subreddit} </h1>"

@app.route("/r/<subreddit>/comments/<int:post_id>")
def show_comments(subreddit, post_id):
    return f"<h1>{subreddit}{post_id}<h/1>"

POSTS= {
    1: 'I like chicken',
    2: 'mayo',
    3: 'rainbow',
    4: 'yolo',
}

@app.route('/posts/<int:id>')
def post_id(id):
    post = POSTS.get(id, "POST NOT FOUND")
    return f"<p>{post}</p>"

