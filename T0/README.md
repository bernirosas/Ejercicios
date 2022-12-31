
# Tarea 0: Star Advanced 🚀🌌

La tarea a continuación presenta 5 archivos ejecutables ".py" que serán explicados, además del archivo ".txt" puntajes (que puede vaciarse, aunque para comodidad del corregidor dejé varias partidas del juego para uso de función ranking), la carpeta "partidas" en la que también dejé varias partidas jugadas ".txt" que pueden borrarse.

Abierto desde la carpeta "TO", desde donde se debe ejecutar, "archivo.py" ejecuta de manera correcta el juego "Star advanced". Además, se realizó el bonus.
#### Programación Orientada a Objetos (18pts) (22%%)
##### ✅ Menú de Inicio
##### ✅ Funcionalidades		
##### ✅ Puntajes
#### Flujo del Juego (30pts) (36%) 
##### ✅ Menú de Juego
##### ✅ Tablero		
##### ✅ Bestias	
##### ✅ Guardado de partida		
#### Término del Juego 14pts (17%)
##### ✅ Fin del juego	
##### ✅ Puntajes	
#### Genera: 15 pts (15%)
##### ✅ Menús
##### ✅ Parámetros
##### ✅ PEP-8
#### Bonus: 3 décimas
##### ✅
## Ejecución :computer:

El módulo principal de la tarea a ejecutar es  ```archivo.py```. Además se debe crear los siguientes archivos y directorios adicionales:
carpeta ```partidas``` en ```T0```
```puntajes.txt``` en ```T0```
Ambos ya fueron creadas, pero pueden vaciarse a comodidad del corregidor.

La lista de librerías externas que utilicé fue la siguiente:

1. ```os```: ```path(), isfile() / manejo_partidas.py, archivo.py```
2. ```math```: ```ceil() / manejo_partidas.py, validar.py``` 
3. ```string```: ```ascii_lowercase / validar.py``` 
4. ```random```: ```randint() / manejo_partidas.py```

Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```manejo_partidas.py```: Contiene a guardar, calcular_y_guardar_puntaje, cargar_partida, crear_nuevo_tablero,
                            terminado_func y ver_ranking. Tal como dice su nombre, su función general es 
                            administrar toda la información relacionada con la creación y continuación de una partida.
2. ```validar.py```: Hecha para validar numerosos inputs relacionados con el flujo del juego, principalmente. Incluye  coordenada_valida, revisar_input_correcto, validar_bestias_cercanas, verificar_ganar y descubrimiento_de_casillas.

3. ```tablero.py```: Permite imprimir el tablero de manera correcta. Este módulo fue entregado por syllabus.

4. ```parametros.py```: Parámetros entregados en syllabus importados para las fórmulas.


No utilicé fuentes externas al curso, aunque si me basé en AF1 para la función que permite ver si el input es válido y para la organización general de la tarea.

Los supuestos que realicé durante la tarea son los siguientes:

1. Luego de que un jugador pierda o gane, este no puede seguir jugando en la misma partida, para ello, al perder o al ganar, se agrega un línea al archivo en "partidas" del jugador que tiene el nombre de su usuario que luego se lee al querer cargar partida y obliga al jugador a partir una nueva partida. Al ganar o perder, el guardado es automático.

2. Al guardar, el archivo con el nombre del usuario ".txt" guarda ancho, largo, tanto el tablero oculto (con sus filas unidas por -) como el tablero del jugador para así asegurar legibilidad a la hora de revisar el archivo tanto para el programador como para luego el programa que puede revertir el proceso fácilmente para cargar la partida previa del jugador. Un archivo de un usuario cualquiera (en este caso angelica.txt) contiene la siguiente información:
# Tablero actual jugador:
# Ancho:5
# Largo:6
#### - - - -
#### - - - - 
#### - - - -
#### - - - - 
#### - - - -
#### - - - - 
# Tablero oculto de bestias: 
#### - - - -
#### - - - -N 
#### -N-N- -
#### - - - - 
#### - - -N-
#### - -N- - 
 Nota: Para comprender exactamente la forma de guardado, es necesario ver uno de los archivos dentro de la carpeta "partidas". 
 Notar que en caso de haber terminado la jugada, entonces se incluye una línea adicional "partida terminada" que permite regular intentos de trampa o errores humanos. En caso de haber descubierto un nuevo sector, en el tablero de jugador se podría ver la cantidad de bestias cercanas a la celda, revisar ejemplo en carpeta "partidas".


3. Los jugadores solo pueden elegir carácteres alfanúmericos a la hora de escoger su nombre de usuario, esto para asegurar que no existan tantos problemas.

4. De la misma forma, tal y como se le explica al jugador, se deben ingresar las coordenadas de forma [Letra:numero], para así checkear de manera más fácil que la coordenada sea válida.
