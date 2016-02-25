
# coding: utf-8

# <img width="800" src="fig/MalvasiaCabeciblanca-Cabecera.jpg"/>  
# [www.postdata-statistics.com](www.postdata-statistics.com)  
# **Curso de Introducción a la Estadística. Tutorial 2 (versión Python).**

# # Primer contacto con Python a través de Jupyter.
# 
# Este documento es un *cuaderno* de Jupyter (o IPython, que es como se llamaban las versiones previas). Eso significa que es un documento que combina párrafos de texto, como este que estás leyendo, con *bloques de código* en Python, como el que que aparece aquí debajo. Un cuaderno de Jupyter está estructurado en *celdas* (traducimos así el inglés *cells*) que, como hemos dicho, pueden contener texto o código. Cuando pinchas en una celda del cuaderno, esa celda es la *celda activa* y Jupyter lo indica rodeándola con un rectángulo. Prueba a hacer click ahora en esta misma frase para ver como aparece ese rectángulo.
# 
# **Atención:** si haces click dos veces, verás que la celda cambia de aspecto. No te preocupes, no puedes romper nada importante. Simplemente has accedido al *código fuente* de la celda, lo que te permite hacer modificaciones. Ese código es un lenguaje llamado *markdown*, sobre el que volveremos más adelante, Por el momento lo mejor es que dejes las cosas como estaban. Para conseguirlo, asegúrate de que el cursor está dentro de esta celda y pulsa a la vez las teclas Mayúsculas y Enter.
# 
# Como hemos dicho, este cuaderno contiene dos tipo de celdas:
# 
# + Las **celdas de código** se sistinguen porque van precedidas, a su izquierda, por la palabra `In`. La celda situada debajo de esta es una celda de código, por ejemplo.
# + Las **celdas de texto**, como esta, no tienen ningún texto a su izquierda.
# 
# Los cuadernos de Jupyter son documentos interactivos. Eso significa que puedes ejecutar directamente el código que contienen desde este mismo documento. Para comprobarlo, asegúrate de activar la siguiente celda de código (por ejemplo, haz clic en cualquier lugar de la celda) y pulsa a la vez Mayúsculas + Enter.

# In[1]:

2 + 3


# Si todo ha ido como se espera, habrás visto aparecer el resultado de esa operación debajo de la celda, precedido por la palabra `Out` y el número uno entre corchetes. Esos corchetes y números son la forma en la que Jupyter nos indica el orden en que ejecutamos las celdas de código. Prueba a ejecutar la celda otra vez y verás como ese número aumenta.
# 
# ## Python como calculadora.
# 
# En la primera celda hemos empezado a usar Python como una calculadora. Aparte de sumas podemos hacer, naturalmente, multiplicaciones y divisiones. Prueba a ejecutar las siguientes celdas: 

# In[ ]:

6 * 5


# In[ ]:

16 / 5


# El resultado de la división muestra la forma en la que Python escribe los decimales, con punto separando la parte entera y la parte decimal. Puesto que estamos usando la versión 3 de Python, el resultado de una divsión hecha con / es siempre un número decimal. Prueba la siguiente operación: 

# In[ ]:

16/4


# Si alguna vez tienes que usar la versión 2 de Python descubrirás que allí la división usando / es un poco más complicada. Por el momento, seguiremos adelante sin preocuparnos de esto. 
# 
# Vamos a elevar un número al cubo. En muchos lenguajes de programación las potencias se indican con el símbolo ^ (el acento circunflejo). Pero Python utiliza dos asteriscos: `**`. Prueba a ejecutar esta operación:

# In[ ]:

3**2


# ## División entera: resto y cociente.
# 
# En alguna ocasión tendremos necesidad de calcular el cociente y el resto de una división entera. Por ejemplo, para convertir un tiempo en segundos al formato minutos-segundos. En Python 3 el cociente se obtiene con `//` y el resto con `%`. Así, un experimento que dura 475 segundos, expresado en el formato minutos-segundos dura: 

# In[538]:

475 // 60


# In[539]:

475 % 60


# Es decir, que el experimento dura 55 minutos y 7 segundos.

