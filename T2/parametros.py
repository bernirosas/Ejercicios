import os
# Los intervalos están en milisegundos
INTERVALO_DISPARO = 2000
INTERVALO_SOLES_GIRASOL = 20000
INTERVALO_TIEMPO_MORDIDA = 5000
INTERVALO_APARICION_SOLES = 40000
# El daño y la vida tienen las mismas medidas
DANO_PROYECTIL = 10
DANO_MORDIDA = 10
VIDA_PLANTA = 100
VIDA_ZOMBIE = 80
# Número de zombies por carril
N_ZOMBIES = 7
# Porcentaje de ralentización
RALENTIZAR_ZOMBIE = 0.25
# Soles iniciales por ronda
SOLES_INICIALES = 250
# Número de soles generados por planta
CANTIDAD_SOLES = 2
# Número de soles agregados a la cuenta por recolección
SOLES_POR_RECOLECCION = 50
# Número de soles agregados a la cuenta por Cheatcode
SOLES_EXTRA = 25
# Ponderadores de escenarios
PONDERADOR_NOCTURNO = 0.8
PONDERADOR_DIURNO = 0.9
# La velocidad del zombie en milisegundos
VELOCIDAD_ZOMBIE = 6
# Puntaje por eliminar zombie
PUNTAJE_ZOMBIE_DIURNO = 50
PUNTAJE_ZOMBIE_NOCTURNO = 100
# Costo por avanzar de ronda
COSTO_AVANZAR = 500
# Costo tiendas
COSTO_LANZAGUISANTE = 50
COSTO_LANZAGUISANTE_HIELO = 100
COSTO_GIRASOL = 50
COSTO_PAPA = 75
# Caracteres de nombre usuario
MIN_CARACTERES = 3
MAX_CARACTERES = 15

#  posiciones de cada planta en juego
x1_girasol = 20
y1_girasol = 20
x2_girasol = 20 + 71
y2_girasol = 20 + 81
ruta_girasol1 = os.path.join("sprites", "plantas", "girasol_1.png")
ruta_girasol2 = os.path.join("sprites", "plantas", "girasol_2.png")

x1_planta_verde = 20
x2_planta_verde = 20 + 71
y1_planta_verde = 140
y2_planta_verde = 140 + 81
ruta_planta_verde1 = os.path.join("sprites", "plantas", "lanzaguisantes_1.png")
ruta_planta_verde2 = os.path.join("sprites", "plantas", "lanzaguisantes_2.png")
ruta_planta_verde3 = os.path.join("sprites", "plantas", "lanzaguisantes_3.png")
ruta_guisante1 = os.path.join("sprites", "Elementos de juego",
                              "guisante_1.png")
ruta_guisante2 = os.path.join("sprites", "Elementos de juego",
                              "guisante_2.png")
ruta_guisante3 = os.path.join("sprites", "Elementos de juego",
                              "guisante_3.png")

x1_planta_azul = 20
x2_planta_azul = 20 + 71
y1_planta_azul = 260
y2_planta_azul = 260 + 81
ruta_planta_azul1 = (os.path
                     .join("sprites", "plantas", "lanzaguisantesHielo_1.png"))
ruta_planta_azul2 = (os.path
                     .join("sprites", "plantas", "lanzaguisantesHielo_2.png"))
ruta_planta_azul3 = (os.path
                     .join("sprites", "plantas", "lanzaguisantesHielo_3.png"))
ruta_guisante_hielo1 = os.path.join("sprites", "Elementos de juego",
                                    "guisanteHielo_1.png")
ruta_guisante_hielo2 = os.path.join("sprites", "Elementos de juego",
                                    "guisanteHielo_2.png")
ruta_guisante_hielo3 = os.path.join("sprites", "Elementos de juego",
                                    "guisanteHielo_3.png")

x1_papa = 20
x2_papa = 20 + 71
y1_papa = 380
y2_papa = 380 + 81
ruta_papa1 = os.path.join("sprites", "plantas", "papa_1.png")
ruta_papa2 = os.path.join("sprites", "plantas", "papa_2.png")
ruta_papa3 = os.path.join("sprites", "plantas", "papa_3.png")
ruta_sol = os.path.join("sprites", "Elementos de juego", "sol.png")
ruta_noche = os.path.join("sprites", "Fondos", "salidaNocturna.png")
ruta_sonido_1 = os.path.join("sonidos", "crazyCruz_1.wav")
ruta_sonido_2 = os.path.join("sonidos", "crazyCruz_2.wav")
ruta_sonido_3 = os.path.join("sonidos", "crazyCruz_3.wav")
ruta_sonido_4 = os.path.join("sonidos", "crazyCruz_4.wav")
ruta_sonido_5 = os.path.join("sonidos", "crazyCruz_5.wav")
ruta_sonido_6 = os.path.join("sonidos", "crazyCruz_6.wav")
ruta_musica = os.path.join("sonidos", "musica2.wav")

