import tkinter as tk
from time import strftime

root= tk.Tk()
root.title('Digital Clock')

def time():
    string = strftime('%H:%M:%S %p \n %D')
    Label.config(text=string)
    Label.after(1000, time) #Update the time every second

Label = tk.Label(root, font=('calibri', 50, 'bold'), background='yellow', foreground='black')
Label.pack(anchor='center')

time()
root.mainloop()
# mainloop() is a method from tkinter that keeps the application running and responsive to user interactions. It waits for events such as button clicks or window actions and updates the GUI accordingly.