# ## Algunos detalles de la interfaz de Jupyter.
# 
# 
# Ahora que ya has visto algunos ejemplos del funcionamiento de un cuaderno de Jupyter y antes de seguir adelante con nuestro trabajo, es preciso detenernos un momento en algunas cuestiones relativas al uso de estos cuadernos, para facilitar tu trabajo en lo que queda de curso. Para empezar con confianza, recuerda lo que te hemos dicho antes: no puedes romper nada demasiado importante. En el peor de los casos, si haces alguna operación que dañe este cuaderno y no sabes cómo deshacerlo, siempre puedes volver a la página del curso en [www.postdata-statistics.com](http://www.postdata-statistics.com), descargar una copia intacta del cuaderno, usarla para remplazar la copia dañada y volver al trabajo.
# 
# Lo primero que debes entender es que un cuaderno de Jupyter es un documento *vivo*. Nosotros te hemos proporcionado una versión inicial, pero cuando aprendas un poco más podrás modificarlo para añadir tus anotaciones y comentarios, hacer experimentos con el código, etc. Y también, si quieres, podrás empezar a crear tus propios cuadernos de Jupyter.
# 
# Vamos con algunas **nociones básicas**. Al principio esto parecerá complicado y si en una primera lectura te pierdes, no te preocupes. Déjalo para más adelante y sigue avanzando en el tutorial. Más adelante, cuando vayas ganado experiencia con los cuadernos de Jupyter podrás volver aquí y todo se irá aclarando: 
# 
# + Recuerda que hay dos tipos de celdas: de texto y de código.
# + Una celda, sea cual sea su tipo, puede estar en *modo edición* o en *modo comando*. Lo normal, al abrir un cuaderno de Jupyter es que todas las celdas estén en modo comando. Ese modo sirve para visualizar el cuaderno, pero también para manipular las celdas: borrarlas, cambiarlas de posición, añadir celdas nuevas, etc. 
# + Para pasar al modo edición puedes hacer doble clic en la celda que deseas editar. También puedes hacer que esa celda sea la celda activa (con un clic) y pulsar *Enter*. 
# + Para salir del modo edición y volver al modo comando pulsa *Esc*. Pero es importante entender que con eso no se ejecuta el contenido de la celda, ni se formatea la salida en el caso de una celda de texto. Si eso es lo que deseas, asegúrate de que esa es la celda activa y pulsa a la vez mayúsculas y *Enter*. 
# 
# Como hemos dicho, todo esto te parecerá ahora un embrollo considerable. Pero con un poco de paciencia y un bastante de práctica te acostumbrarás a las pequeñas extravagancias de la interfaz de Jupyter. Nosotros ya casi nos hemos acostumbrado. 
# 
# Hablando un poco más en serio, Jupyter es la mejor herramienta disponible, en este momento, para obtener este tipo de documentos que combinan texto y código. No es, ni mucho menos perfecta, y en otros lenguajes de programación hay ideas similares que nos gustan mucho más (como los documentos Rmarkdown para el lenguaje R). Pero en el mundo de Python, Jupyter es todavía la mejor opción: si te pudiéramos ofrecer algo mejor ya lo estaríamos haciendo.
# 
# Puedes explorar los menús de Jupyter para conocer algunas de las opciones disponibles. Por ejemplo el menú *Edit* te permite, en modo edición, hacer algunas de esas operaciones que hemos mencionado: mover celdas o borrarlas, insertar celdas nuevas, etc. Algunas de esas operaciones se pueden deshacer en caso de error, pero en cualquier caso sé prudente antes de modificar celdas si no te has asegurado de que dispones de una copia. Insistimos: los cuadernos origianles de los tutoriales siempre se pueden descargar otra vez desde la página del curso. Pero las posibles modificaciones que hayas introducido tú no están a salvo hasta que hagas una copia (menú *File* $\to$ *Make a Copy*) y guardes regularmente tu trabajo (menú *File* $\to$ *Save and Checkpoint*).
# 
# Por su lado el menú *Cell* te permite ejecutar una o varias celdas del cuaderno y cambiar el tipo de una celda, de texto a código o viceversa.   Por último el menú Help contiene por supuesto enlaces a documentación de ayuda (siempre en inglés), pero también una colección de *atajos de teclado* (keyboard shortcuts) que facilitan mucho el trabajo con Jupyter. Hay atajos para ambos modos, edición y comando, y al principio es fácil que te equivoques y uses un atajo de modo edición cuando en realidad estás en modo comando o al contrario. De nuevo, paciencia y práctica, que es como hemos aprendido todos. Para que puedas practicar te dejamos un ejercicio:

# ** Ejercicio:** 
# 
# Ejecuta con atención cada uno de estos pasos:
# 
# + Asegúrate de que está celda está activa (haz clic en ella) y de que estás en modo comando (pulsa mayúsculas + Enter). Vuelve a hacer clic en la celda si es preciso para activarla y asugúrate de que ves un rectángulo rodeando esta celda. 
# + Ahora que nos hemos asegurado del estado en el que se encuentra Jupyter, pulsa la tecla B (del inglés *below*, debajo) para añadir una celda nueva debajo de esta (si hubieras pulsado A, de *above* -arriba-, la celda nueva se añadiría encima de la celda activa). También podrías insertar esa celda usando el menú *Edit*, claro. 
# 
# + Haz clic en la zona de código (fondo gris) de la nueva celda para convertirla en la celda activa. ¿De qué tipo es? AL hacer clic en la zona de código de la celda habrás pasado automáticamente al modo edición. Puedes reconocerlo porque el cursor parpadea dentro de esa zona de código sombreada. 
# 
# + Escribe `2 + 3` dentro de la zona de código y después pulsa mayúsculas + *Enter* a la vez para ejecutarlo. Debería aparecer 5 como resultado debajo de la celda.
# 
# + Vuelve a hacer clic en la zona de código de la celda que contiene `2 + 3` y  pulsa *Esc* para pasar al modo comando (el cursor deja de parpadear). Ahora pulsa M. La celda ha pasado a ser una celda de texto y el resultado desaparece. Si ahora pulsas pulsa mayúsculas + *Enter* la celda pasa a modo comando y el texto 2 + 3 aparece como texto normal, sobre fondo blanco. 
# 
# 
# + De nuevo haz clic en esa celda para activarla. Si pulsas Y (siempre en modo comando) volverá a ser de código. Estos cambios entre texto y código afectan al formato del contenido pero son reversibles. 
# 
# + Para terminar el ejercicio asegúrate de estar en modo comando y con esa celda nueva como celda activa y pulsa D dos veces para borrar la celda. ¡Cuidado, no vayas a borrar otra celda por error! 
# 
#  
# <!--
# <font color="red">
# **PENDIENTE**
# </font>
# -->

