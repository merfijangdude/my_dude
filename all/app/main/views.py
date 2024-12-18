from flask import render_template, Blueprint

main_page_blueprint = Blueprint("main_page_blueprint", __name__, template_folder="templates")

@main_page_blueprint.route("/", methods= ["GET"])
def index():
    print("index")
    print("down")
    print("clown")
    print("mega_down")
    print("until_state_fullest_down")
    print("dang it")
    print("oh dang it")
    print("oh dang itgwe")
    return render_template("user-feed.html")