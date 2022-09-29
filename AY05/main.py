import sys
from PyQt5.QtWidgets import QApplication
from frontend.ventana_login import VentanaLogin
from frontend.ventana_principal import VentanaPrincipal
from backend.logica_login import LogicaLogin

# Función para debuggear


def hook(type, value, traceback):
    print(type)
    print(traceback)
    sys.__excepthook__ = hook


# Se instancia la aplicación
app = QApplication([])

# Se instancian las clases
v_login = VentanaLogin()
v_principal = VentanaPrincipal()
logica = LogicaLogin()
# Se conectan las señales

v_login.senal_input = logica.senal_input
v_login.senal_principal = v_principal.senal_principal
logica.senal_bool = v_login.senal_bool
v_principal.senal_inicio = v_login.senal_inicio

# Se muestra la ventana de login
v_login.show()

sys.exit(app.exec_())
