# Tarea 1: DCCampeonato 🏃‍♂️🏆

## Consideraciones generales :octocat:

<La ejecución de la tarea es limpia, y, a mi parecer, libre de errores. Realicé el bonus de los csv dinámicos.

### Cosas implementadas y no implementadas :white_check_mark: :x:

#### Programación Orientada a Objetos (18pts) (22%%)
##### ✅ Diagrama
##### ✅ Definición de clases, atributos, métodos y properties		
##### ✅ Relaciones entre clases
#### Preparación programa: 11 pts (7%)			
##### ✅ Creación de partidas
#### Entidades: 28 pts (19%)
##### ✅ Programón
##### ✅ Entrenador		
##### ✅ Liga	
##### ✅ Objetos		
#### Interacción Usuario-Programa 57 pts (38%)
##### ✅ General	
##### ✅ Menú de Inicio
##### ✅ Menú Entrenador
##### ✅ Menu Entrenamiento
##### ✅ Simulación ronda campeonato
##### ✅ Ver estado del campeonato
##### ✅ Menú crear objeto
##### ✅ Menú utilizar objeto
##### ✅ Ver estado del entrenador
##### ✅ Robustez
#### Manejo de archivos: 12 pts (8%)
##### ✅ Archivos CSV
##### ✅ Parámetros
#### Bonus: 5 décimas
##### ❌ Mega Evolución
##### ✅ CSV dinámico

## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```menus.py```. No se deben crear directorios ni archivos adicionales. La tarea se ejecuta desde carpeta ```T1```.


## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```collections```: ```namedtuple / cargar_objetos_y_programones.py, cargar.py```
2. ```random```: ```random(), choice() / entrenador.py, liga_programon.py, menus.py, objetos.py, programon.py`` 
3.  ```abc```: ```ABC, abstractmethod / objetos.py, programon.py`` 

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```menus.py```: Las funciones más importantes que contiene son ```menu_inicio```, ```menu_entrenador```, ```menu_usar_objeto```.
2. ```liga_programon.py```: Hecha para <diseñar clase que contiene el resto de los componentes del juego>
3. ```funciones_utiles.py```: que contiene ciertas funciones transversales a través del juego.
4. ```parametros.py```: que contiene el valor de parámeteros utilizados en el juego.
5. ```objetos.py```: Hecha para <diseñar clase objeto, baya, pocion y caramelos(las últimas tres heredan de objetos y la última hereda tanto de pocion como baya) >
6. ```entrenador.py```: Hecha para <diseñar clase Entrenador que contiene a la lista de programones y de objetos.
7. ```cargar.py```: Contiene función que devuelve lista de entrenadores.
8. ```cargar_objetos_y_programones.py```: Contiene diversas funciones para cargar objetos tanto al usarlos como al crearlos y para programones. Sirve en la creación  de instancias.
9. ```programon.py```: Modela clase programon y sus subclases correspondientes.



## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. Juego termina cuando pierde el jugador, ya que sino no tiene sentido continuar el campeonato. 
2. Si se utiliza un objeto que por ejemplo aumenta la vida, cuando la vida ya es máxima, entonces se avisa en consola wue ya está al máximo, y aunque no aumente el valor sale que "paso de x a y" a pesar de que no exista un cambio, por completitud.
3. Al ganar o perder el juego, se pregunta si se quiere volver a jugar o salir (el enunciado aparecen dos cosas distintas (liga programon v/s flujo).

## Referencias de código externo :book:
No usé código externo para la realización de la tarea.