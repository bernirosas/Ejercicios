
## Liga programon 🏆
Liga programon contiene una lista de entrenadores, instancias de Entrenador creados en el menú principal (no se
 en liga progrramón). Se creo un atributo de ```entrenador_elegido``` y una lista ```siguen``` que contiene los entrenadores que no han perdido. 

## Entrenador 🏃‍♂️
Luego, en el init de la clase ```entrenador```, se crean los programones a partir de una
función que los carga y los vuelve instancias de clases (a partir de los nombres que contiene el entrenador). De la misma forma, se crean los objetos. Entrenador entonces contiene una lista de instancias de programones y objetos creados dentro de su init.

## Objetos y programones
Además programon contiene 3 subclases para cada uno de sus tipos (```planta```, ```fuego``` y ```agua```), y objeto tiene también 3 subclases(```baya```, ```pocion``` y ```caramelo```), una de ellas (```caramelo```) hereda de las otras dos (```baya```y ```pocion```).

Tanto programon como objeto son clases abstractas que obligan a sus subclases a
sobreescribir ciertos métodos para asegurarse de no tener problemas. También se establecen
properties para asegurarse de mantener los rangos requeridos en la tarea.
