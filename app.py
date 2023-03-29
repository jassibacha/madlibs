from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from markupsafe import Markup
from stories import story

app = Flask(__name__)

app.config['SECRET_KEY'] = "aliceisaqt"
debug = DebugToolbarExtension(app)

@app.route('/')
def home_page():
    """Shows home page"""
    prompts = story.prompts
    return render_template('home.html', prompts=prompts)
    
@app.route('/story')
def show_story():
    """Shows their story"""
    print('request.args output:', request.args)
    text = story.generate(request.args)
    print('text:', text)
    text2 = Markup(text)
    print('text2:', text2)
    return render_template('story.html', text=text2)
    # place = request.args['place']
    # noun = request.args['noun']
    # verb = request.args['verb']
    # adjective = request.args['adjective']
    # plural_noun = request.args['plural_noun']
    # text = story.generate({"place":place, "noun":noun, "verb":verb, "adjective":adjective, "plural_noun":plural_noun})
    # return render_template('story.html', text=text)