---
output: pdf_document
---

# Tutorial 2. Estadística descriptiva con Python.

## Primeros pasos: Python como una calculadora

Para empezar a ganar algo de confianza con Python y con la interfaz que vamos a utilizar empezaremos utilizando Python como una calculadora. Para eso, empieza tecleando estas operaciones. Para ver el resultado debes situar el cursos del ratón en la línea correspondiente de este documento y pulsar a la vez las teclas de mayúsculas y Enter. 


```python
3 * 2
```

Las potencias, como $3^2$, se expresan en Python con dos asteriscos.


```python
3**2
```

### Raíces cuadradas. Importando funciones de un módulo.

Para calcular una raíz cuadrada podemos, desde luego, hacer algo como
$$\sqrt{9} = 9^{1/2}$$


```python
9**0.5
```

Pero también podemos usar nuestra primera función de Python, la función `sqrt` (del inglés *square root*). Para usarla, como sucede con las otras funciones que veremos, el primer paso es *importarla* desde el módulo `math`. Puedes pensar en el módulo como una colección de funciones empaquetadas todas juntas, y normalmente dedicadas a tareas relacionadas entre sí. La forma de importar la función `sqrt` de ese módulo es esta:


```python
from math import sqrt
```

Y ahora ya podemos usarla:


```python
sqrt(9)
```

El resultado es, desde luego, el mismo que antes. El verdadero potencial de `math` queda de manifiesto cuando empezamos a pensar en funciones más complicadas, como las funciones trigonométricas. Por ejemplo, para usar las funciones seno (en inglés *sin*), coseno y tangente las importamos todas de `math` con un único comando:


```python
from math import sin, cos, tan
```

Sabemos que $\sin(\pi)=0$ y que $\pi\approx 3.141592$. Así que podemos hacer un primer ensayo con la función seno así:


```python
sin(3.141592)
```

El resultado aparece expresado en la notación exponencial, típica de Python y de muchos otros lenguajes computacionales. La letra `e` que aparece aquí procede de exponente. Y en realidad la respuesta de Python es equivalente a 
$$6.535897930762419\cdot 10^{-07}$$
Es decir, aproximadamente $0.0000006536$, un número bastante próximo a $0$ como cabía esperar, dada la aproximación a $\pi$ que hemos usado. El módulo `math` de Python incluye una aproximación a $\pi$ bastante más precisa que podemos importar como hemos hecho con las otras funciones:


```python
from math import pi
```

Para ver el valor podemos escribir simplemente el nombre:


```python
pi
```




    3.141592653589793



Y ahora podemos comprobar que esa aproximación produce un resultado bastante más próximo a cero que el anterior.


```python
sin(pi)
```




    1.2246467991473532e-16



### Ejercicio 1.

**Nota preliminar:** Abre un notebook de IPython diferente de este (en el menú `File` $\to$ `New Notebook` $\to$ `Python 3`) para trabajar en este ejercicio. En el futuro está será nuestra forma habitual de trabajar en los ejercicios de este y los próximos tutoriales. Al principio te lo recordaremos, pero progresivamente iremos dejando de hacerlo.

Trata de adivinar, antes de hacer nada con el ordenador, el resultado que produce cada una de las siguientes operaciones:

`2 + 3`



```python

```
