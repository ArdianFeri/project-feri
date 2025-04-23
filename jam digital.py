import tkinter as tk
import time

def update_time():
    current_time = time.strftime("%H:%M:%S") 
    label.config(text=current_time)
    window.after(1000, update_time) 

window = tk.Tk()
window.title("Jam Digital")
window.geometry("250x100")
window.config(background="blue")

label = tk.Label(window, font=("Arial", 40), fg="white", bg="black")
label.pack(expand=True)

update_time()

window.mainloop()
