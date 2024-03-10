# System imports here
import customtkinter
import tkinter as tk
import os
import webbrowser

# File imports here
from about import MyWindow
from menu_Bar import Menubar
from text_Area import textarea
from settings import Settings
from tkinter import ttk, filedialog, PhotoImage
from PIL import Image
import pygments.lexers

# Function import here
from search import Searchwindow
from new_file import newfile_window
from open_file import openfile_window
from chlorophyll import CodeView

# Sets (for now the appearance to light and color scheme to blue)
customtkinter.set_appearance_mode("dark")
    
# Should be replaced with a function in future for catppuccin color scheme 
customtkinter.set_default_color_theme("dark-blue")

# Welcome screen for the text editor disabled because currently a mess 
# Need to work on this mess in future
def show_welcome_window(root):
    welcome_window = customtkinter.CTkToplevel(root)
    # welcome_window.geometry(f"{root.winfo_width()}x{root.winfo_height()}+{root.winfo_x()}+{root.winfo_y()}")
    welcome_window.title("Welcome to NyxText")
    welcome_window.geometry(f"{1100}x{580}")
    welcome_window.wm_overrideredirect(True)
    welcome_window.grab_set()
    welcome_label = customtkinter.CTkLabel(welcome_window, text="Welcome to NyxText, your advanced text editor!\n\nClick 'Start' to proceed.", font=("VictorMono Nerd Font", 14))
    welcome_label.pack(pady=50)
    # Button to destroy the window
    start_button = customtkinter.CTkButton(welcome_window, text="Start", command=welcome_window.destroy, font=("VictorMono Nerd Font", 14))
    start_button.pack(pady=10)

# This defines the main function, which is the entry point of the application
def main():
    global root
    root = customtkinter.CTk()
    root.geometry(f"{1100}x{580}")
    root.title("NyxText")
    # configure grid layout (4x4)
    # Useful for responsiveness 
    root.grid_rowconfigure(0,weight=1)
    root.grid_columnconfigure(0,weight=1)
    root.grid_columnconfigure(1,weight=1)

# This is the icon for the application. It is expected to be in the same directory as the scriptw
    if os.name == 'nt':  # for Windows
        root.iconbitmap("editor/scripts/misc/icons/icon.ico")
    elif os.name == 'posix':  # for Linux and MacOS
        # root.iconphoto(False, PhotoImage(file="editor/scripts/misc/icons/icon.png"))
        pass
    
# Setting width variables
    screen_width = root.winfo_screenwidth() 
    screen_height = root.winfo_screenheight() 
    
# Frames for the main text editor 
    top_frame = customtkinter.CTkFrame(root, width=screen_width,height=int(screen_height * 0.15),corner_radius=0) # Adjust height as needed
    top_frame.grid(row=0, column=0, columnspan=2, sticky='nsew')
    
    left_frame = customtkinter.CTkFrame(root, width=screen_width * 0.16,corner_radius=0)
    left_frame.grid(row=1, column=0,rowspan=4, sticky='nsew') # Ensure left_frame is correctly placed
    
    right_frame = customtkinter.CTkFrame(root, width=int(screen_width)-100,height=int(screen_height)-30,corner_radius=0)
    right_frame.grid(row=1, column=1,sticky='nsew')
    
    bottom_frame = customtkinter.CTkFrame(root, width=screen_width,height=int(screen_height * 0.15),corner_radius=0)
    bottom_frame.grid(row=2, column=0, columnspan=2, sticky='nsew')

    right_frame.grid_rowconfigure(0, weight=1)
    right_frame.grid_columnconfigure(0, weight=2)

# Creates a tab view to show tabs, implimented the dynamic tab view for the workspace (Text Area) :
    tab_view = customtkinter.CTkTabview(right_frame,width=int(screen_width)-250,height=int(screen_height)-200)
    tab_view.grid(row=0, column=0,pady=10, sticky='nsew')
    
