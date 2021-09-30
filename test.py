import tkinter as tk
def draw(Canvas):
    pass
def makeCanvas(w,h):
    root=tk.Tk()
    canvas=tk.Canvas(root,width=w,height=h)
    canvas.configure(bd=0,highlightthickness=0)
    canvas.create_rectangle(10,50,110,100)
    canvas.pack()
    draw(canvas)
    root.mainloop()
makeCanvas(400,400)