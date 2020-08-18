from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block 
if __name__ == '__main__':
    
    # Make a new window variable, window = Tk()
    FGkl996ijL____F= Tk()
    # Hide the window using the window's .withdraw() method
    FGkl996ijL____F.withdraw()
    # Ask the user for their name and save it to a variable
    RTYx7 = simpledialog.askstring(title='Greeter', prompt="What is your name?")

    # Show a message box with your message using the .showinfo() method
    messagebox.showinfo(RTYx7)
    # Print your message to the console using the print() function
    print(RTYx7)
    # Show an error message using messagebox.showerror()
    messagebox.showerror()
    # Run the window's .mainloop() method
    FGkl996ijL____F.mainloop()