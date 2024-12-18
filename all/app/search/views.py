from flask import render_template, Blueprint

search_blueprint = Blueprint("search_blueprint", __name__, template_folder="templates")


@search_blueprint.route("/posts/", methods=["GET"])
def search_posts():
    return render_template("search.html")

#@search_blueprint.route("/posts/<", methods=["GET"])