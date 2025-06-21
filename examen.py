import tkinter as tk
from tkinter import messagebox
def mostrar_edad():
 
    messagebox.showinfo("mensaje", "Mi edad es 24")
def mostrar_vivienda():
    messagebox.showinfo("mensaje", "Mi vivienda es en Peru")

root = tk.Tk()
root.title("Examen I Parcial, Carlos Perez")


etiqueta_usuario = tk.Label(root, text="Danny Josue Moreno Maza:")
etiqueta_usuario.pack(pady=10)

boton = tk.Button(root, text="Edad", command=mostrar_edad)
boton.pack(side="right", padx=100) 

boton1 = tk.Button(root, text="Vivienda", command=mostrar_vivienda)
boton1.pack(side="left", padx=100) 

root.geometry("800x600")

 
root.configure(bg="lightblue")
 
root.mainloop()