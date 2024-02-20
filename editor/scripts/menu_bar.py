#menu_bar
import tkinter as tk
from tkinter import filedialog, messagebox, ttk, colorchooser
from text_Area import textarea
import os as os
class Menubar:
    def __init__(self, root,text_Area):
        self.root = root
        self.text_Area = text_Area
        self.menubar = tk.Menu(self.root)
        
        
        #Defining menu options as menu objects
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.editmenu = tk.Menu(self.menubar, tearoff=0)
        self.searchmenu = tk.Menu(self.menubar, tearoff=0)
        self.viewmenu = tk.Menu(self.menubar, tearoff=0)
        self.settings = tk.Menu(self.menubar, tearoff=0)
        self.run = tk.Menu(self.menubar, tearoff=0)
        self.window = tk.Menu(self.menubar, tearoff=0)
        self.helpmenu = tk.Menu(self.menubar, tearoff=0)
        
        
        
        #Menu Bar
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        self.menubar.add_cascade(label="Edit", menu=self.editmenu)
        self.menubar.add_cascade(label="Search", menu=self.searchmenu)
        self.menubar.add_cascade(label="View", menu=self.viewmenu)
        self.menubar.add_cascade(label="Settings", menu=self.settings)
        self.menubar.add_cascade(label="Run", menu=self.run)
        self.menubar.add_cascade(label="Window", menu=self.window)
        self.menubar.add_cascade(label="Help", menu=self.helpmenu)
        #Functions of menu bar
        
        
        
        
        
        #functions of file option
        self.filemenu.add_command(label="New",accelerator="Ctrl+N" ,command=self.new_file)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Open", accelerator="Ctrl+O",command=self.open_file)
        self.filemenu.add_command(label="Open Containing Folder", command=self.open_folder)
        self.filemenu.add_command(label="Open Folder as Workspace...", command=self.open_workspace)
        self.filemenu.add_separator()

        #Save OPtions
        self.filemenu.add_command(label="Save", accelerator="Ctrl+S",command=self.save_file)
        self.filemenu.add_command(label="Save As", accelerator="Ctrl+Alt+S",command=self.save_as_file)
        self.filemenu.add_command(label="Save a Copy as", command=self.save_copy_as)
        self.filemenu.add_cascade(label="Save All",accelerator="Ctrl+Shift+S" ,menu=self.save_all)
        self.filemenu.add_separator()

        self.filemenu.add_cascade(label="Rename ...", menu=self.rename)
        self.filemenu.add_separator()
        #CLose Options
        self.filemenu.add_cascade(label="Close",accelerator="Ctrl+W", menu=self.close)
        self.filemenu.add_cascade(label="Close All",accelerator="Ctrl+Shift+W", menu=self.close_all)
        self.filemenu.add_cascade(label="Close Multiple Documents", menu=self.close_multiple)
        
        self.filemenu.add_cascade(label="Move to Recycle Bin", menu=self.move_to_recycle)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", accelerator="Alt+F4",command=self.exit_editor)
        
        
        
        
        
        #functions for edit option
        self.editmenu.add_command(label="Undo",accelerator="Ctrl+Z" ,command=self.undo)
        self.editmenu.add_command(label="Redo",accelerator="Ctrl+Y"  ,command=self.redo)
        self.editmenu.add_separator()
        self.editmenu.add_command(label="Cut",accelerator="Ctrl+X", command=self.cut)
        self.editmenu.add_command(label="Copy",accelerator="Ctrl+C",command=self.copy)
        self.editmenu.add_command(label="Paste", accelerator="Ctrl+V" ,command=self.paste)
        self.editmenu.add_command(label="Delete",accelerator="Del"  ,command=self.delete)
        self.editmenu.add_command(label="Select All",accelerator="Ctrl+A"  ,command=self.select_all)
        self.editmenu.add_command(label="Begin/End Select",command=self.begin_end_select)
        self.editmenu.add_separator()
        self.editmenu.add_command(label="Insert",command=self.insert)
        self.editmenu.add_command(label="Copy to Clipboard", command=self.copy_to_clipboard)
        self.editmenu.add_command(label="Indent",command=self.indent)
        self.editmenu.add_command(label="Convert Case to",command=self.convert_case)
        self.editmenu.add_command(label="Line Operations",command=self.line_operations)
        self.editmenu.add_command(label="Comment/Uncomment",command=self.comment_uncomment)
        self.editmenu.add_command(label="Auto/Uncomment",command=self.auto_uncomment)
        self.editmenu.add_separator()
        self.editmenu.add_command(label="Clipboard History", command=self.clipboard_history)
        self.editmenu.add_separator()
        self.editmenu.add_command(label="Set Read-Only", command=self.set_readonly)
        self.editmenu.add_command(label="Clear Read-Only Flag",command=self.clear_readonly)
        
        #Search Menu
        self.searchmenu.add_command(label="Find",accelerator="Ctrl+F",command=self.find)
        self.searchmenu.add_command(label="Find in Files ...",accelerator="Ctrl+Shift+F",command=self.find_in_files)
        self.searchmenu.add_separator()
        self.searchmenu.add_command(label="Replace",accelerator="Ctrl+H",command=self.replace)
        self.searchmenu.add_separator()
        self.searchmenu.add_command(label="Jump UP",command=self.jump_up)
        self.searchmenu.add_command(label="Jump Down",command=self.jump_down)
        self.searchmenu.add_separator()
        self.searchmenu.add_command(label="Bookmark",command=self.bookmark)
        
        
        
        #View Menu
        self.viewmenu.add_command(label="Always on Top",command=self.always_on_top)
        self.viewmenu.add_command(label="Toggle Full Screen Mode",accelerator="F11",command=self.toggle_full_screen)
        self.viewmenu.add_command(label="Post-It",accelerator="F12",command=self.post_it)
        self.viewmenu.add_command(label="Distraction Free",command=self.distraction_free)
        self.viewmenu.add_separator()
        self.viewmenu.add_command(label="View Current File in",command=self.view_currentfile)
        self.viewmenu.add_separator()
        self.viewmenu.add_command(label="Show Symbol",command=self.show_symbol)
        self.viewmenu.add_command(label="Zoom",command=self.zoom)
        self.viewmenu.add_command(label="Move/Clone Current Document",command=self.move_current_document)
        self.viewmenu.add_command(label="Tab",command=self.tab)
        self.viewmenu.add_command(label="Word Wrap",command=self.word_wrap)
        self.viewmenu.add_command(label="Focus on Another View",accelerator="F8",command=self.focus_on_another_view)
        self.viewmenu.add_command(label="Hide Lines",accelerator="Alt+H",command=self.hide_lines)
        
        
        #Settings MEnu
        
        self.settings.add_command(label="Preferences....",accelerator="Randi Mc",command=self.preferences)
    # Define the methods for your menu commands here
    def new_file(self):
        pass
    file_path = None
    def save_file(self):
        # global self.file_path
        if self.file_path and os.path.exists(self.file_path):
            # Write to the file and close it
            with open(self.file_path, "w") as file:
                file.write(self.text_Area.text_area.get(1.0, tk.END))
        else:
            self.save_as_file()
    def open_file(self):
        self.file_path = filedialog.askopenfilename(defaultextension=".txt",
                                                filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if self.file_path:
            with open(self.file_path, "r") as file:
                self.text_Area.text_area.delete(1.0, tk.END)  # Clear the text area
                self.text_Area.text_area.insert(tk.INSERT, file.read())  # Insert the file content
        
    def save_as_file(self):
        self.file_path = filedialog.asksaveasfile(defaultextension=".txt",
                                        filetypes=[("Text file","*.txt"),("All Files","*.*")])
        if not self.file_path:
            return
        self.file_path.write(self.text_Area.text_area.get(1.0, tk.END))
        self.file_path.close()
    

    def exit_editor(self):
        if messagebox.askokcancel("Exit ?","Do you want to save your changes?"):
            self.save_file()
        self.root.destroy()
        
    def open_folder(self):
        pass

    def open_workspace(self):
        pass

    def save_copy_as(self):
        pass

    def save_all(self):
        pass

    def rename(self):
        pass

    def close(self):
        pass

    def close_all(self):
        pass

    def close_multiple(self):
        pass

    def move_to_recycle(self):
        pass



#Edit Menu Functions
    def undo(self):
        pass
    def redo(self):
        pass
    def cut(self):
        pass
    def copy(self):
        pass
    def paste(self):
        pass

    def delete(self):
        pass

    def select_all(self):
        pass

    def begin_end_select(self):
        pass

    def insert(self):
        pass

    def copy_to_clipboard(self):
        pass

    def indent(self):
        pass

    def convert_case(self):
        pass

    def line_operations(self):
        pass

    def comment_uncomment(self):
        pass

    def auto_uncomment(self):
        pass

    def clipboard_history(self):
        pass

    def set_readonly(self):
        pass

    def clear_readonly(self):
        pass




#Search Functions

    def find(self):
        pass

    def find_in_files(self):
        pass

    def replace(self):
        pass

    def jump_up(self):
        pass

    def jump_down(self):
        pass

    def bookmark(self):
        pass

#View Menu Functions
    def always_on_top(self):
        pass

    def toggle_full_screen(self):
        pass

    def post_it(self):
        pass

    def distraction_free(self):
        pass

    def view_currentfile(self):
        pass

    def show_symbol(self):
        pass

    def zoom(self):
        pass

    def move_current_document(self):
        pass

    def tab(self):
        pass

    def word_wrap(self):
        pass

    def focus_on_another_view(self):
        pass

    def hide_lines(self):
        pass


#Settings Menu Functions
    def preferences(self):
        pass