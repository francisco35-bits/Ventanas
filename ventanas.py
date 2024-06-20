from tkinter import *

ventana_principal = Tk()
ventana_principal.title("Identificate")
ventana_principal.minsize(width=300, height=400)
ventana_principal.config(padx=35, pady=35)

etiqueta1 = Label(text="Escribe Tu Nombre Completo Pa", font=("Arial", 14))
etiqueta1.grid(column=0, row=1)

Caja_Texto1 = Entry(width=20, font=("Arial",14))
Caja_Texto1.grid(column=0, row=2)

etiqueta2 = Label(text="Escribe Tu Contraseña Pa", font=("Arial", 14))
etiqueta2.grid(column=0, row=3)

Caja_Texto2 = Entry(width=20, font=("Arial",14), show="*")
Caja_Texto2.grid(column=0, row=4)

boton1 = Button(text="Aceptar", font=("Arial", 14))
boton1.grid(column=0, row=6)


ventana_principal.mainloop()