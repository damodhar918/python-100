from msilib.schema import Font
import tkinter


FONT = ("Arial", 14, "normal")

window = tkinter.Tk()
window.title('MY FIRST GUI PROGRAM')
window.minsize(width=500, height=300)


my_label = tkinter.Label(text='I am a Label', font=FONT)
my_label.pack(side = 'left')

import turtle
mk = turtle.Turtle()
mk.write('Hello World')



window.mainloop()