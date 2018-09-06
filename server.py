from flask import  Flask,request

from BackEnd.Controller import Validation







app = Flask(__name__)



# these are apis
# @app.route('/')
# def hello():
#     return "hell"

# @app.route('/login')
# def login():
#     # u can use htmls
#     return "<h1>login</h1>"
#
# # passing variables like this strings
# @app.route('/profile/<username>')
# def profile(username):
#     return 'hey there %s' %username
#
# #passing other variables like this
# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     return 'hey there %s' % post_id

@app.route('/')
def hello():

    return '<h1>correctnessof the answer:</h1>%s'%Validation.func()
    # return "Method used: %s" % request.method

# BACON PAGE CAPABLE HANDLING BOTH GET AND POST
@app.route("/bacon",methods=['GET','POST'])
def hello1():
    if request.method == 'POST':
        return "you use POST"
    else:
        return "you use get"

# @app.route('/login')
# def login():
#     a="jaja"
#     return "<h1>"%a%"</h1>"




if __name__ == "__main__":
    app.run(debug=True)