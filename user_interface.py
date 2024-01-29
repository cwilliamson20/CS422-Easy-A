from tkinter import *
from tkinter import filedialog
from tkinter import ttk
# testing push
class EasyAUserInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("EasyA")

        # Set minimum size for main window
        self.root.minsize(500, 300)

        # Create frames for each page
        self.home_frame = Frame(root)
        self.user_frame = Frame(root)
        self.supervisor_frame = Frame(root)

        # Initialize pages
        self.create_home_page()
        self.create_user_page()
        self.create_supervisor_page()

        # Show home page initially
        self.show_home_page()

    def create_home_page(self):
        Label(self.home_frame, text="Welcome to EasyA!").pack()
        Button(self.home_frame, text="User Mode", command=self.show_user_page).pack()
        Button(self.home_frame, text="Supervisor Mode", command=self.show_supervisor_page).pack()

        # TODO: Hide Main Menu button on home page

    def create_user_page(self):

        # Column 1:

        Label(self.user_frame, text="Graph Type:").grid(row=0, column=0, padx=(0, 20), pady=(0, 10))
        # Add radio buttons
        var = IntVar()
        R1 = Radiobutton(self.user_frame, text="Single Class", variable=var, value=1)
        R1.grid(row=2, column=0, sticky=W, padx=(0, 20))
        R2 = Radiobutton(self.user_frame, text="Single Department", variable=var, value=2)
        R2.grid(row=3, column=0, sticky=W, padx=(0, 20))
        R3 = Radiobutton(self.user_frame, text="Single Department Level", variable=var, value=3)
        R3.grid(row=4, column=0, sticky=W, padx=(0, 20))

        # Department Level drop-down list
        Label(self.user_frame, text="Department Level:").grid(row=5, column=0, sticky=W, pady=(10, 0))
        class_level_box = ttk.Combobox(
            self.user_frame,
            state="readonly",
            values=["100", "200", "300", "400"]
        )
        class_level_box.set("100")  # Set default value to "100"
        class_level_box.grid(row=6, column=0, sticky=W)

        # Year drop-down list
        Label(self.user_frame, text="Year:").grid(row=7, column=0, sticky=W, pady=(10, 0))
        year_box = ttk.Combobox(
            self.user_frame,
            state="readonly",
            values=["2013", "2014", "2015", "2016"]
        )
        year_box.set("2013")  # Set default value to "100"
        year_box.grid(row=8, column=0, sticky=W)

        # Subject Code drop-down list
        Label(self.user_frame, text="Course Code:").grid(row=9, column=0, sticky=W, pady=(10, 0))
        subject_box = ttk.Combobox(
            self.user_frame,
            state="readonly",
            values=["CS", "etc", "etc", "etc"] # TODO: ADD CORRECT COURSE CODES
        )
        subject_box.set("todo")  # Set default value to "100"
        subject_box.grid(row=10, column=0, sticky=W)

        # Course Number text box
        Label(self.user_frame, text="Course Number:").grid(row=11, column=0, sticky=W, pady=(10, 0))

        # Create a style
        style = ttk.Style()

        # Configure style to have a border
        style.configure('TEntry', borderwidth=2, relief="solid")

        # Create Entry / text box with visible border
        course_num_entry = ttk.Entry(self.user_frame, style='TEntry')
        course_num_entry.grid(row=12, column=0, sticky=W, pady=(0, 10))

        # Column 2:
        Label(self.user_frame, text="Display Options:").grid(row=0, column=1, sticky=W, pady=(0, 10))
        # Add check boxes
        var1 = IntVar()
        var2 = IntVar()
        var3 = IntVar()
        c1 = Checkbutton(self.user_frame, text='Show % As', variable=var1, onvalue=1, offvalue=0)
        c1.grid(row=2, column=1, sticky=W)
        c2 = Checkbutton(self.user_frame, text='Show Only Regular Faculty', variable=var2, onvalue=1, offvalue=0)
        c2.grid(row=3, column=1, sticky=W)
        c3 = Checkbutton(self.user_frame, text='Show Class Count on X-Axis', variable=var3, onvalue=1, offvalue=0)
        c3.grid(row=4, column=1, sticky=W)

        # Enter button
        Button(self.user_frame, text="Enter", command=self.enter_graph).grid(row=5, column=1, sticky=W, pady=(10, 0))

    def create_supervisor_page(self):

        # Main Menu button
        main_menu_button = Button(self.root, text="Main Menu", command=self.show_home_page)
        main_menu_button.pack(side=TOP, anchor=NE)

        Label(self.supervisor_frame, text="Supervisor Page").pack()
        Button(self.supervisor_frame, text="Select File", command=self.select_file).pack()

    def show_home_page(self):
        self.hide_frames()
        self.home_frame.pack()

    def enter_graph(self):
        Label(self.user_frame, text="Graph data entered").grid(row=6, column=1, sticky=W)

    def show_user_page(self):
        self.hide_frames()
        self.user_frame.pack()

    def show_supervisor_page(self):
        self.hide_frames()
        self.supervisor_frame.pack()

    def hide_frames(self):
        self.home_frame.pack_forget()
        self.user_frame.pack_forget()
        self.supervisor_frame.pack_forget()

    def select_file(self):
        file_path = filedialog.askopenfilename(title="Select a File")
        if file_path:
            print(f"Selected File: {file_path}")

if __name__ == "__main__":
    root = Tk()
    app = EasyAUserInterface(root)
    root.mainloop()