# Welcome Tab : 
    welcome_tab = tab_view.add("Welcome")
    
    if os.name == 'nt':  # for Windows
        my_image = customtkinter.CTkImage(light_image=Image.open("main/assets/logo/logo.png"),
                                        dark_image=Image.open("main/assets/logo/logo.png"),
                                        size=(400, 200))
        
        welcome_title_text = customtkinter.CTkLabel(welcome_tab, text="",image= my_image,
                                                font=('JetBrainsMono NF',80,"bold"),
                                                padx=100,anchor="center")
        welcome_title_text.pack(side='top',pady=(100,0))
    elif os.name == 'posix': # for linux
        welcome_title_text = customtkinter.CTkLabel(welcome_tab, text="NyxText",
                                                font=('JetBrainsMono NF',80,"bold"),
                                                padx=100,anchor="center")
        welcome_title_text.pack(side='top',pady=(100,0))

        welcome_title_desc = customtkinter.CTkLabel(welcome_tab, text="- A Catppuccin based Text Editor",
                                                    font=('JetBrainsMono NF',20,"italic"),
                                                    padx=100,anchor="center")
        welcome_title_desc.pack(side='top')
    
    welcome_title_start = customtkinter.CTkLabel(welcome_tab, text="Start",
                                                font=('JetBrainsMono NF',16,"bold"),
                                                padx=100,anchor="center")
    welcome_title_start.pack(side='top',pady=(30,10))
    
# Opens a new window for creating a new file : 
    def new_window(master):
            new = newfile_window(master)
    welcome_new_button = customtkinter.CTkButton(welcome_tab,text=" New file... ", command=lambda: new_window(welcome_tab),
                                                fg_color='transparent',hover=False,anchor="center",text_color='#ed8796')
    welcome_new_button.pack()
    def open_window(master):
            open = openfile_window(master)
    welcome_open_button = customtkinter.CTkButton(welcome_tab,text=" Open file... ", command=lambda: open_window(welcome_tab),
                                                fg_color='transparent',hover=False,anchor="center",text_color='#a6da95')
    welcome_open_button.pack()
    
    welcome_openfolder_button = customtkinter.CTkButton(welcome_tab,text=" Open Folder... ", 
                                                fg_color='transparent',hover=False,anchor="center",text_color='#91d7e3')
    welcome_openfolder_button.pack()
    
    def about_window(master):
            about = MyWindow(master)
    welcome_about_button = customtkinter.CTkButton(welcome_tab, text=" About... ",
                                fg_color='transparent', hover=False, anchor="center", text_color='#8aadf4', command=lambda: about_window(welcome_tab))
    welcome_about_button.pack()
    
    welcome_title_recents = customtkinter.CTkLabel(welcome_tab, text="Recents",
                                                font=('JetBrainsMono NF',16,"bold"),
                                                padx=100,anchor="center")
    welcome_title_recents.pack(side='top',pady=(30,10))
    
    # Static at the moment need to replace with dynamic :
    welcome_recent = customtkinter.CTkButton(welcome_tab,text=" Github/Parazeeknova/Nyxtext ",
                                                fg_color='transparent',hover=False,anchor="center",text_color='#ee99a0')
    welcome_recent.pack()
    
    welcome_recent = customtkinter.CTkButton(welcome_tab,text=" Github/Parazeeknova ",
                                                fg_color='transparent',hover=False,anchor="center",text_color='#ee99a0')
    welcome_recent.pack()

# Workspace continue creates a Default text area for text editing:
# All functions of the menu bar works on this tab, NEED TO FIX AND MAKE THE FUNCTIONS TO WORK ON SELECTED TAB !!
    tab_init = tab_view.add("Workspace")
    
    # Initialize a variable to keep track of the tab count
    global tab_count # Use the global keyword to modify the global variable
    tab_count = 0
    def add_new_tab():
        global tab_count # Use the global keyword to modify the global variable
        tab_count += 1 # Increment the tab count
    # Generate a unique title for the new tab
        tab_title = f"Workspace {tab_count}"
    # Add a new tab to the tab view
        new_tab = tab_view.add(tab_title)
        text_area = textarea(new_tab)
    
        # Temp for testing will remove later
        # text_area = customtkinter.CTkTextbox(new_tab, height=int(screen_height), width=rf, activate_scrollbars=True, wrap='none')
        # text_area.pack(fill='both', expand=True)
        
    # Function to remove the currently selected tab
    def remove_current_tab():
    # Get the currently selected tab
        selected_tab = tab_view.get()
        if selected_tab:
        # Remove the selected tab
            tab_view.delete(selected_tab)

