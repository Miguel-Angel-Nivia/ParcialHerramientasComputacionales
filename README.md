# Parcial Herramientas Computacionales
Trabajo Final De Herramientas, epic.
> Julio Mazo Reyes (8962011) y Miguel Angel Nivia Ortega (8958691)

## 1. Ejercicios de Python (Cafeteria Jave):
**Contexto:** 

Para recuperarse un poco del tiempo en cuarentena, las cafeterias de la universidad se encuentran dando descuentos a la comunidad estudiantil y dependiendo si es estudiante o profesor, tienen descuentos diferentes. Se desea saber entonces por cada compra cuánto debe pagar el usuario en caja. Para ello:
* Pida por teclado la siguiente información para el cliente: cédula y rol: profesor o estudiante
* Registrar el producto a comprar: codigo producto, cantidad de unidades y precio del producto. (un solo producto, varias unidades, por ejemplo: producto 076: gaseosa, 3 unidades)
* Los descuentos estan dados de la siguiente forma: los estudiantes tienen un 50 % de descuento mientras que los profesores tienen un 20 % de descuento.

Al final el procedimiento por cada cliente deberá imprimir el valor a pagar por sus productos de la forma: 

*”El **Rol** con cedula **Numero**, debe pagar **Valor** por el producto **Codigo**”*

**Ejemplo:** 

*”El **profesor** con Cedula **1454898** debe pagar **$12.900** por el producto **076**”* 

Tenga en cuenta que este valor final a pagar corresponde al precio de cada producto por la cantidad llevada menos el descuento otorgado, debe imprimir el rol y la cédula de cada cliente y el código del producto llevado en el mensaje.

**Bonus:** Desarollar el caso que el usuario pueda llevar más de un item (puede comprar varios
productos, varias unidades)

*El archivo se encuentra en el repositorio como **A. Parcial Final.Py***

Este es el problema **#A** 

El archivo de este ejercicio fue realizado en el IDLE de Python el cual no recibe ningun dato de entrada para el ejercico, y como salida, retorna un texto con la información recolectada durante todo el código, siendo:

* El Rol De La Persona.   → (rol)
* La cedula De La Persona.→ (ced)
* El Valor Del Producto.  → (valor)
* El Codigo del producto. → (cod)

Como Lo Calcula?

Nuestro código se encarga de calcular el Precio Final A Pagar con toda la informacion anterior, por lo cual, primero se hizo un procedimiento que se encarga de imprimir los nombres de las comidas disponibles en la tienda pero directamente este procedimiento no se ejecuta aun. Posteriormente se realizó una función que no recibe ningun valor de entrada sino que da la bienvenida al usuario, recordandole los descuentos que hay que son del 50% para estudiantes y el 20% para profesores; y le pide los datos de la cédula y su rol **(Estudiante/Profesor)**, luego le pide al usuario la cantidad de productos a llevar, para luego pedirle el nombre específico de dicho producto una vez si solo es 1, pero varias veces si es mas de un alimentos, luego pregunta cuantas unidades va a llevar de dicho producto y verifica en una lista de alimentos si la comida esta, si es asi **ans** pasara de ser 0 a una **lista** de 2 elementos que contiene en la posición 0 el codigo y en la posición 1 el precio del alimento, pero si no esta el alimento ejecutara un error.

Despues de este proceso de preguntar información al usuario, realizara las operaciones necesarias dependiendo si la cantidad de productos y unidades es 1 o mas, y ademas realizara dos verificaciónes con if para saber si el rol era estudiante o profesor, dependiendo de esto ocurrira:

* Si es 1 en ambas y es estudiante, entonces el precio del valor sera multiplicado por 1/2 que seria la mitad del valor original.
* Si es 1 en ambas y es profesor, entonces se realiza un calculo adicional donde se hallara el descuento multiplicando el valor original con 1/5; para luego coger este descuento y restarle al valor original para obtener el valor con el descuento.
* Si es diferente en producto o unidad y es estudiante, entonces también se hara un proceso similiar de encontrar el descuento pero con el 1/2 y asi restarselo al valor original para hallar el valor con el descuento.
* Si es diferente en producto o unidad y es profesor, entonces también se hara un proceso similiar de encontrar el descuento pero con el 1/5 y asi restarselo al valor original para hallar el valor con el descuento.

Para finalizar se retorna la iformacion pertinente para dar a conocer el resultado al usuario.

Ejemplo:

*El estudiante con cedula 12323282 debe pagar $10000 por varios productos.*

## 2. Preguntas de errores y soluciones (Cafeteria Jave):

*El archivo se encuentra en el repositorio como **Parcial Final (Migue y Julio).docx***

Este es el problema **#B**

En este documento de word se respondio a las siguientes 2 preguntas:

1. Que tipo de errores se presentaron o se pueden presentar con su implementación a problema?
2. Que estrategias podr´ıa usar para solucionar estos errores?

Donde Respondimos de forma textual los problemas ocurridos durante el proceso de decodificación y sus posibles soluciones.
