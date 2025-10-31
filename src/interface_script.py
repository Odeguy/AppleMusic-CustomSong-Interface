import tkinter
from tkinter import filedialog
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
        from_file_button = ttk.Button(tab_select, text="Add From File", command= lambda: App.open_add_from_file(root))
        from_file_button.pack()

        from_link_button = ttk.Button(tab_select, text="Add From Link", command= lambda: App.open_add_from_link(root))
        from_link_button.pack()

        config_button = ttk.Button(tab_select, text="Configure", command= lambda: App.open_config(root))
        config_button.pack()

        root.mainloop()

    def new_tab(type, root):
        if App.tabs.__contains__(type): return

        frame = ttk.Frame(root, relief="solid", borderwidth=5, padding="10 10 10 10")
        frame.pack(expand=True, anchor="nw", fill="both", side="left")
        frame.propagate(False)

        exit_button = ttk.Button(frame, width=10, text="Close", command= lambda: App.remove_frame(type, frame), padding="10 10 10 10")
        exit_button.pack(anchor="ne", side="top")

        App.tabs[type] = frame
        return frame

    def remove_frame(type, frame):
        frame.destroy()
        App.tabs.pop(type)

    def open_add_from_file(root):
        audio_file: str
        image_file: str

        frame = App.new_tab("Add From File", root)

        file_selector = ttk.PanedWindow(frame, orient="horizontal")
        file_selector.pack(anchor="n", side="top", fill="x", expand=True)
        
        file_select_button = ttk.Button(file_selector, width =  10, text="Choose File", command= lambda: file_dialogue("image"), padding="10 10 10 10")
        file_select_button.pack(side="left")

        file_select_entry = ttk.Entry(file_selector)
        file_select_entry.pack(side="left", expand=True, fill="x", anchor="center")

        properties_selector = ttk.PanedWindow(frame, orient="vertical")
        properties_selector.pack(anchor="n", side="top", fill="x", expand=True)

        properties = dict.fromkeys([
            "album",
            "albumartist",
            "artist",
            "artwork",
            "comment",
            "compilation",
            "composer",
            "discnumber",
            "genre",
            "lyrics",
            "totaldiscs",
            "totaltracks",
            "tracknumber",
            "tracktitle",
            "year",
            "isrc"
        ])
        for property in properties.keys():
            if property == "artwork": continue
            widget = ttk.PanedWindow(properties_selector, orient="horizontal", height=500)
            widget.pack(anchor="center", side="top", fill="x", expand=True)

            label = ttk.Label(widget, text=property, padding="10 0 10 0")
            label.pack(side="left", anchor="center")

            entry = tkinter.Entry(widget, textvariable=properties[property])
            entry.pack(anchor="n", side="left", fill="x", expand=True)

        file_type_widget = ttk.PanedWindow(frame, orient="horizontal", height=500)
        file_type_widget.pack(anchor="center", side="top", fill="x", expand=True)

        file_type_label = ttk.Label(file_type_widget, text="Final File Type", padding="10 0 10 0")
        file_type_label.pack(side="left", anchor="center") 

        file_type_box = ttk.Combobox(file_type_widget, values=operations.Operations.file_types)
        file_type_box.pack()
        file_type_box.set(operations.Operations.file_types[0])

        file_type: str

        def select_file_type(event):
            file_type = file_type_box.get()

        file_type_box.bind("<<ComboboxSelected>>", select_file_type)

        def file_dialogue(type):
            #type = image or str
            file_path = filedialog.askopenfile().name

            file_select_entry.delete(0, len(file_select_entry.get()))
            file_select_entry.insert(0, file_path)

        confirmation_box = ttk.Button()

        
    
    def open_add_from_link(root):
        frame = App.new_tab("Add From Link", root)
    
    def open_config(root):
        frame = App.new_tab("config", root)


if __name__ == "__main__":
    App()