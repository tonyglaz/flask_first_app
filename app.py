import logging

from flask import Flask, render_template, request, send_from_directory

from forms.views import forms_blueprint
from search.views import search_blueprint
from utils import get_candidate, load_candidates_from_json

logging.basicConfig(filename="basic.log", level=logging.INFO)

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024
app.register_blueprint(forms_blueprint)
app.register_blueprint(search_blueprint)


@app.route("/")
def page_index():
    logging.info("Main page requested")
    candidates_data = load_candidates_from_json(r"D:\Py_projects\flask_begin\candidates.json")
    return render_template("index.html", candidates=candidates_data)


@app.route("/candidate/<int:uid>")
def profile(uid):
    logging.info("candidate page requested")
    candidate = get_candidate(uid)
    return render_template("profile.html", candidate=candidate)




@app.route('/test_page', methods=["POST", "GET"])
def test_page():
    name = request.values.get('name')
    return f'u input name: {name}'


@app.route('/page_upload')
def page_form_upload():
    return render_template('file_upload.html')


# обработка отправленной формы (с файлом)
@app.route('/upload', methods=["POST"])
def page_upload():
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
    picture = request.files.get('picture')
    __data = request.headers
    if picture:
        filename = picture.filename
        extension = filename.split('.')[-1]
        if extension in ALLOWED_EXTENSIONS:
            picture.save(f"./uploads/{filename}")
            return f'file with name {picture.filename} uploaded and saved'
        else:
            return f' file type \'{extension}\' is not supported'
    else:
        return f' file were not uploaded {picture}'


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory('uploads', path)


@app.errorhandler(413)
def page_not_found(e):
    return "<h1> File is too big, need smaller pls! </h1>"


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
