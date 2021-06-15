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

Tenga en cuenta que este valor final a pagar corresponde al precio de cada producto por la
cantidad llevada menos el descuento otorgado, debe imprimir el rol y la cédula de cada cliente
y el código del producto llevado en el mensaje.

**Bonus:** Desarollar el caso que el usuario pueda llevar más de un item (puede comprar varios
productos, varias unidades)

Falta la explicación

## 2. Preguntas:
**A. Qué tipo de errores se presentaron o se pueden presentar con su implementación al problema?**

**R//** En nuestra implementación al problema en Python pudimos observar:

* Que al organizar los prints, de forma errónea, nos arrojaba múltiples respuestas innecesarias para nuestra solución.

* Organizar bien las listas para usarlas, ya que, si no se pedía el dato correcto, daba un error de operaciones entre string e int.

También se puede presentar problemas en esta implementación en otros usuarios en que desconozcan el código como los siguientes:

* Que escriban por accidentes letras donde van números o viceversa.

* No se pueda devolver o cancelar el producto.

* Escribir palabras sin mayúscula o de una forma que el sistema no detecte el descuento o ect.

**B. Que estrategias podría usar para solucionar estos errores?**

**R//** Las estrategias que se podrían usar para solucionar los dichos problemas anteriores serian:

* Que el cliente posea acompañamiento de alguna persona que conozca el código y le pueda colaborar en el proceso.

* Dejar más print con información extra que recalquen como ingresar los datos o de qué manera.

* También poder aplicar las “excepciones” para que permitan facilitar procesos en casos de errores en pantalla.
