import logging

from flask import Blueprint, render_template, request

from flask_begin.utils import get_candidates_by_name, get_candidates_by_skill

search_blueprint = Blueprint('search_blueprint', __name__,template_folder='templates',url_prefix='/search')


@search_blueprint.route("/search_by_name/<name>")
def search_by_name(name):
    logging.info("search page requested")
    candidates = get_candidates_by_name(name)
    return render_template("search.html", candidates=candidates, candidates_len=len(candidates))


@search_blueprint.route('/skills/<skill>')
def get_skills(skill):
    logging.info("skills page requested")
    candidates = get_candidates_by_skill(skill)
    return render_template("skills.html", candidates=candidates, candidates_len=len(candidates), skill=skill)


@search_blueprint.route('/search_by_word')
def search_by_word():
    s = request.args['s']
    return f'ur input is word: {s}'
