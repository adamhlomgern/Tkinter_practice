from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

#Label
my_label = Label(text="text", font=("Arial", 24, "bold"))
my_label.pack()


#Button
def button_clicked():
    print("I got clicked")
    my_label.config(text="Button got clicked")


button = Button(text="Click me", command=button_clicked)
button.pack()


#Entry
input = Entry(width=10)
print(input.get())
input.pack()





window.mainloop()
