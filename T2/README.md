# Tarea 2: DCCruz vs Zombies :zombie::seedling::sunflower:

## Consideraciones generales :octocat:

<Descripción Mi tarea realiza la mayoría de las funciones, exceptuando el botón de pausa, el cual se puede activar con la letra p o con el botón, sin embargo, no se debe volver a apretar, sino que por default se pausa 10 segundos y no supe como pausarlo por un tiempo indeterminado (agradecería si me pudieran explicar cómo en el feedback ya que busqué muchas fuentes y no pude), funciona letra p para activarlo. Adicionalmente, implementé el bonus de drag and drop, la pala y los sonidos.>

### Cosas implementadas y no implementadas :white_check_mark: :x:
#### Ventanas: 39 pts (40%)
##### ✅ Ventana de Inicio
##### ✅ Ventana de Ranking	
##### ✅ Ventana principal
##### ✅ Ventana de juego	
##### ✅ Ventana post-ronda
#### Mecánicas de juego: 46 pts (47%)			
##### ✅ Plantas
##### ✅ Zombies
##### ✅ Escenarios		
##### ✅ Fin de ronda	
##### ✅ Fin de juego	
#### Interacción con el usuario: 22 pts (23%)
##### ✅ Clicks	
##### ✅ Animaciones
#### Cheatcodes: 8 pts (8%)
##### 🟠 Pausa
##### ✅ S + U + N
##### ✅ K + I + L
#### Archivos: 4 pts (4%)
##### ✅ Sprites
##### ✅ Parametros.py
##### ✅ K + I + L
#### Bonus: 9 décimas máximo
##### ✅ Crazy Cruz Dinámico
##### ✅ Pala
##### ✅ Drag and Drop Tienda
##### ❌ Música juego

## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py```. No se deben crear archivos adicionales


## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```PyQt5.QtWidgets```: ```QApplication / main.py . QLabel / anexo.py, logica_juego.py, ventana_juego_jardin.py . QMessageBox / ventana_inicio.py, ventana_principal.py, ventana_juego_jardin.py . ```
2. ```os```: ```path /parametros.py, logica_ranking.py``` 
3. ```PyQt5.QtCore```: ```QObject / anexo_2.py, anexo.py, logica_inicio.py, logica_juego.py, logica_ranking.py . QThread / guisantes.py . QTimer /guisantes.py . pyqtSignal / logica_inicio.py, logica_juego.py ventana_inicio.py, ventana_juego_jardin.py, ventana_post_ronda.py, ventana_principal.py, ventana_ranking.py . QTimer / logica_juego.py, plantas.py, guisantes.py, zombies.py . QMutex / logica_juego.py . QThread / plantas.py, guisantes.py, zombies.py .  Qt / ventana_juego_jardin.py```
4. ```PyQt5.QtGui```: ```QPixmap / logica_juego.py, ventana_juego_jardin.py``` 
5. ```random```: ```randint() / logica_juego.py, ventana_juego_jardin.py```
6. ```aparicion_zombies.py```: ```intervalo_aparicion() / logica_juego``` Venía en syllabus
7. ```PyQt5```: ```uic / ventana_inicio.py, ventana_juego_jardin.py, ventana_post_ronda.py, ventana_principal.py, ventana_ranking.py```  
8. ```time```: ```sleep() / logica_juego.py```
9. ```PyQt5```: ```QtMultimedia / logica_juego.py```

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```logica_juego.py```: Es el archivo más importante ya que modela el juego en sí, contiene a todas las funciones que administran las señales recibidas desde le frontend, en particular, ```crear_guisante_hielo()```, ```borrar_zombie()```, ```aparecer_soles()```, ```jugar()```, etc... Además cuenta con los anexos ```anexo.py```, ```anexo_2.py``` simplemente porque el archivo sino tendría una extensión demasiado grande y no respetaría pep8. Lo más relevante respecto a este es que contiene el flujo del juego, crea las clases de todos los objetos, así como manda señales a la ventana de juego para controlar los elementos gráficos. Además se encarga de mandar señales para abrir ventana de juego y ventana post-ronda. Dentro de anexo_2 se encuentra mi intento de hacer una pausa, a pesar de que me parece que funcionaba en mantener los niveles que estaban antes de la pausa, paré de seguir porque me iba a demorar mucho tiempo.
2. ```logica_ranking.py```: Hecha para <manejar el ranking de los jugadores y hacer los cálculos requeridos>
3. ```logica_inicio.py```: Revisa que el intento de log in cumpla las condiciones.
4. ```plantas.py```: Hecha para <crear clases de cada una de las plantas, modelar su funcionamineto y que cada una mande señales al frontend>
5. ```zombies.py```: Contiene a la clase ```zombie``` y su funcionamiento-
6. ```guisantes.py```: Contiene a la la clases de los guisantes verdes y guisantes de hielo, así como modela su funcionamiento.
7. ```ventana_inicio.py```: Modelada a través de qt designer <para dar la bienvenida al juego>
8. ```ventana_juego_jardin.py```: Modelada también en qt designer, contiene el principal layout, en el cual tanto los pastos como los elementos de la tienda son QLabel.
9. ```ventana_post_ronda.py```: Hecha para <mostrar un resumen de la ronda>, también fue modelada en qt designer.
10. ```ventana_principal.py```: Contiene la ventana principal que deja elegir un escenario.
11. ```ventana_ranking.py```: Muestra el ranking
12. ```parametros.py```: Contiene las posiciones de todas las qlabels del juego, parámetros necesarios para el juego, rutas de archivos, entre otros.

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. <Por simplicidad, consideré que los soles se generaban en la casilla siguiente al girasol, por ejemplo si el girasol está en A1, el girasol se genera en A2. Además, los soles generados en el escenario se posicionan en las mismas posiciones disponibles a las plantas/a> 
2. <Consideré que desde que se terminaba la ronda, pasarían 5 segundos hasta que aparezca la ventana post juego dado que el jugador querría ver el mensaje final/a>
3. <Los girasoles en el escenario de día salen cada 40 segundos./a>
4. <Cuando les queda la mitad de la vida, las patatas cambian a su posición 2 y luego cuando les queda un cuarto cambian a la 3, ya que me pareció lógico./a>
5. <Cambié la velocidad del zombie en parámetros ya que no me hacía mucho sentido el que fuera 5000 por milisegundo. La cambie a 6 para que cada vez que se actualice la posición del zombie runner, esta corresponda a un número entero (9). También modifiqué el daño de los guisantes a 10 y el de los zombies también a 10 para que el juego no sea tan lento./a>
6. <El intervalo de aparición de zombies lo multipliqué por 8000 (para pasar a milisegundos y establecer tiempo razonable) y lo pasé a int ya que parece razonable que los zombies aparezcan cada 6 segundos aproximadamente (ronda 1), no así 0,7 segundos. En el enunciado no se específica la unidad de tiempo en la que la función entrega el intervalo de aparición de zombies por lo que me parece válido, aparte sino se hace imposible un juego con una dificultad razonable./a>
7. <Para usar los cheatcodes, tan solo es necesario apretar las teclas requeridas de forma secuencial./a>
8. <Cabe mencionar que solo funciona el método drag and drop, y no la forma click-izquierdo, click izquierdo, esto es válido según el enunciado y ocurre ya que cuenta un evento release button al hacer el primer click izquierdo./a>
9. <En el caso del bonus de sonidos, se reproduce uno al azar de entre los 6 que se dan./a>
10. <Elegí la música 2 del juego ya que el enunciado no especificaba cual usar./a>


## Referencias de código externo :book:

Para realizar mi tarea saqué código de:
1. \<https://www.techwithtim.net/tutorials/pyqt5-tutorial/messageboxes/>: este permite crear pop ups para mostrar error a usuario
2. \<https://www.delftstack.com/es/tutorial/pyqt5/pyqt5-radiobutton>: Este me permitió usar radio buttons
3. AS3 2022-2 \<https://github.com/IIC2233/Syllabus/tree/master/Actividades/AS3>: Estructura general.
4. AS3 2022-1 \<https://github.com/IIC2233/Syllabus-2022-1/tree/main/Actividades/AS3>: Estructura general, particularmente al crear guisantes y que se movieran me fijé en como lo hacían los topos, keypress event para cheatcodes.
5. Actividad en clases syllabus \<https://github.com/IIC2233/Syllabus/tree/master/Clases/Interfaces%20Gr%C3%A1ficas>: Estructura general, uso de press en el mouse.
6. https://doc.qt.io/qtforpython para la documentación de pyqt5, por ejemplo los mouse move y released events.
7. https://stackoverflow.com/questions/62667514/how-to-play-sound-with-pyqt5-qtmultimedia para reproducir la música