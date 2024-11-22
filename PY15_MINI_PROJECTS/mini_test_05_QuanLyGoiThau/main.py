import subprocess
import os

def run_app():
    # Get the path to app.py
    app_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'CTK', 'app.py')

    # Run app.py
    subprocess.run(['python', app_path])

if __name__ == "__main__":
    run_app()