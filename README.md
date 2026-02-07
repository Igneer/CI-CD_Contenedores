# IMPLEMENTACIÓN DE CI/CD CON GITHUB ACTIONS
![imagen](https://miro.medium.com/v2/1*JDKxmDwriUdVxUSyMwaFyA.png)
## INTRODUCCIÓN
Para llevar a cabo el proyecto sobre la implementación de **CI/CD**, que es una herramienta de configuración del software (SCM por sus siglas en inglés), utilizaremos este repositorio, mostrando mediante los commits, como partiendo de un código "malo" es decir mal implementado, mal estructurado y hasta con partes sin usar para luego aplicar, primeramente, **CI** para ejecutar test y poder construir adecuadamente la porción de código que queramos pushear al proyecto obtendremos la primera parte de esta herramienta para la integración y despliegue.  
 
Luego para poder generar los despliegues en la rama correspondiente (en este caso la main) crearemos, a traves de, Github Actions el despliegue continuo **CD** configurando los parámetros dentro del archivo .yaml

## Pasos para implementar  el proyecto de manera local 

<!-- 
Una vez realizado los cambios que "rompen" la funcionalidad correcta hay que actualizar la imagen de Docker creada para que se vean reflejados los cambios con el siguiente comando:
docker build -t mi-calculadora:latest . -->
Para poder utilizar el proyecto de manera local es primero necesario tener instalado la herramienta necesaria para poder utilizarlo, la cual es  Docker.


Mediante los siguiente comando se mostrará cómo debería ser un proceso normal para utilizarlo, estos comando pueden ser utilizados tanto en Bash como en PowerShell:
1. **Clonar el repositorio:**


1. **Construir la imagen en Docker:**  
 Este paso sirve para generar el espacio donde se estará corriendo el proyecto.    
``docker build -t mi-calculadora .``
1. **Ejecutar un contenedor temporal de la imagen buildeada en Docker:**
Con el siguiente comando se realizarán las pruebas y se detectará tanto errores de implementación como de linteo.    
 ``docker run --rm mi-calculadora ruff check . && docker run --rm mi-calculadora pytest test-calculadora.p ``
1. **Actualizar la imagen de Docker:**   
En caso de encontrar un error, luego de corregirlo se puede reconstruir la imagen de Docker con el siguiente comando.   
``docker build -t mi-calculadora:latest .``




## Desarrollo práctico


### CI/CD


Para demostrar de forma sencilla decidimos realizar una calculadora escrita en Python. Entonces decidimos desarrollarlo en dos partes:
- **CI** (Integración Continua): Partimos de un código mal implementado, en el que los métodos de la clase calculadora no cumplían su propósito de manera correcta, por ejemplo, las operaciones devuelven valores erróneos. Luego desarrollamos los tests que hemos considerado necesarios para los casos borde acordes a cada operación.
Una vez realizado el código de partida, donde previamente se probó que los test no pasarán utilizando _pytest_. A partir de aquí, comenzó la implementación del GitHub Action, el cual facilita la Integración Continua.  
Una vez configurado el GitHub Actions, a la hora de realizar un commit donde se implemente
algún cambio en la funcionalidad de algún módulo del proyecto, se disparará de manera automática
la creación de un contenedor en la nube con las especificaciones y _jobs_ establecidos en el proyecto, donde para este caso simplemente se utiliza las librerías _pytest_, para la ejecución de los tests, y _ruff_, para el _linting _ y formateo del código.  


- **CD** (Despliegue Continuo): Una vez realizado lo anterior, configuramos el GitHub Action
para implementar, con Docker, el Despliegue Continuo. Para ello agregamos en el archivo .yaml
los jobs de login-action y build-push-action de docker, los cuales al detectar el push, automáticamente compilan una imagen Docker con las librerías necesarias para el funcionamiento de la aplicación con tan solo ejecutar el comando que se genera en la sección de packages del repositorio. Obteniendo así siempre la última imágen más actualizada del proyecto.




## Beneficios de implementar la técnica


A través de la implementación de las herramientas utilizadas para aplicar **CI**, que para este proyecto se conocen como Github Actions, él mismo se beneficia de características como, el testeo automático de módulos/cambios implementados en cada commit que se realice y se pusheen. Permitiendo así detecciones de errores de una manera visible para todo colaborador dentro del proyecto, para poder actuar de manera rápida en las soluciones de los mismos. Obteniendo de esta manera un código de cierta manera controlado bajo posibles políticas de una empresa o equipo de trabajo como así también una robustez y fiabilidad en el mismo.  
Para la aplicación de **CD**, despliegue continuo, utilizamos la misma herramienta de Github Actions las cuales brindan como beneficio al proyecto, en conjunto con las de **CI**, mantener un despliegue en producción reciente y funcional de manera automatica, disparandose cuando se detecta algún cambio en el repositorio del proyecto siempre y cuando la actualización recibida sea testeada de manera correcta con las herramientas de **CI** previamente configuradas.


## Desafíos y consideraciones

Para dar un uso correcto a la técnica **CI** tiene como desafío el realizar el uso correcto de los test para que se pueda tanto como verificar como validar que se llegue a una implementación correcta del proyecto. Pero nada te puede asegurar que se cumplan las condiciones  que se desean, además que conlleva un extenso periodo de tiempo el diseñar e implementar los test necesarios.  
Otro tema a tener en cuenta es que los _jobs_ se realizen en el archivo de formato .yaml se ejecuten en un orden adecuado, por ejemplo, que se asegure de probar todo antes de realizar la build de la imagen de docker con la última versión del proyecto.   
Una consideración a tener en cuenta es asegura que los test que se realizan en el entorno del desarrollador se un entorno de mismas características en el entorno de despliegue.  

## Conclusión

Luego de realizar este proyecto nos llevamos como aprendizaje la importancia y utilidad de aplicar la integración continua para poder mantener una portabilidad y firmeza en el proyecto mientras se está llevando a cabo sosteniendo también el cumplimiento de las políticas dentro del equipo de trabajo.  
Del despliegue podemos rescatar la utilidad de poder automatizar la construcción de entregables versionados creados en docker, que nos permite ahorrar tiempo que sería utilizado para crear dichos desplegables.  
Por lo tanto, hemos demostrado que la combinación de SCM  y CI/CD  junto con la tecnología de contenedores, transforma radicalmente la forma de construir software sólido para cualquier proyecto de ingeniería de software moderno que busque escalabilidad y robustez.
  
## Referencias

- [GitHubAction](https://docs.github.com/es/actions/tutorials/build-and-test-code/python)  
- [Login action para Docker](https://github.com/docker/login-action)
- [Despliege en Docker](https://github.com/docker/build-push-action)