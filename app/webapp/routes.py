"""
Set up Flask stuff
"""
from flask import Blueprint, render_template
from flask import send_from_directory
from flask import request, redirect

# import questions

"""
configure blueprint
"""
webapp_blueprint = Blueprint(
    'webapp', 
    __name__, 
    template_folder='templates',
)


"""
Renders home page
"""
@webapp_blueprint.route('/anyotherpage')
def serve_home():
    return render_template('home.html')

"""
Serves static file for web app index.html file 
"""
@webapp_blueprint.route('/')
def serve_client():
    return send_from_directory('webapp/static/client', 'index.html')

"""
Serves static files like CSS and JS for webapp
"""
@webapp_blueprint.route('/<path:path>')
def serve_client_files(path):
    return send_from_directory('webapp/static/client', path)
