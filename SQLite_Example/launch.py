"""
launch.py

This is where you will press the execute button in order to
launch the application.
"""

# Imports
import traceback
from framework import app

# Call to main
if __name__ == '__main__':
    try:
        # Runs the app
        app.run(debug=app.debug, host='localhost', port=8097)
    except Exception as e: # Prints the traceback to the failure
        traceback.print_exc()
