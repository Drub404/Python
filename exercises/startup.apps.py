import tkinter
# Let's create the Tkinter window
window = tkinter.Tk()
window.title("Startup Apps")

# creating a function called DataCamp_Tutorial()
def mygui():
#   tkinter.Label(window, text = "GUI with Tkinter!").pack()
    print("Hello world")

tkinter.Button(window, text = "Discord", command = mygui).pack()
window.mainloop()