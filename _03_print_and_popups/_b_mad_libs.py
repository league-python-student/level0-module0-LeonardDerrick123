from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':
    
    # Make a new window variable, window = Tk()
    FTghj89 = Tk()
    # Hide the window using the window's .withdraw() method
    FTghj89.withdraw()
    # Put this sentence in a pop-up message box:
    
    # Get the player to enter an adjective
    adj = simpledialog.askstring(None, "adjective")
    # Get the player to enter a type of liquid
    uitubwifusdrytuj2wt43e = simpledialog.askstring(None, "liquid")
    # Get the player to enter a body part
    gjnfre = simpledialog.askstring(None, "verb")
    gh = simpledialog.askstring(None, "body part")
    # Get the player to enter a place
    rterwre = simpledialog.askstring(None, "place")
    # The story below has has been written as a group of Strings joined together by + signs.

    # The story contains place holders, indicated by [** **] which you need to replace with
    # the values entered by the player.
    # Hint:  You will need to add more + signs to join the variables to the other parts of the story.
        
    story = (
    "Piranhas are more "+ adj + " during the day, so cross the river at\n"
    "night. Piranhas are attracted to fresh " + uitubwifusdrytuj2wt43e + " and will most\n"
    "likely take a bite out of your " + gh + " if you " +  gjnfre + ". Whatever\n"
    "you do, if you have an open wound, try to find another way to get "
    "back to the  "+ rterwre +" Good luck!"
    )

    
    # Make a pop-up that contains the final story. The \n escape characters add line breaks to the story. 
    # If you need to, move them around to make your story look better in the pop-up
    messagebox.showinfo("story", story)
    # If you want to write your own Madlib story, just change the story variable and ask the player different questions.


    # Run the window's .mainloop() method
