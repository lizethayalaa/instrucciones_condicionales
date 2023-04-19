# instrucciones_condicionales
conceptos básicos de las instrucciones condicionales y de repetición en el lenguaje de programación Python.

En Python, las instrucciones condicionales y de repetición son fundamentales para controlar el flujo de ejecución del programa. A continuación se describen brevemente los conceptos básicos de estas instrucciones:

Instrucciones condicionales:

Las instrucciones condicionales permiten ejecutar ciertas líneas de código solo si se cumple una determinada condición. En Python, la instrucción condicional se escribe con la palabra clave if, seguida de una expresión booleana (que se evalúa como verdadera o falsa) y dos puntos. A continuación, se especifican las líneas de código que se ejecutan si la condición es verdadera, indentándolas con cuatro espacios. Por ejemplo:

python
Copy code
if x > 0:
    print("x es positivo")
En este caso, si la variable x es mayor que cero, se imprimirá en la pantalla el mensaje "x es positivo".

Es posible agregar más condiciones usando la palabra clave elif (abreviatura de "else if"). Si se usa la palabra clave else, se especifican las líneas de código que se ejecutan si ninguna de las condiciones anteriores es verdadera. Por ejemplo:

python
Copy code
if x > 0:
    print("x es positivo")
elif x < 0:
    print("x es negativo")
else:
    print("x es cero")
En este caso, si x es mayor que cero, se imprimirá el mensaje "x es positivo". Si x es menor que cero, se imprimirá "x es negativo". Si ninguna de estas condiciones es verdadera, se imprimirá "x es cero".

Instrucciones de repetición:

Las instrucciones de repetición permiten ejecutar un bloque de código varias veces, ya sea un número fijo de veces o hasta que se cumpla una determinada condición. En Python, las instrucciones de repetición son while y for.

La instrucción while repite un bloque de código mientras una determinada condición sea verdadera. La sintaxis es similar a la instrucción if, pero la palabra clave es while en lugar de if. Por ejemplo:

python
Copy code
i = 0
while i < 10:
    print(i)
    i += 1
En este caso, se imprimirán los números del 0 al 9, ya que el bloque de código se repite mientras i sea menor que 10.

La instrucción for permite iterar sobre una secuencia (por ejemplo, una lista o una cadena de texto) y ejecutar un bloque de código para cada elemento de la secuencia. La sintaxis es la siguiente:

python
Copy code
for variable in secuencia:
    # bloque de código a ejecutar para cada elemento de la secuencia
Por ejemplo:

python
Copy code
frutas = ["manzana", "banana", "naranja"]
for fruta in frutas:
    print(fruta)
En este caso, se imprimirán los elementos de la lista frutas: "manzana", "banana" y "naranja".

Estos son solo los conceptos básicos de las instrucciones condicionales y de repetición en Python. Hay muchas más opciones y detalles para cada una de estas instrucciones, que pueden encontrarse en la documentación oficial de Python.





