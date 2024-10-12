from flask import Blueprint, render_template

# Create a Blueprint instance
main_bp = Blueprint('main', __name__)

# Define a route for the homepage
@main_bp.route('/')
def home():
    return render_template('structure.html')  # Render the structure.html template
