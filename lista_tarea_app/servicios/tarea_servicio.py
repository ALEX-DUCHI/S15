from modelos.tarea import Tarea

class TareaServicio:
    def __init__(self):
        self.tareas = []
        self.contador_id = 1

    def agregar_tarea(self, descripcion):
        if not descripcion.strip():
            return None
        tarea = Tarea(self.contador_id, descripcion)
        self.tareas.append(tarea)
        self.contador_id += 1
        return tarea

    def obtener_tareas(self):
        return self.tareas

    def completar_tarea(self, id):
        for tarea in self.tareas:
            if tarea.id == id:
                tarea.marcar_completada()
                return tarea
        return None

    def eliminar_tarea(self, id):
        for tarea in self.tareas:
            if tarea.id == id:
                self.tareas.remove(tarea)
                return True
        return False

