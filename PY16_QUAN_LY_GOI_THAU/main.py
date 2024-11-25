from app.views.KD01QuanLyGoiThauView import KD01QuanLyGoiThauView
import os
# Ensure the working directory is set to the directory containing main.py
os.chdir(os.path.dirname(__file__))

if __name__ == "__main__":
    # Initialize and run the app
    app = KD01QuanLyGoiThauView()
    app.mainloop()