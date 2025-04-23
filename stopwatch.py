import tkinter as tk

detik = 0
jalan = False

def mulai():
    global jalan
    jalan = True
    hitung()

def stop():
    global jalan
    jalan = False

def reset():
    global detik
    detik = 0
    label.config(text="00:00:00")

def hitung():
    global detik
    if jalan:
        detik += 1

        jam = detik // 3600
        menit = (detik % 3600) // 60
        dtk = detik % 60

        label.config(text=f"{jam:02}:{menit:02}:{dtk:02}")
        window.after(1000, hitung)

window = tk.Tk()
window.title("Stopwatch")
window.geometry("500x400")
window.config(bg="pink")

label = tk.Label(window, text="00:00:00", font=("Arial", 38) , bg="pink")
label.pack(pady=40)

tombol_mulai = tk.Button(window, text="Mulai", font=("Arial", 14) , command=mulai)
tombol_mulai.pack(pady=10)

tombol_stop = tk.Button(window, text="Stop", font=("Arial" , 14), command=stop)
tombol_stop.pack(pady=10)

tombol_reset = tk.Button(window, text="Reset", font=("Arial", 14),command=reset)
tombol_reset.pack(pady=10)

window.mainloop()
