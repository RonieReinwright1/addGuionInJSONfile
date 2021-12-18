from tkinter import *
import app
window=Tk()

inputtxt = Text(window, height = 30, width = 600, bg = "light yellow")
def initWindow():
    # add widgets here
    # window.title("creepypasta maker")
    window.geometry("800x600")
    btn=Button(window, text="Add element", fg='blue',height=5 , width=30, command=buttonPressed)
    
    bt2=Button(window, text="save", fg='blue', height=5 , width=30 , command=app.save)
    btn.pack()
    inputtxt.pack()
    bt2.pack()
    window.mainloop()
def buttonPressed():
    INPUT = inputtxt.get("1.0", "end-1c")
    window.title(str(app.index))
    app.addElement(app.guion,app.index,INPUT,1,"hola")
    app.index += 1
