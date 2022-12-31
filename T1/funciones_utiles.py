def revisar_input_correcto(opciones_correctas: set):
    # Esta función se asegura de que el usuario ingresó una opción válida
    # Copiada (con cambios) de T0 propia
    input_jugador = input()
    if input_jugador in opciones_correctas:
        return int(input_jugador)
    else:
        print("Opción no válida, vuelva a intentarlo.")
        return "menu"


def salir_del_juego():
    print("Lamentamos verte ir!\nEsperamos verte pronto!")
