from PyQt5.QtWidgets import QApplication
from backend.logica_juego import LogicaJuego
from backend.logica_ranking import LogicaRanking
from frontend.ventana_inicio import VentanaInicio
import sys
from backend.logica_inicio import Logica_inicio
from frontend.ventana_juego_jardin import VentanaJuegoJardin
from frontend.ventana_post_ronda import VentanaPostRonda
from frontend.ventana_principal import VentanaPrincipal
from frontend.ventana_ranking import VentanaRanking
from backend.anexo import FuncionesVarias
from backend.anexo_2 import FuncionesVarias2
# Codigo sacado de actividad resuelta en clase
if __name__ == '__main__':
    def hook(type, value, traceback):
        print(type)
        print(traceback)
    sys.__excepthook__ = hook

    app = QApplication([])
    ventana_inicio = VentanaInicio()
    logica_inicio = Logica_inicio()
    ventana_principal = VentanaPrincipal()
    ventana_juego_jardin = VentanaJuegoJardin()
    ventana_ranking = VentanaRanking()
    logica_ranking = LogicaRanking()
    logica_juego = LogicaJuego(ventana_juego_jardin)
    funciones = FuncionesVarias(logica_juego)
    funciones_2 = FuncionesVarias2(logica_juego)
    ventana_post_juego = VentanaPostRonda()
    ventana_post_juego.senal_salir.connect(ventana_inicio.abrir)
    ventana_post_juego.senal_salir.connect(logica_juego.guardar_puntaje)
    logica_juego.funciones = funciones  # funciones que ocupaban muchas líneas
    logica_juego.funciones_2 = funciones_2
    logica_juego.senal_pop_up.connect(ventana_juego_jardin.crear_pop_up)
    #  conexión señales, tal y como en AS3
    ventana_inicio.senal_log_in.connect(logica_inicio.revisar_log_in)
    logica_inicio.senal_resultado_log_in.connect(ventana_inicio.log_in)
    ventana_inicio.senal_salir.connect(app.exit)
    ventana_juego_jardin.senal_salir.connect(logica_juego.ganaron_zombies)
    ventana_inicio.senal_abrir_ranking.connect(ventana_ranking.abrir)
    ventana_ranking.senal_volver.connect(ventana_inicio.abrir)
    ventana_ranking.senal_actualizar_ranking.connect(logica_ranking.actualizar)
    (logica_ranking.senal_actualizar_labels.
     connect(ventana_ranking.actualizar_labels))
    ventana_inicio.senal_abir_principal.connect(ventana_principal.
                                                mostrar_principal)
    ventana_principal.senal_abrir_juego.connect(logica_juego.escenificar)
    logica_juego.senal_jardin.connect(ventana_juego_jardin.abrir)
    (ventana_juego_jardin.
     senal_click_pantalla.connect(logica_juego.checkear_posicion_planta))
    (logica_juego.
     resultado_planta.connect(ventana_juego_jardin.validar_planta_elegida))
    (ventana_juego_jardin.
     senal_click_lugar.connect(logica_juego.checkear_posicion_lugar))
    (logica_juego.senal_cambiar_label.connect(ventana_juego_jardin.
     actualizar_posicion_planta_1))
    (logica_juego.senal_cambiar_label2.connect(ventana_juego_jardin.
     actualizar_posicion_planta_2))
    ventana_juego_jardin.senal_boton_iniciar.connect(logica_juego.jugar)
    logica_juego.senal_agregar_sol.connect(ventana_juego_jardin.colocar_sol)
    ventana_juego_jardin.senal_recoger_sol.connect(logica_juego.recoger_sol)
    (logica_juego.senal_actualizar_datos.connect(ventana_juego_jardin.
     actualizar_datos))
    (logica_juego.senal_planta_verde.connect(ventana_juego_jardin.
     actualizar_planta))
    (logica_juego.senal_actualizar_guis.connect(ventana_juego_jardin.
     actualizar_guisante))
    logica_juego.senal_inicial.connect(ventana_juego_jardin.crear_label_guis)
    logica_juego.senal_inicial_hielo.connect(ventana_juego_jardin.
                                             crear_label_hielo)
    ventana_juego_jardin.senal_label_guis.connect(logica_juego.recibir_label)
    ventana_juego_jardin.senal_label_hielo.connect(logica_juego.
                                                   recibir_label_hielo)
    logica_juego.senal_papa.connect(ventana_juego_jardin.actualizar_planta)
    ventana_juego_jardin.senal_sol_colocado.connect(logica_juego.recibir_sol)
    logica_juego.senal_inicial_zombie.connect(ventana_juego_jardin.
                                              senal_inicial_zombie)
    ventana_juego_jardin.senal_label_zombies.connect(logica_juego.crear_zombie)
    logica_juego.senal_mover_zombie.connect(ventana_juego_jardin.
                                            actualizar_posicion_zombie)
    logica_juego.senal_zombie.connect(ventana_juego_jardin.actualizar_zombie)
    logica_juego.senal_ventana_post_ronda.connect(ventana_post_juego.abrir)
    logica_juego.senal_ventana_post_ronda.connect(ventana_juego_jardin.hide)
    (logica_juego.senal_termino_ronda.
     connect(ventana_juego_jardin.actualizar_interfaz_post_ronda))
    ventana_post_juego.senal_pasar_ronda.connect(logica_juego.pasar_ronda)
    ventana_post_juego.senal_pasar_ronda.connect(ventana_juego_jardin.show)
    ventana_juego_jardin.senal_pausa.connect(logica_juego.pausar)
    ventana_juego_jardin.senal_avanzar.connect(logica_juego.avanzar)
    (ventana_juego_jardin.senal_cheatcode_sun.
     connect(logica_juego.cheatcode_sun))
    (ventana_juego_jardin.senal_cheatcode_kil.
     connect(logica_juego.cheatcode_kil))
    sys.exit(app.exec())
