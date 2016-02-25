
# coding: utf-8

# # Tutorial 2. Estadística descriptiva con Python.

# ## Primeros pasos: Python como una calculadora

# Para empezar a ganar algo de confianza con Python y con la interfaz que vamos a utilizar empezaremos utilizando Python como una calculadora. Para eso, empieza tecleando estas operaciones. Para ver el resultado debes situar el cursos del ratón en la línea correspondiente de este documento y pulsar a la vez las teclas de mayúsculas y Enter. 

# In[ ]:

3 * 2


# Las potencias, como $3^2$, se expresan en Python con dos asteriscos.

# In[ ]:

3**2


# ### Raíces cuadradas. Importando funciones de un módulo.

# Para calcular una raíz cuadrada podemos, desde luego, hacer algo como
# $$\sqrt{9} = 9^{1/2}$$

# In[ ]:

9**0.5


# Pero también podemos usar nuestra primera función de Python, la función `sqrt` (del inglés *square root*). Para usarla, como sucede con las otras funciones que veremos, el primer paso es *importarla* desde el módulo `math`. Puedes pensar en el módulo como una colección de funciones empaquetadas todas juntas, y normalmente dedicadas a tareas relacionadas entre sí. La forma de importar la función `sqrt` de ese módulo es esta:

# In[ ]:

from math import sqrt


# Y ahora ya podemos usarla:

# In[ ]:

sqrt(9)


# El resultado es, desde luego, el mismo que antes. 
# 
# #### Funciones trigonométricas, exponenciales y logaritmos.
# 
# El verdadero potencial de `math` queda de manifiesto cuando empezamos a pensar en funciones más complicadas, como las funciones trigonométricas. Por ejemplo, para usar las funciones seno (en inglés *sin*), coseno y tangente las importamos todas de `math` con un único comando:

# In[ ]:

from math import sin, cos, tan


# Sabemos que $\sin(\pi)=0$ y que $\pi\approx 3.141592$. Así que podemos hacer un primer ensayo con la función seno así:

# In[ ]:

sin(3.141592)


# El resultado aparece expresado en la notación exponencial, típica de Python y de muchos otros lenguajes computacionales. La letra `e` que aparece aquí procede de exponente. Y en realidad la respuesta de Python es equivalente a 
# $$6.535897930762419\cdot 10^{-07}$$
# Es decir, aproximadamente $0.0000006536$, un número bastante próximo a $0$ como cabía esperar, dada la aproximación a $\pi$ que hemos usado. El módulo `math` de Python incluye una aproximación a $\pi$ bastante más precisa que podemos importar como hemos hecho con las otras funciones:

# In[5]:

from math import pi


# Para ver el valor podemos escribir simplemente el nombre:

# In[7]:

pi


# In[16]:

print("{0:.40f}".format(pi))


# Y ahora podemos comprobar que esa aproximación produce un resultado bastante más próximo a cero que el anterior.

# In[20]:

sin(pi)


# De todas formas, no queremos dejar de mencionar que las aproximaciones de $\pi$ que usa Python, como las de muchos otros lenguajes de programación, no son correctas más allá de las primeras 15 o a lo sumo 20 cifras decimales. Si se necesita más precisión (lo cual raramente sucede) se pueden usar programas especializados para este tipo de cálculos. Puesto que más adelante en estos tutoriales vamos a usar [Wolfram Alpha](http://www.wolframalpha.com/) para otras tareas, si quieres puedes ir echando un vistazo a este enlace:
# [http://www.wolframalpha.com/input/?i=pi](http://www.wolframalpha.com/input/?i=pi)
# 
# El módulo `math` también contiene la **función exponencial**  `exp`. Por ejemplo, para calcular 
# 
# $$e^3$$
# 
# en Python empezaríamos por importar la función (recuerda que basta con hacer esto una vez por sesión de trabajo o por programa):

# In[23]:

from math import exp


# y ahora haríamos 

# In[24]:

exp(3)


# De la misma forma, la función logaritmo neperiano (o logaritmo natural, de base $e$) es la función `log` del módulo `math`. 

# In[27]:

from math import log


# Y ahora poemos usarla para comprobar (dentro de la precisión de las aproximaciones numéricas de Python) que el logaritmo es la inversa de la exponencial.

# In[28]:

log(exp(5))


