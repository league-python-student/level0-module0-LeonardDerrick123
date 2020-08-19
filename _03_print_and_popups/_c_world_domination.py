from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':


    # Make a new window variable, window = Tk()
    yhafhdije889P = Tk()
    # Hide the window using the window's .withdraw() method
    yhafhdije889P.withdraw()
    # 1. Ask the user if they know how to write code.
    th = simpledialog.askstring(None, "Do you know how to write code")
    # 2. If they say "yes", tell them they will rule the world in a message box pop-up.
    if "yes" == th.lower():
        messagebox.showinfo(None, "you will rule the world")
    # 3. Otherwise, tell them to sign up for classes at The League in an error box pop-up.
    else:
        messagebox.showinfo(None, "well then get to signing up for classes at the League")
    # Run the window's .mainloop() method
    yhafhdije889P.mainloop()