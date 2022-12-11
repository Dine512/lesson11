from flask import Flask, request, render_template
from utils import get_candidate, get_candidates_by_name, get_candidates_by_skill, load_candidates_form_json
app = Flask(__name__)
data = load_candidates_form_json('candidates.json')

@app.route('/')
def index():
    return render_template('index.html', candidates=data)


@app.route('/candidate/<int:x>')
def candidate_x(x):
    candidate = get_candidate(x)
    return render_template('card.html', candidate=candidate)


@app.route('/searh/<candidate_name>')
def search_name(candidate_name):
    candidates = get_candidates_by_name(candidate_name)
    return render_template('search.html', candidates=candidates, count=len(candidates))


@app.route('/skill/<skill_name>')
def skill(skill_name):
    candidates = get_candidates_by_skill(skill_name)
    return render_template('skill.html', candidates=candidates, count=len(candidates))



app.run()

