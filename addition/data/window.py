from tkinter import*

def comand():
    text=Label(w, text="Щось там")
    text.grid(column=1, row=2)

def ent(event):
    comand=txt.get()
    if comand in ["go", "went", "gone"]:
        comand()
    #text=Label(w, text="gopo")
    #text.grid(column=1, row=1)

w=Tk()
w.title("Мій додаток")
w.geometry("400x550")
text=Label(w, text="Команда:  ")
text.grid(column=1, row=0)
txt = Entry(w, width=30)
txt.grid(column=1, row=1)
txt.bind("<Return>", ent)

w.mainloop()

