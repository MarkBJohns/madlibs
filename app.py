from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')

from stories import story as story

@app.route('/story', methods=['GET'])
def story_form():
    return render_template('story.html', words=story.prompts)

@app.route('/story/result', methods=['POST'])
def show_story():
    form_data = request.form.to_dict()
    return render_template('result.html', form_data=form_data, story=story)