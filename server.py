from flask import Flask, request, render_template, redirect, url_for
app = Flask(__name__)


@app.route('/')
def index():
#     return 'Index Page'
	# return redirect(url_for('hello', username=request.form.get('username')))
	return redirect(url_for('static', filename='index.html'))

    # return render_template('black_cool_python3/index.html')


@app.route('/about')
def about():
    return 'The about page'

@app.route('/hello')
def hello():
    return 'Hello World'

@app.route('/HW')
def hello_world():
    return 'Hello World!'


@app.route('/HT')
def ht():
    return 'Hello HT!'

@app.route('/AC')
def ac():
    return 'Hello AC!'

@app.route('/door')
def door():
    return 'Hello door!'

@app.route('/HTD/<ht>')
def show_user_profile(ht):
    # show the user profile for that user
    return 'User %s' % ht

@app.route('/post/<string:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %s' % post_id

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        do_the_login()
    else:
        show_the_login_form()





if __name__ == '__main__':
    #app.run()
    app.debug = True
    app.run(host='0.0.0.0')