x1_pala = 20
x2_pala = 20 + 71
y1_pala = 510
y2_pala = 510 + 61

ruta_zombie_walker_1 = os.path.join("sprites", "Zombies", "Caminando",
                                    "zombieNicoWalker_1.png")
ruta_zombie_walker_2 = os.path.join("sprites", "Zombies", "Caminando",
                                    "zombieNicoWalker_2.png")
ruta_zombie_runner_1 = os.path.join("sprites", "Zombies", "Caminando",
                                    "zombieHernanRunner_1.png")
ruta_zombie_runner_2 = os.path.join("sprites", "Zombies", "Caminando",
                                    "zombieHernanRunner_2.png")
ruta_runner_comiendo_1 = os.path.join("sprites", "Zombies", "Comiendo",
                                      "zombieHernanComiendo_1.png")
ruta_runner_comiendo_2 = os.path.join("sprites", "Zombies", "Comiendo",
                                      "zombieHernanComiendo_2.png")
ruta_runner_comiendo_3 = os.path.join("sprites", "Zombies", "Comiendo",
                                      "zombieHernanComiendo_3.png")
ruta_walker_comiendo_1 = os.path.join("sprites", "Zombies", "Comiendo",
                                      "zombieNicoComiendo_1.png")
ruta_walker_comiendo_2 = os.path.join("sprites", "Zombies", "Comiendo",
                                      "zombieNicoComiendo_2.png")
ruta_walker_comiendo_3 = os.path.join("sprites", "Zombies", "Comiendo",
                                      "zombieNicoComiendo_3.png")

LIM_DERECHO = 985
LIM_IZQUIERDO = 210

x1_A1 = 305
x2_A1 = x1_A1 + 55
y1_A1 = 160
y2_A1 = y1_A1 + 80

x1_A2 = 360
x2_A2 = x1_A2 + 55
y1_A2 = 160
y2_A2 = y1_A2 + 80

x1_A3 = 415
x2_A3 = x1_A3 + 55
y1_A3 = 160
y2_A3 = y1_A3 + 80

x1_A4 = 470
x2_A4 = x1_A4 + 60
y1_A4 = 160
y2_A4 = y1_A4 + 80

x1_A5 = 530
x2_A5 = x1_A5 + 55
y1_A5 = 160
y2_A5 = y1_A5 + 80

x1_A6 = 585
x2_A6 = x1_A6 + 55
y1_A6 = 160
y2_A6 = y1_A6 + 80

x1_A7 = 640
x2_A7 = x1_A7 + 55
y1_A7 = 160
y2_A7 = y1_A7 + 80

x1_A8 = 695
x2_A8 = x1_A8 + 60
y1_A8 = 160
y2_A8 = y1_A8 + 80

x1_A9 = 755
x2_A9 = x1_A9 + 55
y1_A9 = 160
y2_A9 = y1_A9 + 80

x1_A10 = 810
x2_A10 = x1_A10 + 55
y1_A10 = 160
y2_A10 = y1_A10 + 80

x1_B1 = 305
x2_B1 = x1_B1 + 55
y1_B1 = 240
y2_B1 = y1_B1 + 81

x1_B2 = 360
x2_B2 = x1_B2 + 55
y1_B2 = 240
y2_B2 = y1_B2 + 81

x1_B3 = 415
x2_B3 = x1_B3 + 55
y1_B3 = 240
y2_B3 = y1_B3 + 81

x1_B4 = 470
x2_B4 = x1_B4 + 60
y1_B4 = 240
y2_B4 = y1_B4 + 81

x1_B5 = 530
x2_B5 = x1_B5 + 55
y1_B5 = 240
y2_B5 = y1_B5 + 81

x1_B6 = 585
x2_B6 = x1_B6 + 55
y1_B6 = 240
y2_B6 = y1_B6 + 81

x1_B7 = 640
x2_B7 = x1_B7 + 55
y1_B7 = 240
y2_B7 = y1_B7 + 81

x1_B8 = 695
x2_B8 = x1_B8 + 60
y1_B8 = 240
y2_B8 = y1_B8 + 81

x1_B9 = 755
x2_B9 = x1_B9 + 55
y1_B9 = 240
y2_B9 = y1_B9 + 81

x1_B10 = 810
x2_B10 = x1_B10 + 55
y1_B10 = 240
y2_B10 = y1_B10 + 81
