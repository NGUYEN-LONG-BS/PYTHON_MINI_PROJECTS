from app.views.KD01QuanLyGoiThauView import KD01QuanLyGoiThauView
# Ensure the working directory is set to the directory containing main.py
import os
os.chdir(os.path.dirname(__file__))

def main():
    # Create the view instance, no need to pass the controller
    app = KD01QuanLyGoiThauView()
    # Start the Tkinter main loop
    app.mainloop()
    
if __name__ == "__main__":
    main()