# ## Funciones matemáticas y módulos de Python.
# 
# Aparte de las cuatro operaciones aritméticas básicas, las calculadoras científicas de mano incluyen funciones como la raíz cuadrada, logaritmos, funciones trigonométricas, etc. En Python, por supuesto, también podemos calcular esas funciones. Pero antes de hacerlo tenemos que aprender algo sobre el sistema de módulos de Python. 
# 
# Como todos los lenguajes de programación de *propósito general*, Python se puede utilizar para una gran cantidad de tareas distintas, cada una con sus necesidades específicas. Los programadores de Python han desarrollado muchísimas herramientas orientadas al cálculo científico, pero también a operaciones financieras, gestión de servidores web y sistemas, trabajo con bases de datos, etc. Si cada vez que usamos Python tuviéramos que instalar todo ese código estaríamos desperdiciando una enorme cantidad de recursos. Al fin y al cabo el usuario que quiere utilizar Python para Genómica no necesitará, seguramente, las funciones financieras más especializadas de Python. Por eso, como sucede en otros lenguajes, Python está organizado en una estructura modular, de manera que en cada momento podemos disponer de aquellas partes del código de Python que necesitamos. Concretamente, el código se organiza en **módulos** que puedes imaginar como cajas de herramientas y cuando queremos utilizar una herramienta concreta debemos indicárselo a Python pidiéndole que *importe* el módulo que contiene esa herramienta.   
# 
# Veamos un ejemplo. Muchas funciones matemáticas, como la raíz cuadrada y otras que mencionábamos antes, están guardadas en un módulo (caja de herramientas) llamado `math`. La función raíz cuadrada se llama `sqrt` (del inglés *square root*).  Para importar la función `sqrt` del módulo `math` en Python usamos este comando:

# In[12]:

from math import sqrt


# Esta frase es nuestra forma de decir, en lenguaje Python, *"saca la herramienta `sqrt` de la caja `math`"*. Una vez hecho esto, podemos usar la herramienta para, por ejemplo, calcular la ráiz cuadrada de 9 o cualquier otra. Compruébalo ejecutando estas dos operaciones:

# In[2]:

sqrt(9)


# In[3]:

sqrt(17)


# Como ves, la función se ejecuta o *invoca* colocando su argumento entre paréntesis. 
# 
# El módulo `math` contiene muchas otras funciones además de la raíz cuadrada. Por ejemplo, las funciones trigonométricas seno, coseno y tangete que se representan, respectivamente mediante `sin`, `cos` y `tan`. Por defecto, esas funciones asumen que los ángulos se miden en radianes. Por su parte, el logaritmo natural (o neperiano) de base $e$ se llama en Python `log` y la exponencial (para calcular $e$ elevado a un número) se llama  `exp`.
# 
# Pero, además de funciones, a menudo los módulos de Python contienen otro tipo de *objetos*. Por ejemplo, el módulo `math` contiene valores aproximados de las constantes matemáticas $\pi$ y $e$, entre otras. 
# 
# Recuerda que para usar estas herramientas las debemos empezar por importarlas. Para hacer más cómodo nuestro trabajo, podemos importar varias funciones de una vez:

# In[8]:

from math import sin, cos, tan, log, exp, pi, e


# Una vez hecho esto podemos empezar a usar las funciones. Por ejemplo, en trigonometría elemental hemos aprendido que:
# $$\sin\left(\dfrac{\pi}{4}\right) = \dfrac{\sqrt{2}}{2}\approx 0.7071$$
# Vamos a calcular con Python este número de dos formas:  

# In[10]:

sin(pi/4)


# In[13]:

sqrt(2)/2


# ¡Fíjate en que las últimas cifras son distintas! Eso nos debe servir de recordatorio de que los cálculos que estamos realizando son *aproximaciones numéricas*, no valores exactos.

