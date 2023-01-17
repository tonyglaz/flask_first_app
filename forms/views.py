from flask import Blueprint, render_template,request

forms_blueprint = Blueprint('forms_blueprint', __name__, template_folder='templates', url_prefix='/forms')


@forms_blueprint.route('/')
def forms_page():
    return "main page of forms pages"


@forms_blueprint.route('/get_form')
def my_get_form():
    return render_template("get_form.html")


@forms_blueprint.route('/post_form')
def my_post_form():
    return render_template("post_form.html")

@forms_blueprint.route('/add_into_list', methods=["POST"])
def add_page():
    task = request.form['task_name']
    return f' u add task : {task}'
