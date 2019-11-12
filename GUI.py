# Front end Graphical User Interface for Readit application.
# Version beta 0.2
# Authors: Josh Duran, Kenny Ngo, Alex Debont, Chase Pan
# Created for HackUTD 2019

from tkinter import *
from tkinter import messagebox
from Backend import *


# Runs when the button on the screen is pressed (or when the enter key is pressed)
def button_pressed(url):
    try:
        # Gets a string (the reddit link) from the url entry box
        link = url.get()

        # The title, body, and author variables are initialized using the get_data() function
        title, body, author = get_data(link, create_reddit_object())
        # The comment variable is initialized using the get_comments() function
        comments = get_comments(link)

        # A combined string is generated using the master_string() function and the title, body, author and comments
        combined_str = master_string(title, body, author, comments)

        # Finally, the say_post() function will output to the speakers the combined string
        say_post(combined_str)
    except:
        # If the url link does not lead to a proper reddit post, then the user gets a warning pop up and an error
        # is printed to the console
        print("ERROR: Invalid Link!")
        show_link_warning()


# Function that displays a warning pop up when there is an invalid link
def show_link_warning():
    messagebox.showwarning("Warning", "Please enter in a valid Reddit link!")


# Shows a help pop up, called whenever user clicks 'help' under top menu
def show_help_box():
    messagebox.showinfo("Help", "Enter in a Reddit link and press the button to have the post read to you")


# Shows an about pop up with information about the application, called whenever user clicks 'about' under top menu
def show_about_box():
    messagebox.showinfo("About", "Readit is an application that reads Reddit posts. Developed by Josh Durana, "
                                 "Kenny Ngo, Alex Debont, and Chase Pan for HackUTD 2019")


# Exits the program, called whenever user clicks 'exit' under to menu
def exit_program():
    exit()


# Controls all the GUI features of the application
def main():
    # Creates a new Tkinter object called window
    window = Tk()
    window.title("Readit beta v0.2")
    window.geometry('600x400')
    mycolor = '#fa8366'
    window.configure(background=mycolor)
    window.resizable(False, False)

    # Controls the top menu bar
    menu = Menu(window)
    help = Menu(menu)
    file = Menu(menu)
    window.config(menu=menu)
    file.add_command(label="Exit", command=exit_program)
    menu.add_cascade(label="File", menu=file)
    help.add_command(label="Help", command=show_help_box)
    help.add_command(label="About", command=show_about_box)
    menu.add_cascade(label="Help", menu=help)

    # Large label at top middle of application
    secondlabel = Label(window, text='Readit beta v0.2', bg=mycolor, font=("Arial", 20)).grid(row=0, column=2)

    # Configures the window to look more symmetrical
    window.grid_rowconfigure(0, weight=1)
    window.grid_rowconfigure(3, weight=1)
    window.grid_rowconfigure(5, weight=1)
    window.grid_columnconfigure(0, weight=1)
    window.grid_columnconfigure(3, weight=1)

    # A label that tells the user to enter in the reddit link
    label = Label(window, text='Enter a reddit link: ', bg=mycolor, font=("Arial", 12)).grid(row=2)

    # The entry box where the user inputs a link
    url_entry = Entry(window, width=50)
    url_entry.grid(row=2, column=2)

    # Binds the entry box to the Enter key, ie whenever enter key pressed the the button_pressed() function runs
    url_entry.bind("<Return>", (lambda event: button_pressed(url_entry)))

    # Creates a button and binds the button press to the button_pressed() function
    enter = Button(window, text="Read It!", width=10, height=2, command=lambda: button_pressed(url_entry)).grid(row=3,
                                                                                                                column=2)
    window.mainloop()


main()