# Enseguida vamos a seguir avanzando hacia la Estadística. Pero antes vamos a hacer un ejercicio y, tomando como punto de partida los resultados del ejercicio, nos detendremos un poco en algunos aspectos técnicos relacionados con el módulo `math` y el uso de funciones, aspectos que nos resultarán muy útiles más adelante.

# ** Ejercicio:** 
# Calcula los siguientes valores usando Python:
# 
# $
# \begin{array}{l}
# (a)\quad 2 + 3\\
# (b)\quad 15 - 7 \\
# (c)\quad 4 \cdot 6\\
# (d)\quad \dfrac{13}{5}\\
# (e)\quad \mbox{el cociente de $13$ entre $5$}\\
# (f)\quad 1 / 3 + 1 / 5\\
# (g)\quad \sqrt{25}\\
# (h)\quad \sqrt{26}\\
# (i)\quad \sin(\pi)\\
# (j)\quad \sin(3.14)\\
# (k)\quad \mbox{la tangente de }\pi/4\\
# (l)\quad \mbox{el logaritmo de 7}
# \end{array}
# $
# 
# <hr style="background:#FFAAAA; border:0; height:2px" />

# ### Notación científica.
# 
# El resultado del apartado *(i)* del ejercicio anterior es `1.2246467991473532e-16`.  La notación que se usa en la respuesta es la forma típica de traducir la *notación científica* a los lenguajes de ordenador y calculadoras. El símbolo `1.2246467991473532e-16` representa el número:
# $$1.2246467991473532\cdot 10^{-16},$$
# de manera que el número $-16$, que sigue a la letra `e` en esta representación, es el *exponente* de $10$ (también llamado *orden de magnitud*), mientras que el número $1.2246467991473532$ se denomina a veces *mantisa*. Puedes leer más sobre la notación científica en este artículo de la Wikipedia:
# 
# [Notación\_científica](http://es.wikipedia.org/wiki/Notación_científica)
# 
# En cualquier caso, el exponente $-16$ nos indica que se trata de un número extremadamente pequeño, muy cercano a $0$. Fíjate, en cambio, que si usas $3.14$ como aproximación de $\pi$, como hemos hecho en el apartado *(j)*, la respuesta, aunque pequeña, es todavía del orden de milésimas.

# ### Errores en Python.
# 
# Al trabajar con Python, como con cualquier otro lenguaje de programacion, la aparición de errores es inevitable. Así que es conveniente saber lo que ocurre cuando le pedimos a Python una operación para la que no tiene respuesta. Por ejemplo, ejecuta el siguiente código:

# In[ ]:

3 / 0


# Al hacerlo Python contesta un mensaje de error que contiene una descripción más o menos detallada del tipo de error que se ha producido, en este caso `ZeroDivisionError`, y del punto concreto donde ha ocurrido el error (lo cual será muy útil cuando empecemos a escribir fragmentos de código más largos).
#  
# Veamos otros ejemplos de errores en el siguiente ejercicio.

# ** Ejercicio:** 
# Ejecuta estos comandos de Python, que producirán distintos tipos de errores, y fíjate en esos errores:

# In[ ]:

log(-1)


# In[ ]:

