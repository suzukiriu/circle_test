import tkinter
root=tkinter.Tk()
cvs = tkinter.Canvas(width=600,height=600)
cvs.pack()
cvs.create_oval(5,5,200,200,fill = "red")
cvs.create_oval(200,5,400,200,fill = "yellow")
cvs.create_oval(400,5,600,200,fill = "blue")

cvs.create_oval(5,200,200,400,fill = "red")
cvs.create_oval(200,200,400,400,fill = "yellow")
cvs.create_oval(400,200,600,400,fill = "blue")

cvs.create_oval(5,400,200,600,fill = "red")
cvs.create_oval(200,400,400,600,fill = "yellow")
cvs.create_oval(400,400,600,600,fill = "blue")

root.mainloop()