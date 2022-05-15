from flask import Flask, request, render_template
from stories import story


app = Flask(__name__)

@app.route('/')
def show_form():
    return render_template('form.html', prompts=story.prompts)


@app.route('/story', methods=['post'])
def generate():        
    return render_template('story.html', story=story.generate(request.form))