4/*3


# In[ ]:

ln(7)


# <hr style="background:#FFAAAA; border:0; height:2px" />

# ### Ayuda con Python.
# 
# ¿Cómo se llaman las funciones de Python que calculan el arcotangente o el logaritmo en base 10? La respuesta a esta y a muchas otras preguntas está en Internet, y los buscadores son nuestros mejores aliados. Una expresión popular en los foros de Internet, desde hace años es: *"Google is your friend"*. Es decir que, si hacemos la pregunta correcta, a menudo la primera respuesta de un buscador contendrá la información necesaria. 
# 
# En cualquier caso, existen algunos recursos sobre Python que es bueno conocer. El principal de ellos es la página oficial del lenguaje, situada en:
# 
# [https://www.python.org/](https://www.python.org/)
# 
# y que contiene la documentación sobre los módulos oficiales con Python, tanto en la versión 2 como la 3. Por ejemplo, el módulo `math`, para la versión 3 de Python, está documentado en:
# 
# [https://docs.python.org/3/library/math.html](https://docs.python.org/3/library/math.html)
# 
# 

# ** Ejercicio:** 
# Busca la respuesta a la pregunta que hemos dejado pendiente: ¿cómo se llaman las funciones de Python que calculan el arcotangente o el logaritmo en base 10?  
# <hr style="background:#FFAAAA; border:0; height:2px" />

# ### Más formas de importar funciones.
# 
# Es posible que te estés preguntando: "¿si voy a usar muchas funciones matemáticas tengo que importarlas escribiendo uno a uno el nombre de cada una de ellas?". Para evitar eso, que más adelante resultaría muy incómodo, Python proporciona varias formas alternativas de importar funciones desde un módulo. 
# 
# En primer lugar, podemos decirle a Python que queremos importar *todas* las funciones de un módulo. Por ejemplo, para importar todas las funciones del módulo usaríamos:

# In[14]:

import math


# El módulo `math` contiene una función llamada `sinh`, que sirve para calcular el seno hiperbólico de un número (no te preocupes si no sabes lo que es, es sólo un ejemplo; si te pica la curiosidad puedes ver su definición [aquí](https://es.wikipedia.org/wiki/Seno_hiperbólico). La función seno hiperbólico cumple:
# $$\sinh(0) = 0$$
# Así que, dado que supuestamente  hemos importado todas las funciones del módulo `math`, deberíamos poder ejecutar este código y obtener 0 como respuesta (al menos aproximadamente) :

# In[ ]:

sinh(0)


# Sin embargo si ejecutas ese código verás que Python te espeta un mensaje de error inesperado, en el que dice que:
# 
# `name 'sinh' is not defined`
# 
# ¿Cómo es posible? Esto se debe a que la comodidad de importar todas las funciones del módulo `math` a la vez tiene un precio. Al usar `import math` Python en efecto ha importado todas las funciones, pero para saber de qué módulo proceden ha añadido el prefijo `math` seguido de un punto al nombre de cada una de esas funciones. Así que la forma correcta de usar la función es:

# In[16]:

math.sinh(0)


# Prueba a ejecutar esta versión de la función y verás que ahora no hay errores y el resultado es el esperado.
# 
# ### Importar módulos sin prefijo. Posibles conflictos de nombre.
# 
# Es posible que pienses que, puestas así las cosas, no hemos ganado mucho importando todas las funciones de `math` a la vez. La supuesta comodidad queda en parte eclipsada por la necesidad de escribir ese prefijo `math` delante de cada aparición de una función del módulo. 
# 
# Creemos que es conveniente que comprendas el problema que se plantea para los desarrolladores de Python, y el compromiso que han tenido que adoptar para evitar errores imprevisibles: pronto vamos a aprender a escribir nuestras propias funciones. Y estos prefijos son necesarios para evitar conflictos entre funciones de distintos módulos que tienen el mismo nombre.
# 
# En cualquier caso, cuando estamos muy seguros de lo que hacemos podemos usar una forma distinta de importación:

# In[17]:

from math import *


# Esta forma de importar te recordará a la primera que hemos visto, pero ahora el asterisco juega el papel de *comodín*, de manera que lo que estamos diciéndole a Python es que importe todas las funciones del módulo `math`, usando directamente los nombres de esas funciones, sin prefijos. Ahora puedes probar a ejecutar directamente:

# In[18]:

sinh(0)


# #### Números complejos como ejemplo de conflicto de nombres.
# 
# Los conflictos de nombre a los que hemos aludido antes no son un fenómeno raro. Para que veas un ejemplo sencillo vamos a usar otro módulo de Python llamado `cmath` que contiene funciones para trabajar con números complejos. Podrías cargar todas las funciones de ese módulo como hemos hecho con las de `math`.

# In[19]:

from cmath import *


# Y ahora, supongamos que quieres volver a calcular la misma raíz cuadrada que vimos como primer ejemplo: 

# In[20]:

sqrt(9)


# -
# 

# ** Ejercicio:**  
# 
# Vamos a comprobar el hecho de que el último módulo importado reemplaza a las anteriores funciones del mismo nombre. Vuelve a importar `math` usando el método del asterisco y repite el cálculo de $\sqrt{9}$. ¿Qué sucede ahora?
# <hr style="background:#FFAAAA; border:0; height:2px" />

# Como ilustra este ejemplo, la opción de importar las funciones de un módulo usando el asterisco es a menudo demasiado arriesgada y puede producir errores difíciles de diagnosticar cuando el código en Python sea más complejo que los ejemplos básicos que estamos viendo. Por esa razón usar el asterisco para importar se considera una *mala práctica* al programar en Python. ¡No lo hagas! Y por si te lo has preguntado, ocurre algo análogo si usas:
# ```
# from math import sqrt
# ```
# y después 
# ```
# from cmath import sqrt
# ```
# La segunda función importada reemplaza a la anterior. Tenemos que resignarnos, por tanto, a utilizar los prefijos de los módulos. Es decir que tenemos que hacer:

# In[22]:

import math


# Y ahora usar la función raíz cuadrada mediante:

# In[23]:

math.sqrt(9)


# Si queremos usar la raíz cuadrada de un número complejo hacemos:

# In[24]:

import cmath


# y ahora podemos calcular con:

# In[25]:

cmath.sqrt(9)


# Esto no afecta a la otra función `sqrt`, la de `math`, que sigue funcionando sin problemas:

# In[26]:

math.sqrt(25)


# Esta forma de trabajar elimina los conflictos de nombre entre módulos, pero puede resultar especialmente molesto con módulos de nombres largos. Por ejemplo, un poco más abajo aprenderemos a usar el módulo `matplotlib` para dibujar algunas gráficas. Sería bastante molesto tener que escribir el prefijo `matplotlib` cada vez que queremos usar una función de ese módulo. Para aliviar al menos parcialmente esa incomodidad Python nos permite usar un *alias*, normalmente una abreviatura, para importar un módulo. Por ejemplo, para importar `matplotlib` usaríamos:
# 
# ```
# import matplotlib as mp
# ```
# 
# y entonces en lugar de usar `matplotlib` como prefijo para las funciones de ese módulo basta con usar `mp`. Aunque `math` y `cmath` son nombres de módulo relativamente cortos, vamos a usar alias aún más cortos para que nos sirvan de ejemplo de cómo funciona esta idea:

# In[27]:

import math as m
import cmath as c


# Y ahora usamos las funciones raíz cuadrada de cada módulo mediante estos alias:

# In[28]:

m.sqrt(9)


# In[29]:

c.sqrt(9)


# Como ves, de esta forma el esfuerzo necesario para evitar conflictos es considerablemente menor.

# ###  Borrando la memoria de un cuaderno de Python.
# 
# Al llegar a a este punto hemos importado los módulos `math` y `cmath` de tantas maneras que es difícil seguirles el rastro. Y eso, al igual que ocurría con los conflictos de nombre, puede causarnos problemas en el resto del cuaderno. A veces, al trabajar en un cuaderno de Jupyter, te encontrarás en una situación como esta en la que quieres hacer *tabla rasa* y pedirle a Python que olvide todos los pasos previos para poder empezar a trabajar sin preocuparte de ese tipo de conflictos. Afortunadamente, existe un mecanismo para hacer esto. Basta con escribir 
# ```
# %reset
# ```
# en una celda de código y ejecutarlo. Al hacerlo, Jupyter nos pedirá que confirmemos esa decisión. Al fin y al cabo, estaremos borrando todos los *resultados* del código que hayamos ejecutado hasta ese momento. **Es importante entender esto:** no borramos ni el código que hemos escrito, ni desde luego las celdas de texto como esta. Lo único que desaparece son los resultados de ejecutar el código del cuaderno hasta ese momento. ¡Qué no es poco a veces! Algunos cuadernos que hemos escrito tardan horas en ejecutarse, y en ese caso hacer un reset puede suponer perder todo ese trabajo. Asegúrate siempre de que realmente quieres hacer esto.
# 
# Una vez hechas las advertencias pertinentes, adelante. Hagamos un reset en la celda situada justo aquí debajo.

# In[2]:

get_ipython().magic('reset')


# ** Ejercicio:**  
# 
# Para comprobar que, en efecto, hemos deshecho el trabajo previo, prueba a ejecutar el siguiente módulo de código. Deberías obtener un mensaje de error como prueba de que Python ha olvidado nuestras andanzas hasta ahora: 
# <hr style="background:#FFAAAA; border:0; height:2px" />
# 

# In[ ]:

m.sqrt(9)


# # Variables.

# En la sección previa hemos usado Python como una calculadora. Pero, para ir más allá, tenemos que disponer de *estructuras de datos*. Ese término describe, en Computación, las herramientas que nos permiten almacenar y procesar información. Las estructuras de datos más básicas de Python son las *variables* y las *listas*. En próximos tutoriales nos iremos encontrando con otras estructuras de datos: conjuntos, diccionarios, tuplas, matrices, dataframes, entre otras.
# 
# ## Variables en Python.
# 
# Una *variable* en Python es un símbolo o nombre que usamos para referirnos a un objeto. Por ejemplo, si ejecutas este código:

# In[5]:

a = 2


# entonces, aunque aparentemente no ha sucedido nada (porque no hay respuesta), a partir de ese momento Python ha asignado el valor 2 al símbolo {\tt a}. Así que si, por ejemplo, ejecutas

# In[6]:

a + 1


# obtendrás como respuesta $3$.

# **Ejercicio:**
# 
# ¿Cuánto valen las variables a, b y c al ejecutar estos comandos uno tras otro? Haz una tabla con tres columnas tituladas a, b y c y anota el valor de las variables en cada paso.

# In[ ]:

a = 2
b = 3
c = a + b
a = b * c
b = (c - a)^2
c = a * b


# Como has podido ver, al ejecutar esas asignaciones Python no produce ningún valor como resultado. ¿Se te ocurre alguna forma de comprobar los resultados que has escrito en la tabla?
# <hr style="background:#FFAAAA; border:0; height:2px" />

# ### Variables de tipo cadena de caracteres.
# 
# En el Capítulo 1 del libro hemos hablado de variables cualitativas y cuantitativas. Estas últimas toman siempre valores numéricos, y las variables de Python sirven, desde luego, para almacenar esa clase de valores. Pero, como iremos viendo en sucesivos tutoriales,  también se pueden utilizar variables de Python para guardar valores de variables cualitativas (factores), y  otros tipos de objetos que iremos conociendo a lo largo del curso. De momento, para que veas a que nos referimos, recordaremos el Ejemplo \ref{curso-cap01:ejem:VariableCualitativaOrdenada} del libro (pág. \pageref{curso-cap01:ejem:VariableCualitativaOrdenada}), en el que teníamos una variable cualitativa ordenada que representa el pronóstico de un paciente que ingresa en un hospital. Prueba a ejecutar este código:

# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# # Listas.

# In[ ]:

edades = [22, 21, 18, 19, 17, 21, 18, 20, 17, 18, 17, 22, 20, 19, 18, 19, 18, 22, 20, 19]


# In[ ]:




# ## Selección de elementos dentro de una lista.

# In[ ]:




# ## Listas a medida.

# In[ ]:

list(range(10))


# In[ ]:

list(range(2, 15))


# In[ ]:

list(range(2, 15, 3))


# In[ ]:

list(range(15, 2))


# In[ ]:

list(range(15, 2, -3))


# In[ ]:

# list(range(2, 5, 0.3))


# In[ ]:

list(np.arange(2, 5, 0.3))


# In[ ]:




# In[ ]:




# In[ ]:

valores = [1, 2, 3, 4, 5]


# In[ ]:

print(np.repeat(valores, 3))


# In[ ]:




# In[ ]:




# In[ ]:

print(np.repeat(valores, [2, 9, 1, 4, 3]))


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# ## Ordenación de una lista.

# In[ ]:

print(sorted(edades))


# In[ ]:

print(sorted(edades, reverse=True))


# ### Ordenación *in situ*.

# In[ ]:

edades_copia = list(edades)
print(edades_copia)


# In[ ]:

edades_copia.sort()
print(edades)
print(edades_copia)


# ## Operaciones sobre todos los elementos de una lista. 

# In[ ]:




# ### Bucles for.

# In[ ]:




# ### Otra forma de hacerlo: comprensión de listas . 

# In[ ]:

edadesCuadrado = [edad**2 for edad in edades]
print(edadesCuadrado)


# ### Y todavía una forma más: Numpy y aritmética vectorial.

# In[ ]:




# In[ ]:

import numpy as np
edades_np = np.array(edades)
edades_np


# In[ ]:

edades_np + 1


# In[ ]:

edades_np**2


# In[ ]:




# # Ficheros `csv` con Python.

# ## Leyendo datos de un fichero csv.

# In[ ]:

from pandas import read_csv


# In[ ]:

vectorEdades = read_csv("../datos/Tut02-Edades.csv", names=["v"])
vectorEdades = vectorEdades["v"].tolist()
print(vectorEdades)


# ### Otro formato del fichero de datos.

# In[ ]:

from numpy import genfromtxt
vectorEdades2 = genfromtxt("../datos/Tut02-Edades2.csv", delimiter=',', dtype='int')
print(vectorEdades2.tolist())


# ## Escribiendo datos a un fichero csv.

# In[ ]:

import csv
datos = list(range(1, 51))
print(datos)
with open('csvdeprueba.csv', 'w', newline='\n') as file:
    writer = csv.writer(file, lineterminator='\n')
    for dato in datos:
        writer.writerow([dato])


# In[ ]:

import csv
datos = list(range(1, 51))
print(datos)
with open('csvdeprueba2.csv', 'w', newline='') as file:
    writer = csv.writer(file, lineterminator='\n')
    writer.writerow(datos)
    


# In[ ]:




# # Estadística descriptiva de una variable cuantitativa, datos no agrupados.

# ### Lectura del fichero de datos.

# In[ ]:

var3 = read_csv("../datos/Tut02-var3.csv", names=["v"])
var3 = var3["v"].tolist()
print(var3)


# ## Recorrido de una lista de números.  

# In[ ]:

min(var3)


# In[ ]:

max(var3)


# In[ ]:

np.ptp(var3) # max - min (peak to peak)


# ## Tablas de frecuencia.

# In[ ]:

from collections import Counter
var3_counter = Counter(var3)
freqVar3 = var3_counter.most_common()
print(freqVar3)


# In[ ]:

sorted(freqVar3)


# ## Gráficos.

# In[ ]:

get_ipython().magic('matplotlib inline')


# In[ ]:

import matplotlib.pyplot as plt
bpVar3 = plt.boxplot(var3, patch_artist=True)
plt.setp(bpVar3['boxes'], facecolor='tan')  
plt.show()


# In[ ]:

posiciones = [item[0] for item in sorted(freqVar3)]
print(posiciones)
alturas = [item[1] for item in sorted(freqVar3)]
print(alturas)
plt.bar(posiciones, alturas, align='center', color='tan')
plt.show()


# In[ ]:

plt.hist(var3, bins=15, color='tan')
plt.show()


# In[ ]:




# ## Media aritmética.

# In[ ]:

len(var3)


# In[ ]:

sum(var3)


# In[ ]:

mediaVar3 = sum(var3) / len(var3)
print(mediaVar3)


# ### Con NumPy.

# In[ ]:

np.mean(var3)


# ## Varianza y desviación típica (poblacional y muestral).

# ### Varianza Poblacional.

# In[ ]:

varPoblacional = sum([(valor - mediaVar3)**2 for valor in var3]) / len(var3)
print(varPoblacional)


# ### Varianza muestral.

# In[ ]:

varMuestral = sum([(valor - mediaVar3)**2 for valor in var3]) / (len(var3) - 1)
print(varMuestral)


# ### Desviación típica poblacional.

# In[ ]:

from math import sqrt
desvestPoblacional = sqrt(varPoblacional)
print(desvestPoblacional)


# ### Desviación típica muestral.

# In[ ]:

desvestMuestral = sqrt(varMuestral)
print(desvestMuestral)


# ### Con NumPy.

# In[ ]:

np.var(var3, ddof=1)


# In[ ]:

np.var(var3, ddof=0)


# In[ ]:

np.var(var3)


# In[ ]:

np.std(var3, ddof=1)


# In[ ]:

np.std(var3)


# ## Medidas de posición: mediana, cuartiles y percentiles. Rango intercuartílico.

# ## Mediana.

# In[ ]:

np.median(var3)


# ## Cuartiles y percentiles.

# In[ ]:

np.percentile(var3, 25)


# In[ ]:

list(np.percentile(var3, [0, 25, 50, 75, 100]))


# In[ ]:

IQR = np.percentile(var3, 75) - np.percentile(var3, 25)
print(IQR)


# In[ ]:




# # Ficheros de comandos Python. Comentarios.

# In[ ]:




# In[ ]:




# # Más operaciones con listas. 

# In[ ]:




# ## Números aleatorios.

# In[ ]:

import random
random.randint(1, 6)


# In[ ]:

dado100 = [random.randint(1, 6) for i in range(0, 100)]
print(dado100)


# In[ ]:

dado100_counter = Counter(dado100)
freqDado100 = dado100_counter.most_common()
sorted(freqDado100)


# In[ ]:

print(edades)
print(freqEdades)
import numpy
numpy.random.choice(edades, size=100, replace=True, p=None)


# In[ ]:

numpy.random.choice(edades, size=100, replace=True, p=None)


# In[ ]:

numpy.random.choice(edades, size=100, replace=True, p=None)


# In[ ]:

numpy.random.seed(seed=2016)
numpy.random.choice(edades, size=100, replace=True, p=None)


# In[ ]:

numpy.random.seed(seed=2016)
numpy.random.choice(edades, size=100, replace=True, p=None)


# ## Conjuntos.

# In[ ]:

set(edades)


# In[ ]:

datos = numpy.random.choice(range(1,100), size=100, replace=True, p=None)
print(sorted(datos))


# In[ ]:

print(set(datos))


# In[ ]:

import statistics as st
np.percentile(a, 25)


# In[ ]:




# ## Listas de cadenas de texto. 

# In[ ]:

list('hello')


# In[ ]:

import string
string.ascii_lowercase
string.ascii_uppercase
string.ascii_letters


# In[ ]:

numpy.random.seed(seed=2016)
letras = list(numpy.random.choice(list(string.ascii_lowercase), size=10, replace=True, p=None))
print(letras)


# In[ ]:

print(sorted(letras))


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# # Valores booleanos y condiciones.

# In[ ]:




# ## El operador `==`.

# In[ ]:




# ## Interpretación de `True` y `False` como 1 y 0 respectivamente.

# In[ ]:

sum([True, True, False, True, False, True, False, False, False, False, True, True, True])


# ## Selección de elementos de una lista mediante condiciones.

# In[ ]:

print(dado100)


# In[543]:

numpy.random.seed(seed=2016)
mayoresQue3 = [valor for valor in dado100 if valor > 3]
print(mayoresQue3)


# # Ejercicios adicionales.

# ### Fracciones.
# 
# Cuando hemos usado Python como calculadora es posible que hayas pensado *"muchas calculadoras de mano permiten operar con fracciones"*. Bueno, pues para tu tranquilidad, Python también. Con más precisión, el módulo `fractions` lo permite. Aparte de mostrarnos que Python es una calculadora potente, este módulo nos será de mucha utilidad en el Tutorial03, cuando al tratar el calculo de probabilidades tendremos necesidad de hacer mucha soperaciones con fracciones.
# 
# Tu tarea en este ejercicio consiste en buscar información sobre ese módulo. Después impórtalo y úsalo para calcular estas operaciones:
# 
#  (a) $\quad\dfrac{3}{7} + \dfrac{11}{5}$  
#  
#  (b) $\quad \dfrac{2}{5} \cdot \dfrac{15}{8}$  
#  
#  (c) $\quad \dfrac{\dfrac{2}{5} \cdot \dfrac{1}{8}}{\dfrac{1}{3} \cdot \dfrac{4}{7} + \dfrac{3}{13} \cdot \dfrac{11}{21}}$  
#  
# Para que no pienses que exageramos, la última de estas operaciones es muy representativa del tipo de cálculos que haremos al estudiar la Regla de Bayes en el cálculo de probabilidades.
# <hr style="background:#FFAAAA; border:0; height:2px" />
# 

# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