# Code Area (Need to remove in future:)
# Gives the ability for syntax Highlighting 
    global codespace_count
    codespace_count = 0
    def add_new_codespace():
        global codespace_count
        codespace_count += 1 # Increment the tab count
    # Generate a unique title for the new tab
        codespace_title = f"CodeSpace {codespace_count}"
    # Add a new tab to the tab view
        new_codespace = tab_view.add(codespace_title)
        codespace = CodeView(new_codespace,lexer=pygments.lexers.PythonLexer, color_scheme="dracula")
        codespace.pack(fill="both",expand=True)
        
    tab_codespace = tab_view.add("Codespace")
    codeview = CodeView(tab_codespace, lexer=pygments.lexers.PythonLexer, color_scheme="dracula")
    codeview.pack(fill="both", expand=True)

# All Items for the left frame are below :
    Filetree_Button = customtkinter.CTkLabel(left_frame, text="FileTree :", font=("VictorMono Nerd Font",14,"bold"))
    Filetree_Button.grid(row=0, column=0,pady=5, sticky='nsew')
    Filetree_Button.configure(width=2)

# Preparing images for the file tree
# Commented for better version in future 
    # folder_image = PhotoImage("editor/scripts/misc/icons/folder.png")
    # folder_path = folder_image
    
    # file_image = PhotoImage("editor/scripts/misc/icons/file.png")
    # file_path = file_image

# Inside the main function, after creating the left_frame
    file_tree = ttk.Treeview(left_frame,height=35)
    file_tree.heading("#0", text="Files :", anchor="w")
    file_tree.grid(row=1, column=0, sticky='nsew')
    
# Function to put items in the file tree : 
    def populate_file_tree(tree, path):
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            if os.path.isdir(item_path):
            # Insert the directory into the tree and get its ID
                global dir_id
                dir_id = tree.insert("", "end", text=item, open=True) # ,image= folder_path)
            # Recursively populate the directory
                populate_file_tree(tree, item_path)
            else:
            # Insert the file into the tree using the parent directory's ID
                tree.insert(dir_id, "end", text=item) #, image= file_path)

    def open_directory_dialog():
        directory_path = filedialog.askdirectory()
        if directory_path:
        # Clear the current file tree
            for item in file_tree.get_children():
                file_tree.delete(item)
        # Populate the file tree with the selected directory
        populate_file_tree(file_tree, directory_path)

# Styling the Treeview to look dark          
    style = ttk.Style()
    style.configure('Treeview', background='#333', foreground='#fff')
    style.configure('Treeview.Heading', background='#333', foreground='#333')

# Customizing the appearance of selected items and lines
    style.map('Treeview',
    background=[('selected', '#555')],
    foreground=[('selected', '#fff')])

# Bydefault populate the file tree with the desktop directory
    # desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    current_directory_path = os.getcwd()
    populate_file_tree(file_tree, current_directory_path)
    
# Add a button to open the directory dialog
    open_directory_button = customtkinter.CTkButton(left_frame, text="Open Directory", command=open_directory_dialog)
    open_directory_button.grid(row=2, column=0,pady=5, sticky='nsew')

# This imports the text_Area class from a module named text_area.py. This class is expected to contain the logic for creating a text area for the application
    global Textarea
    Textarea = textarea(tab_init)
    
# This imports the Menubar class from a module named menu_bar.py. This class is expected to contain the logic for creating a menu bar for the application
    menu_bar = Menubar(root,Textarea)
    root.config(menu=menu_bar.menubar)
    
# All buttons and search bar in the top frame for different functions (Right)
    def open_settings_window():
        settings = Settings(root)
    settings_button = customtkinter.CTkButton(top_frame, text="⚙️",command=open_settings_window)
    settings_button.pack(side="right",padx=5,pady=10)
    settings_button.configure(width=10)
    
