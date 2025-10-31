import tkinter
from tkinter import ttk
import sv_ttk
import json
from src import operations

#run using python -m src.interface_script
tab_select_width = 400
tab_width = 1200 - tab_select_width

class App():
    tabs = {}
    config_file_path = "src\config.json"
    with open(config_file_path, "r") as file:
            configuration = json.load(file)
    def __init__(self):
        pass
        
        root = tkinter.Tk(className=" Apple Music Custom Song Interface")
        root.geometry("1200x900")
        sv_ttk.set_theme("dark")
        
        tab_select = ttk.Frame(root,  relief="solid", borderwidth=5, padding="10 10 10 10")
        tab_select.pack(expand=True, anchor="nw", fill="both", side="left")
        tab_select.propagate(False)

        logo = ttk.Label(tab_select, anchor="center", text="AM Custom Songs")
        logo.pack()

        #initizalize all buttons
        home_button = ttk.Button(tab_select, text="Home", command= lambda: App.open_home(root))
        home_button.pack()

        config_button = ttk.Button(tab_select, text="Configure", command= lambda: App.open_config(root))
        config_button.pack()

        root.mainloop()

    def new_tab(type, root):
        if App.tabs.__contains__(type): return

        frame = ttk.Frame(root, relief="solid", borderwidth=5, padding="10 10 10 10")
        frame.pack(expand=True, anchor="nw", fill="both", side="left")
        frame.propagate(False)

        exit_button = ttk.Button(frame, width=10, text="Close", command= lambda: App.remove_frame(type, frame))
        exit_button.pack(anchor="ne", side="right")

        App.tabs[type] = frame
        return frame

    def remove_frame(type, frame):
        frame.destroy()
        App.tabs.pop(type)

    def open_home(root):
        frame = App.new_tab("home", root)
    
    def open_config(root):
        frame = App.new_tab("config", root)


if __name__ == "__main__":
    App()