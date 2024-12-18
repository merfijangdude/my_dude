from flask import Flask
from all.app.main import main_page_blueprint
from all.app.search.views import search_blueprint
app = Flask(__name__)

app.register_blueprint(main_page_blueprint)
app.register_blueprint(search_blueprint)

if __name__ == '__main__':
    app.run(debug=True)