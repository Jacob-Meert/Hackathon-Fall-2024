from CraigApp import create_app

# Create an instance of the Flask application
app = create_app()

# The entry point of the application
if __name__ == '__main__':
    # Run the application in debug mode
    app.run(debug=True)