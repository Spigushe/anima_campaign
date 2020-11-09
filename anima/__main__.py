import copy
import urllib.parse
import re
import unidecode

import flask
import jinja2.exceptions

app = flask.Flask(__name__, template_folder="templates")

# favicon redirection - need when serving card images directly
@app.route("/favicon.ico")
def favicon():
    return flask.redirect(flask.url_for("static", filename="img/favicon.ico"))

# Defining Errors
@app.errorhandler(jinja2.exceptions.TemplateNotFound)
@app.errorhandler(404)
def page_not_found(error):
    return flask.render_template("404.html"), 404

# Default route
@app.route("/")
@app.route("/<path:page>")
def index(page=None):
	redirect = False
	if not page:
		page = "index.html"
		redirect = True
	if redirect:
		return flask.redirect(page, 301)

	return flask.render_template(page)

if __name__ == "__main__":
    app.run(debug=True)
