class Tarea:
    def __init__(self, id, descripcion, completada=False):
        self.id = id
        self.descripcion = descripcion
        self.completada = completada

    def marcar_completada(self):
        self.completada = True

    def __str__(self):
        estado = "[Hecho]" if self.completada else "[Pendiente]"
        return f"{estado} {self.descripcion}"