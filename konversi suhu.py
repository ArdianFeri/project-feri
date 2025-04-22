import tkinter as tk

def konversi():
    try:
        suhu = float(isisuhu.get())  # Ambil angka dari input
        f = (suhu * 9/5) + 32          # Konversi ke Fahrenheit
        k = suhu + 273             # Konversi ke Kelvin

        # Tampilkan hasil
        labelHasil.config(text=f"{f:.2f} °F\n{k:.2f} K" ,bg="white")
    except:
        labelHasil.config(text="Error (Cuma bisa pake angka)", bg="grey")   



window = tk.Tk()
window.title("Konversi Suhu")
window.geometry("400x400")
window.configure(background="Turquoise")


frame = tk.Frame(window, bg="pink", padx=50, pady=40)
frame.pack(pady=20)

label = tk.Label(frame, text="Masukkan Suhu (Celsius)" ,bg= "pink")
label.pack()

isisuhu = tk.Entry(frame, width=20, font=("Arial", 12))
isisuhu.pack()


frame2 = tk.Frame(window , bg="white" , padx=100 , pady=30)
frame2.pack()

labelHasil=tk.Label(frame2, text="Hasil" , bg="white" , font=("Arial", 11) )
labelHasil.pack()

button = tk.Button(window, text="Konversi" , border= 2 , bg="pink" , font=("Arial",12, ), width=20, command=konversi)

button.pack(
    pady=30 
)


window.mainloop()

   