# Switch to change Light and DarkMode :
    def change_appearance_mode_event(new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)
    Appearance_mode_optionemenu = customtkinter.CTkOptionMenu(top_frame, values=["Light", "Dark", "System"],
                                                                        command=change_appearance_mode_event)
    Appearance_mode_optionemenu.pack(side="right",padx=2,pady=10)

# Switch to change the System Scaling to user desired percentage
    def change_scaling_event(new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)
    scaling_optionemenu = customtkinter.CTkOptionMenu(top_frame, width=80,values=["80%", "90%", "100%", "110%", "120%"],
                                                                command=change_scaling_event)
    scaling_optionemenu.pack(side="right",padx=2,pady=10)
    
    def Seperator_R():
        Seperator = customtkinter.CTkLabel(top_frame, text="|")
        Seperator.pack(side="right",padx=2,pady=10)
        Seperator.configure(width=2,font = ("Arial",16),fg_color="transparent")
    Seperator_R()

    def chat_gpt():
            webbrowser.open('https://chat.openai.com/')
    chat_gpt_button = customtkinter.CTkButton(top_frame, text="⚙️ ChatGPT",command=chat_gpt)
    chat_gpt_button.pack(side="right",padx=5,pady=10)
    chat_gpt_button.configure(width=10)
    
    def Phind():
            webbrowser.open('https://www.phind.com/')
    chat_gpt_button = customtkinter.CTkButton(top_frame, text="Phind",command=Phind)
    chat_gpt_button.pack(side="right",padx=5,pady=10)
    chat_gpt_button.configure(width=10)
    
    def Blackbox_AI():
            webbrowser.open('https://www.blackbox.ai/')
    chat_gpt_button = customtkinter.CTkButton(top_frame, text="BlackBox AI",command=Blackbox_AI)
    chat_gpt_button.pack(side="right",padx=5,pady=10)
    chat_gpt_button.configure(width=10)
    
    def Gemini():
            webbrowser.open('https://gemini.google.com/')
    chat_gpt_button = customtkinter.CTkButton(top_frame, text="Gemini",command=Gemini)
    chat_gpt_button.pack(side="right",padx=5,pady=10)
    chat_gpt_button.configure(width=10)
    
    Seperator_R()
    
    # Commented at the moment, will implement later
    
    # right_arrow = customtkinter.CTkButton(top_frame, text=">")
    # right_arrow.pack(side="right",padx=1,pady=10)
    # right_arrow.configure(width= 2,fg_color="transparent")
    
    # Commented at the moment, will be implemented later 
    
    # left_arrow = customtkinter.CTkButton(top_frame, text="<")
    # left_arrow.pack(side="right",padx=1,pady=10)
    # left_arrow.configure(width= 2,fg_color="transparent")
    
# Instantiate SearchWindow and pass the text area
    def open_search_window():
        search = Searchwindow(root)
    serch_button = customtkinter.CTkButton(top_frame,text="🔍 Search",command= open_search_window)
    serch_button.pack(side="right",padx=5,pady=10)
    serch_button.configure(width=10, font= ("VictorMono Nerd Font",15))

# All buttons in the top frame for different functions (Left)
    New_button = customtkinter.CTkButton(top_frame, text="📄")
    New_button.pack(side="left",padx=2,pady=10)
    New_button.configure(width=2,font = ("Arial",18))
    
    Open_button = customtkinter.CTkButton(top_frame, text="📂")
    Open_button.pack(side="left",padx=2,pady=10)
    Open_button.configure(width=2,font = ("Arial",18))
    
    Save_button = customtkinter.CTkButton(top_frame, text="💾")
    Save_button.pack(side="left",padx=3,pady=10)
    Save_button.configure(width=2,font = ("Arial",18))
    
    def Seperator():
        Seperator = customtkinter.CTkLabel(top_frame, text="|")
        Seperator.pack(side="left",padx=2,pady=10)
        Seperator.configure(width=2,font = ("Arial",16),fg_color="transparent")
    Seperator()
        
    Cut_button = customtkinter.CTkButton(top_frame, text="Cut")
    Cut_button.pack(side="left",padx=3,pady=10)
    Cut_button.configure(width=2)
    
    Copy_button = customtkinter.CTkButton(top_frame, text="Copy")
    Copy_button.pack(side="left",padx=3,pady=10)
    Copy_button.configure(width=2)
    
    Paste_button = customtkinter.CTkButton(top_frame, text="Paste")
    Paste_button.pack(side="left",padx=3,pady=10)
    Paste_button.configure(width=2)
    
    select_button = customtkinter.CTkButton(top_frame, text="Select")
    select_button.pack(side="left",padx=3,pady=10)
    select_button.configure(width=2)
    
    undo_button = customtkinter.CTkButton(top_frame, text="Undo")
    undo_button.pack(side="left",padx=3,pady=10)
    undo_button.configure(width=2)
    
    redo_button = customtkinter.CTkButton(top_frame, text="Redo")
    redo_button.pack(side="left",padx=3,pady=10)
    redo_button.configure(width=2)
    
    Seperator()
    
    Suggestions = customtkinter.CTkButton(top_frame, text="Suggest a Feature")
    Suggestions.pack(side="left",padx=2,pady=10)
    Suggestions.configure(width=3) 
    
