
## **~ UD 1-2 Generación de procesos en Python**

<br/>

### ***Actividad 1***

<br/>

#### **- | Gestión de ramas |**
<br/>

Creo la rama **development** donde iremos añadiendo las nuevas funcionalidades creadas en las rama **pid**, y finalmente mergearlo todo al **main**.

<br/>

#### **- | Desarrollo de las ramas |**

<br/>

> pid

- Desarrollaremos las funciones **<code>father()</code>** y **<code>children()</code>**, donde generaremos los procesos padres e hijos.

<br/>

- - **<code>father()</code>** : En esta función preguntaremos al usuario cuantos procesos quiere que generemos, a partir de eso generaremos el número de procesos indicado mediante el uso de **<code>os.fork()</code>** para la creación de cada proceso. Si la salida de este el igual a 0 significará que nos encontramos en el proceso hijo por lo que llamaremos a la función **<code>children()</code>**, sino mostraremos el PID padre y el PID hijo.

<br/>

- - **<code>children()</code>** : Lo que haremos aquí será mostrar el PID del hijo y luego, mediante la función **<code>sleep()</code>** de la clase **<code>time</code>**, le diremos al programa que espere 5 segundos, para que después que transcurra ese tiempo matemos al proceso usando **<code>os._exit(0)</code>** y lo mostremos por pantalla.

<br/>

#### **- | Conclusión del proyecto |**

<br/>

En mi opinión, en este proyecto hemos aprendido como crear procesos en pyhton y a matarlos cuando nosotros queramos, además del uso de diversos modulos como **<code>os</code>**  y **<code>time</code>**.