"""
Entry point for the application.

This script starts the Flask application on port 5001, making it accessible from any IP address.
Debug mode is enabled for development purposes, which provides detailed error messages and
an interactive debugger.
"""

from app import app

if __name__ == "__main__":
    app.run(port=5001, host="0.0.0.0", debug=True)
