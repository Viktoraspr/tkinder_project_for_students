import tkinter as tk
from classes.tkinder_main_class import TkinderManager


def main():
    master = tk.Tk()
    TkinderManager(master)
    master.mainloop()

if __name__ == '__main__':
    main()