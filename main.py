from tkinter import *
root = Tk()
root.geometry("800x500")
root.title("Степан Калачев")
label = Label(root, text="Hello world!", font=("Arial", 18))
label.pack(padx=20, pady=20)
textbox = Text(root, height=3, font=("Arial", 16))
textbox.pack(padx=20, pady=20)
buttonFrame = Frame(root)
buttonFrame.columnconfigure(0, weight=1)
buttonFrame.columnconfigure(1, weight=1)
btn1 = Button(buttonFrame, text="1", font=("Arial", 18))
btn1.grid(row=0, column=0, sticky="we")
buttonFrame.pack(fill="x")
root.mainloop()