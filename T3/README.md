# Tarea 3: DCCard-Jitsu 🐧🥋


## Consideraciones generales :octocat:

<Gran parte de mi tarea la empecé de nuevo debido a cosas que no me funcionaban sin explicación, por esto mismo puede que el código este más desordenado de lo que habitualmente entregaría y hay cosas de la af3 que no me atreví a borrar por si todo me paraba de funcionar de nuevo. En general, a veces se cae sin razón aparente al ingresar un nuevo cliente (aparentemente manda un mensaje vacío), no estoy segura de porque pasa esto pero te pido paciencia, luego funciona todo super y no se cae después ;), si sabes porque ocurriría esto me encantaría que me lo dejaras en los comentarios. Dejé una muy importante nota sobre cómo correr mi tarea en consideraciones (la cuarta). >

### Cosas implementadas y no implementadas :white_check_mark: :x:

#### Networking: 26 pts (19%)
##### ✅ Protocolo	
##### ✅ Correcto uso de sockets		
##### ✅ Conexión	
##### ✅ Manejo de Clientes	
##### ✅ Desconexión Repentina
#### Arquitectura Cliente - Servidor: 31 pts (23%)			
##### ✅ Roles			
##### ✅ Consistencia		
##### ✅ Logs (de lo implementado)
#### Manejo de Bytes: 27 pts (20%)
##### ✅ Codificación			
##### ✅ Decodificación			
##### ✅ Encriptación		
##### ✅ Desencriptación	
##### ✅ Integración
#### Interfaz Gráfica: 27 pts (20%)	
##### ✅ Ventana inicio		
##### ✅ Sala de Espera			
##### ✅ Ventana de juego							
##### ✅ Ventana final
#### Reglas de DCCard-Jitsu: 17 pts (13%)
##### ✅ Inicio del juego			
##### ✅ Ronda				
##### ✅ Termino del juego
#### Archivos: 8 pts (6%)
##### ✅ Parámetros (JSON)		
##### ✅ Cartas.py	
##### ✅ Cripto.py
#### Bonus: 8 décimas máximo
##### ❌ Cheatcodes	
##### ❌ Bienestar	
##### ❌ Chat

## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py``` correspondiente la carpeta de servidor, en primer lugar, para luego correr ```main.py``` en la carpeta de cliente.


## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```os```
2. ```threading```
3. ```json```
4. ```PyQt5```
5. ```socket```
6. ```time```
7. ```sys```
8. ```random```

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```cliente.py```: Contiene a la clase ```cliente``` la cual se encarga de mandar y recibir mensajes, aunque en general los procesamientos correspondientes son realizados por interfaz.
2. ```interfaz.py```: Hecha para <ser el backend de las ventanas de juego>. 
3. ```servidor.py```: Encargado de manejar envío y recibo de mensajes mientras el resto se encarga lógica.
4. ```logica.py```: Se encarga de analizar todas las operaciones del servidor
5. El resto de las ventanas de la carpeta frontend de la carpeta cliente, estas se encargan de la parte visual.
6. ```cripto.py```: Entregada por syllabus, sirve para probar desencriptación y encriptación.
7. ```parametros.json```: Almacena los parámetros
8. ```dic_parametros.py```: Obtiene parámetros
Adicionalmente cartas.py es dado por syllabus y no modificado

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes: *4 es muy importante"

1. <El tiempo de la cuenta regresiva inicial debe estar en segundos, y valores enteros, por la forma en la que diseñe el timer que actualiza el tiempo/a> 
2. <No me quedó tan claro del enunciado si es que eran un mazo para ambos jugadores o uno para cada uno así que decidí que fuera uno para cada uno porque me hacía más sentido. Además leí en un issue que incluso las cartas ganadas iban al mazo de vuelta así que también lo incorporé/a>
3. <A veces se manda un mensaje en blanco desde cliente, de manera aleatoria, no sé si es normal pero funciona casi siempre y funciona el protocolo de desconexión del servidor, pido paciencia con que a veces hay que intentarlo un par de veces, luego de eso todo perfecto. Agradecería que también cerraras el servidor al haber errores ya que no probé el juego sin cerrarlo del todo./a>
4. <Para *correr* mi tarea es necesario primero correr servidor, luego un cliente, poner el nombre y luego correr el siguiente cliente y poner el nombre. Esto es debido a que copié la estructura de la AF3 y lo que ocurre es que de lo contrario dos usuarios tienen el mismo id (misma situación al terminar una partida). Había arreglado esto en versiones anteriores de mi tarea pero no me funcionaban cosas más importantes entonces lo devolví a su estado original ya que no podía descrubrir el error./a>
5. <A veces aparecen cartas repetidas, no sé bien porque pero usé la función get_penguins y efectivamente las "barajé" (desde cliente) por lo que supongo que está bien/a> 
6. <Si es que no hay ganador pero un usuario tiene más de de 15 cartas ganadas entonces el juego continua sin embargo no se ven las fichas ganadas sobre la 15./a> 

Para realizar mi tarea saqué código de:
1. \<https://github.com/IIC2233/Syllabus/tree/master/Actividades/AF3>: este me sirvió para \<modelar la estructura principal> de la tarea, sobre todo la parte de servidor-cliente. También utilicé código copmartido por mi profesora  de la solución de esta misma actividad.
2. \<https://www.techwithtim.net/tutorials/pyqt5-tutorial/messageboxes/>: este permite crear pop ups para mostrar error a usuario.Función específica la copié de mi tarea 2.
3. \<https://github.com/IIC2233/Syllabus/tree/master/Ayudant%C3%ADas/AY08>: Para la encriptación y desencriptación