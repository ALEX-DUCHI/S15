import tkinter as tk
from tkinter import ttk, messagebox

# ================= LOGIN =================
class LoginWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Login")
        self.root.geometry("300x200")

        self.usuario_correcto = "admin"
        self.password_correcto = "1234"
        self.acceso = False

        tk.Label(self.root, text="Usuario").pack(pady=5)
        self.entry_user = tk.Entry(self.root)
        self.entry_user.pack()

        tk.Label(self.root, text="Contraseña").pack(pady=5)
        self.entry_pass = tk.Entry(self.root, show="*")
        self.entry_pass.pack()

        self.btn_login = tk.Button(self.root, text="Ingresar", command=self.validar)
        self.btn_login.pack(pady=10)

        self.root.bind("<Return>", lambda e: self.validar())
    def validar(self):
        user = self.entry_user.get()
        pwd = self.entry_pass.get()

        if user == self.usuario_correcto and pwd == self.password_correcto:
            self.acceso = True
            self.root.destroy()
        else:
            messagebox.showerror("Error", "Credenciales incorrectas")

    def run(self):
        self.root.mainloop()
        return self.acceso
# ================= APP =================
class AppTkinter:
    def __init__(self, servicio):
        self.servicio = servicio

        self.root = tk.Tk()
        self.root.title("Lista de Tareas")
        self.root.geometry("500x400")

        self.frame_top = tk.Frame(self.root)
        self.frame_top.pack(pady=10)

        self.entry = tk.Entry(self.frame_top, width=40)
        self.entry.pack(side=tk.LEFT, padx=5)

        self.btn_add = tk.Button(self.frame_top, text="Añadir Tarea", command=self.agregar_tarea)
        self.btn_add.pack(side=tk.LEFT)

        self.tree = ttk.Treeview(self.root, columns=("ID", "Tarea"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Tarea", text="Descripción")
        self.tree.pack(fill=tk.BOTH, expand=True, pady=10)

        self.frame_bottom = tk.Frame(self.root)
        self.frame_bottom.pack(pady=10)

        self.btn_complete = tk.Button(self.frame_bottom, text="Marcar Completada", command=self.completar_tarea)
        self.btn_complete.pack(side=tk.LEFT, padx=5)
        self.btn_delete = tk.Button(self.frame_bottom, text="Eliminar", command=self.eliminar_tarea)
        self.btn_delete.pack(side=tk.LEFT, padx=5)

        self.entry.bind("<Return>", lambda event: self.agregar_tarea())
        self.tree.bind("<Double-1>", lambda event: self.completar_tarea())

    def agregar_tarea(self):
        texto = self.entry.get()
        tarea = self.servicio.agregar_tarea(texto)
        if tarea:
            self.tree.insert("", tk.END, iid=tarea.id, values=(tarea.id, tarea.descripcion))
            self.entry.delete(0, tk.END)

    def completar_tarea(self):
        seleccion = self.tree.selection()
        if not seleccion:
            return
        item_id = int(seleccion[0])
        tarea = self.servicio.completar_tarea(item_id)
        if tarea:
            self.tree.item(item_id, values=(tarea.id, f"[Hecho] {tarea.descripcion}"))
            self.tree.tag_configure("completado", foreground="gray", background="yellow")
            self.tree.item(item_id, tags=("completado",))

    def eliminar_tarea(self):
        seleccion = self.tree.selection()
        if not seleccion:
            return
        item_id = int(seleccion[0])
        eliminado = self.servicio.eliminar_tarea(item_id)
        if eliminado:
            self.tree.delete(item_id)

    def run(self):
        self.root.mainloop()