# #### Documentación del módulo `math`
# 
# En cualquier caso, si deseas ampliar la información sobre estas y otras funciones matemáticas que contiene el módulo `math`, puedes consultar la documentación del módulo en este enlace:
# 
# [https://docs.python.org/2/library/math.html](https://docs.python.org/2/library/math.html)
# 
# 
# #### Usando paréntesis para controlar el orden de las operaciones
# 
# Cuando Python se encuentra con un comando como este:
# 
# `1 / 3 + 1 / 5`
# 
# tiene que decidir cómo interpretarlo. Lo más probable es que nosotros, lectores humanos, al ver el código anterior hayamos pensado en que representa la operación:
# 
# $$\dfrac{1}{3} + \dfrac{1}{5}$$
# 
# Cuyo resultado es $\frac{8}{15}\approx 0.533$ Pero también podríamos estar representando esta otra operación:
# 
# $$\dfrac{1}{\left(\dfrac{3 + 1}{5}\right)}$$
# 
# cuyo resultado es $1.25$
# 
# Para evitar ese tipo de interpretaciones ambiguas, Python (y cualquier lenguaje de programación) utiliza una serie de *reglas de precedencia* que fijan el orden en que se realizan las operaciones que aparecen en una operación matemática. No queremos entrar en todos los detalles técnicos, que normalmente son innecesarios. Basta con tener una idea general: primero se evalúan de izquierda a derecha las funciones (como `sqrt`), después productos y divisiones y por último sumas y restas. La otra idea fundamental es que, en caso de duda, siempre puedes (y a menudo, debes) usar paréntesis para despejar la posible ambigüedad. Por ejemplo, estas dos expresiones:

# In[18]:

(1/3) + (1/5)


# In[17]:

1/((3 + 1)/5)


# contienen los mismos números y operaciones en el mismo orden (leídos de izquierda a derecha), pero mediante el uso de paréntesis conseguimos que Python las interprete de forma distinta.

# ### Ejercicio 1.

# **Nota preliminar:** Abre un notebook de IPython diferente de este (en el menú `File` $\to$ `New Notebook` $\to$ `Python 3`) para trabajar en este ejercicio. En el futuro está será nuestra forma habitual de trabajar en los ejercicios de este y los próximos tutoriales. Al principio te lo recordaremos, pero progresivamente iremos dejando de hacerlo.
# 
# Trata de adivinar, antes de hacer nada con el ordenador, el resultado que produce cada una de las siguientes operaciones:
# 
# 1.   `2 + 3 * 5`
# 2.   `15 / 3 + 7 * 2`
# 3.   `4 + 2 * 6 * 3 + 1`
# 4.   `12/4/2`

# ### Ejercicio 2.

# Es posible que a la vista de algunas de las operaciones anteriores hayas pensado ''mi calculadora sabe trabajar con fracciones...'' No te preocupes: Python también. Primero calcula a mano el resultado de:
# $$\dfrac{3}{4} + \dfrac{7}{15}$$
# Y luego prueba a ejecutar estos comandos (recuerda usar otro notebook):

# In[10]:

from fractions import Fraction


# In[35]:

Fraction(3, 4) + Fraction(7, 15)


# In[37]:

Fraction(3, 5)/7


# Más adelante en estos tutoriales aprenderemos otras formas de trabajar en Python con fracciones o con objetos matemáticos más complicados. 

# ## Variables y vectores.
# 
# 
# En la sección previa hemos usado Python como una calculadora. Pero, para ir más allá, tenemos que disponer de estructuras de datos. Ese término
# describe, en Computación, las herramientas que nos permiten almacenar y procesar información. Las estructuras de datos más básicas de Python son las variables y las listas. En esta sección vamos a emepzar el trabajo con esas dos estructuras. En próximos tutoriales nos iremos encontrando con otras estructuras de datos más complicadas.
# 
# Puedes pensar en una **variable de Python** como si fuera una caja que guarda en su interior un valor. Y además la caja lleva un rótulo o etiqueta que identifica a esa caja en particular. Por ejemplo, para guardar el valor 2 en una variable (caja) llamada `x` hacemos

# In[42]:

x = 2


# Lo que acabamos de hacer es una *asignación*. Decimos que hemos *asignado* el valor 2 a la variable `x`. Para preguntarle a Python por el valor de una variable (piensa en el contenido de la caja) basta con escribir el nombre de esa variable:

# In[43]:

x


# Y una vez almacenado el valor en la variable podemos usarlo en las operaciones de Python como si estuviéramos escribiendo directamente el valor:

# In[44]:

x + 3


# In[45]:

x**3


# Hemos llamado `x` a la primera variable que hemos usado. En Python podemos 

# In[46]:

x  = x + 4; print(x)


# In[ ]:




# In[ ]:




# In[ ]:




# Hemos guardado el valor 2 en la variable `x`. Si ahora escribimos una orden como esta:

# In[38]:

x = x + 3


# entonces Python la interpretará así: tomamos el valor 2 que hay en x, sumamos 3 a ese valor para obtener 5 y entonces guardamos ese valor en la propia variable x. 

# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# ## Ficheros csv

# ## Estadística descriptiva de una variable cuantitativa, con datos no agrupados.

# ## Ficheros de comandos Python y comentarios

# ## Más operaciones con vectores

# ## Ejercicios adicionales

# In[ ]:



