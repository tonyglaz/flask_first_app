import json

from flask import Flask, render_template

app = Flask(__name__)


def load_candidates_from_json(path):
    global candidates_data
    with open(path, 'r', encoding="utf-8") as file:
        candidates_data = json.load(file)
    return candidates_data


candidates_data = load_candidates_from_json("candidates.json")


def get_candidate(candidate_id):
    for candidate in candidates_data:
        if candidate['id'] == candidate_id:
            return {
                'name': candidate['name'],
                'position': candidate['position'],
                'picture': candidate['picture'],
                'skills': candidate['skills'],
            }
    return {'not_found': 'ничего не найдено'}


def get_candidates_by_name(candidate_name):
    return [candidate for candidate in candidates_data if candidate_name.lower() in candidate['name'].lower()]


def get_candidates_by_skill(skill_name):
    candidates = []
    for candidate in candidates_data:
        skills=candidate['skills'].lower().split(', ')
        if skill_name.lower() in skills:
            candidates.append(candidate)
    return candidates

@app.route("/")
def page_index():
    return render_template("index.html", candidates=candidates_data)


@app.route("/candidate/<int:uid>")
def profile(uid):
    candidate = get_candidate(uid)
    return render_template("profile.html", candidate=candidate)


@app.route("/search/<name>")
def search(name):
    candidates = get_candidates_by_name(name)
    return render_template("search.html", candidates=candidates, candidates_len=len(candidates))


@app.route('/skills/<skill>')
def get_skills(skill):
    candidates=get_candidates_by_skill(skill)
    return render_template("skills.html",candidates=candidates,candidates_len=len(candidates),skill=skill)


@app.route("/messages/")
def page_messages():
    return "user msgs"

    # ^ same things with v
    """
    def page_index():
        return "я тестовая старничка"
    
    app.add_url_rule('/', view_func=page_index)
    """


app.run()
