# main.py
from app.views.DashboardView import Dashboard
import os

# Ensure the working directory is set to the directory containing main.py
os.chdir(os.path.dirname(__file__))

def main():
    # Create the view instance
    app = Dashboard()
    app.run()  # Use `run()` instead of `mainloop()` to avoid redundancy

if __name__ == "__main__":
    main()


