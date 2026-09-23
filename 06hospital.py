import tkinter as tk
from tkinter import messagebox

def calcular_diagnostico():
    try:
        nombre = entry_nombre.get()
        edad = int(entry_edad.get())
        peso = float(entry_peso.get())
        talla = float(entry_talla.get())
        oxigeno = entry_oxigeno.get()
        fc = entry_fc.get()
        pa = entry_pa.get()

        if not nombre:
            messagebox.showwarning("Advertencia", "Por favor ingresa el nombre del paciente.")
            return

        imc = peso / (talla ** 2)

        if imc < 18.5:
            estado_peso = "Bajo peso"
        elif 18.5 <= imc < 25:
            estado_peso = "Peso normal"
        elif 25 <= imc < 30:
            estado_peso = "Sobrepeso"
        else:
            estado_peso = "Obesidad (Alerta de peso elevado)"

        resultado = (
            f"--- DIAGNÓSTICO PRELIMINAR ---\n"
            f"Paciente: {nombre} | Edad: {edad} años\n"
            f"IMC: {imc:.2f} -> Estado: {estado_peso}\n\n"
            f"Signos Vitales:\n"
            f"• Oxígeno: {oxigeno} %\n"
            f"• Frecuencia Cardíaca (F.C.): {fc} lpm\n"
            f"• Presión Arterial (P.A.): {pa} mmHg"
        )
        
        lbl_resultado.config(text=resultado)

    except ValueError:
        messagebox.showerror("Error de datos", "Asegúrate de ingresar números válidos en peso, talla y edad.")
root = tk.Tk()
root.title("Diagnóstico")
root.geometry("450x550")

tk.Label(root, text="Nombre del Paciente:", font=("Arial", 10, "bold")).pack(pady=5)
entry_nombre = tk.Entry(root, width=30)
entry_nombre.pack()

tk.Label(root, text="Edad:", font=("Arial", 10, "bold")).pack(pady=5)
entry_edad = tk.Entry(root, width=30)
entry_edad.pack()

tk.Label(root, text="Peso (kg):", font=("Arial", 10, "bold")).pack(pady=5)
entry_peso = tk.Entry(root, width=30)
entry_peso.pack()

tk.Label(root, text="Altura", font=("Arial", 10, "bold")).pack(pady=5)
entry_talla = tk.Entry(root, width=30)
entry_talla.pack()

tk.Label(root, text="Saturación de Oxígeno (%):", font=("Arial", 10, "bold")).pack(pady=5)
entry_oxigeno = tk.Entry(root, width=30)
entry_oxigeno.pack()

tk.Label(root, text="Frecuencia Cardíaca:", font=("Arial", 10, "bold")).pack(pady=5)
entry_fc = tk.Entry(root, width=30)
entry_fc.pack()

tk.Label(root, text="Presión Arterial :", font=("Arial", 10, "bold")).pack(pady=5)
entry_pa = tk.Entry(root, width=30)
entry_pa.pack()

btn_calcular = tk.Button(root, text="Generar Diagnóstico", bg="green", fg="white", font=("Arial", 10, "bold"), command=calcular_diagnostico)
btn_calcular.pack(pady=15)

lbl_resultado = tk.Label(root, text="", justify="left", font=("Arial", 10), fg="blue")
lbl_resultado.pack(pady=5)

root.mainloop()