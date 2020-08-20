from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':

    # Make a new window variable, window = Tk()
    thywuteuygyeu = Tk()
    # Hide the window using the window's .withdraw() method
    thywuteuygyeu.withdraw()
    # 1. Create a variable to hold the user's score. Set it equal to zero. 
    ghy = 0
    # ASK A QUESTION AND CHECK THE ANSWER

    #      // 2.  Ask the user a question 
    YUI = simpledialog.askstring(None,"a question")
    #      // 3.  Use an if statement to check if their answer is correct

    if "yes" ==YUI.lower() or "no" == YUI.lower() or "how am I supposed to even answer this" == YUI.lower() or "this dosent make any sense" == YUI.lower()  or "I get it" ==YUI.lower() or "an Answer" ==YUI.lower():
        messagebox.showinfo(None, "yes")
        ghy = 1
    else:
        messagebox.showinfo(None,"NO!")
    #      // 4.  if the user's answer was correct, add one to their score
 
    # MAKE MORE QUESTIONS. Ask more questions by repeating the above 
    #      // Option: Subtract a point from their score for a wrong answer
    for i in range(5):
        YUI = simpledialog.askstring(None, "more questions")

        # If first question
        if i == 0:
            if "yes" ==YUI.lower() or "no" ==YUI.lower() or "again" ==YUI.lower() or "BRUH" ==YUI.lower() or "I'm done" ==YUI.lower() or " are all these the same" ==YUI.lower() or "another one" ==YUI.lower or "stop it" == YUI.lower():
                ghy += 1
        elif i == 1:
            if "yes" == YUI.lower() or "no" == YUI.lower() or "again" == YUI.lower() or "BRUH" == YUI.lower() or "I'm done" == YUI.lower() or " are all these the same" == YUI.lower() or "another one" == YUI.lower or "stop it" == YUI.lower():
                ghy += 1

        messagebox.showinfo(None, "Done")
        #score += 1
    else:
        messagebox.showinfo(None, "U kan T3lL yourslf yoo GXT POINTS but you did(n0t)")
        #score -= 1

    # After all the questions have been asked, tell the user their final score
    # remember to convert your variable to a string using the str() function 
    messagebox.showinfo("Score","Your score")
    messagebox.showinfo("I'm just playhing arount here is your score","score" + str(ghy))
    # Run the window's .mainloop() method
    thywuteuygyeu.mainloop()