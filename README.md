# IMPLEMENTACIÓN DE CI/CD CON GITHUB ACTIONS
![imagen](https://miro.medium.com/v2/1*JDKxmDwriUdVxUSyMwaFyA.png)
## INTRODUCCIÓN
Para llevar a cabo el proyecto sobre la implementación de **CI/CD**, que es una herramienta de configuración del software (SCM por sus siglas en inglés), utilizaremos este repositorio, mostrando mediante los commits, como partiendo de un código "malo" es decir mal implementado, mal estructurado y hasta con partes sin usar para luego aplicar, primeramente, **CI** para ejecutar test y poder construir adecuadamente la porción de código que queramos pushear al proyecto obtendremos la primera parte de esta herramienta para la integración y despliegue.  
 
Luego para poder generar los despliegues en la rama correspondiente (en este caso la main) crearemos, a traves de, Github Actions el despliegue continuo **CD** configurando los parámetros dentro del archivo .yaml

## Desarrollo práctico

### CI/CD

Para demostrar de forma sencilla decidimos realizar una calculadora escrita en Python. Entonces decidimos desarrollarlo en dos partes: 
- **CI** (Integración Continua): Partimos de un código mal implementado, en el que los métodos de la clase calculadora no cumplían su propósito de manera correcta, por ejemplo, las operaciones devolvían valores erróneos. Luego desarrollamos los tests que hemos considerado necesarios para los casos borde acordes a cada operación. 
Una vez realizado el código de partida, donde previamente se probó que los test no pasaran utilizando _pytest_. A partir de aquí, comenzó la implementación del GitHub Action, el cual facilita la Integración Continua.  
Una vez configurado el GitHub Actions, a la hora de realizar un commit donde se implemente
algún cambio en la funcionalidad de algún módulo del proyecto, se disparará de manera automática
la creación de un contenedor en la nube con las especificaciones y _jobs_ establecidos en el 
proyecto, donde para este caso simplemente se utiliza las librerías _pytest_, para la ejecución de los tests, y _ruff_, para el _linting _ y formateo del código.  

- **CD** (Despliegue Continuo): Una vez realizado lo anterior, configuramos el GitHub Action 
para implementar, con Docker, el Despliegue Continuo. Para ello agregamos en el archivo .yaml
los jobs de login-action y build-push-action de docker, los cuales al detectar el push, automáticamente compilan una imagen Docker con las librerías necesarias para el funcionamiento de la aplicación con tan solo ejecutar el comando que se genera en la sección de packages del repositorio. Obteniendo así siempre la última imágen más actualizada del proyecto.


## Beneficios de implementar la técnica 

## Desafios y consideraciones 

## Conclusión 

## Referencias 