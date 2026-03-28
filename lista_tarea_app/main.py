from servicios.tarea_servicio import TareaServicio
from ui.app_tkinter import LoginWindow, AppTkinter

if __name__ == "__main__":
    servicio = TareaServicio()

    login = LoginWindow()
    acceso = login.run()

    if acceso:
        app = AppTkinter(servicio)
        app.run()