# About button in the top_bar
    About = customtkinter.CTkButton(top_frame, text="About", command=lambda: about_window(welcome_tab))
    About.pack(side="left",padx=2,pady=10)
    About.configure(width=2)
    
    Seperator()
    
    Exit_button = customtkinter.CTkButton(top_frame, text="Exit")
    Exit_button.pack(side="left",padx=3,pady=10)
    Exit_button.configure(width=2)

# All buttons in the bottom frame for different functions
    # Creating a button for theme change
    # Not working at the moment will implement in future
    
    # def changetheme_event(changetheme_next: str):
    #     customtkinter.set_default_color_theme(changetheme_next)
    # Changetheme_optionmenu = customtkinter.CTkOptionMenu(bottom_frame, values=["blue","dark-blue","green"],
    #                                                         command=changetheme_event)
    # Changetheme_optionmenu.pack(side="left",padx=5,pady=10)
    
    Dir_Label = customtkinter.CTkLabel(bottom_frame, text="Working directory : ")
    Dir_Label.pack(side="left",padx=(10,0),pady=10)
    Dir_Label.configure(width=2,font= ("JetBrainsMono NF",12,"bold"))
    
    dirvar = str(current_directory_path)
    Dir_Label_pth = customtkinter.CTkLabel(bottom_frame, text=dirvar)
    Dir_Label_pth.pack(side="left",padx=2,pady=10)
    Dir_Label_pth.configure(width=2,font= ("JetBrainsMono NF",12))
    
    # Color_Scheme_button = customtkinter.CTkSegmentedButton(bottom_frame, values=["Frappe", "Latte", "Macchiato", "Mocha"])
    # Color_Scheme_button.pack(side="left",padx=5,pady=10)
    # Color_Scheme_button.configure(width=10)
    
    Search_bar = customtkinter.CTkEntry(bottom_frame, placeholder_text="Enter your commands here..")
    Search_bar.pack(side="right",padx=10,pady=10)
    Search_bar.configure(width=250, font = ("VictorMono Nerd Font Bold",15))
    
    def Seperator_R():
        Seperator = customtkinter.CTkLabel(bottom_frame, text="|")
        Seperator.pack(side="right",padx=2,pady=10)
        Seperator.configure(width=2,font = ("Arial",16),fg_color="transparent")
    Seperator_R()

# Add a button to remove the currently selected tab
    remove_tab_button = customtkinter.CTkButton(bottom_frame, text="Remove Tab", command=remove_current_tab)
    remove_tab_button.pack(side="right", padx=5, pady=10)
    
    add_new_tab_button = customtkinter.CTkButton(bottom_frame, text="Add Workspace", command=add_new_tab)
    add_new_tab_button.pack(side="right",padx=5,pady=10)
    
    add_new_codespace_button = customtkinter.CTkButton(bottom_frame, text="Add Codespace", command=add_new_codespace)
    add_new_codespace_button.pack(side="right",padx=5,pady=10)
# The main function is called only when the script is run directly, not when it's imported as a module 
if __name__ == "__main__":
    main()
    # show_welcome_window(root)
    # This is the main loop of the application. It keeps the application running until it is closed
    root.mainloop()