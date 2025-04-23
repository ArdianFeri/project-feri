import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Tic Tac Toe")
window.configure(padx=20, pady=20)
window.config(bg="black")

pemain = "X"

def klik(row, col):
    global pemain
    if buttons[row][col]["text"] == "":
        buttons[row][col]["text"] = pemain
        buttons[row][col]["state"] = "disabled"
        if cek_menang(pemain):
            messagebox.showinfo("Game Over", f"Pemain {pemain} menang!")
            reset()
        elif cek_seri():
            messagebox.showinfo("Game Over", "Seri!")
            reset()
        else:
            pemain = "O" if pemain == "X" else "X"

def cek_menang(p):
    for i in range(3):
        if all(buttons[i][j]["text"] == p for j in range(3)) or all(buttons[j][i]["text"] == p for j in range(3)):
            return True
    if buttons[0][0]["text"] == p and buttons[1][1]["text"] == p and buttons[2][2]["text"] == p:
        return True
    if buttons[0][2]["text"] == p and buttons[1][1]["text"] == p and buttons[2][0]["text"] == p:
        return True
    return False

def cek_seri():
    return all(buttons[i][j]["text"] != "" for i in range(3) for j in range(3))

def reset():
    global pemain
    pemain = "X"
    for i in range(3):
        for j in range(3):
            buttons[i][j]["text"] = ""
            buttons[i][j]["state"] = "normal"

frame_tengah = tk.Frame(window)
frame_tengah.pack()

buttons = []
for i in range(3):
    row = []
    for j in range(3):
        btn = tk.Button(frame_tengah, text="", width=6, height=3, font=("Arial", 24),
                        command=lambda r=i, c=j: klik(r, c))
        btn.grid(row=i, column=j, padx=5, pady=5)
        row.append(btn)
    buttons.append(row)

reset_btn = tk.Button(window, text="Reset", font=("Arial", 12), command=reset)
reset_btn.pack(pady=10)

window.mainloop()
