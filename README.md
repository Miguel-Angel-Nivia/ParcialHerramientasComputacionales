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

```python
def alimentos():
    print("Gaseosa")
    print("Pan")
    print("Perro")
    print("Pandebono")
    print("Empanada")
    print("Pizza")
    print("Agua")
    print("Jugo")
    print("Bombon")
    print("Helado")
    print("Chocolatina")
    print("Pastel")

def cafeteria():
    print("Bienvenido A La Cafeteria De La Universidad Javeriana Cali")
    print()
    print("Hay Descuentos del 50% En Estudiantes y un 20% En Profesores")
    print("Por favor Ingrese Los Siguientes Datos:")
    ced = int(input("Cedula: "))
    rol = str(input("rol(Estudiante/Profesor): "))
    print()
    print("Alimentos disponibles:")
    alimentos()
    print()
    cant = int(input("Cantidad De Productos: "))
    valor = 0
    ans = 0
    i = 0
    while i < cant:
        prod = str(input("Nombre De Alimento: "))
        if prod == "Gaseosa":
            ans = ["079", 1500]
        elif prod == "Pan":
            ans = ["040", 500]
        elif prod == "Perro":
            ans = ["080", 2000]
        elif prod == "Pandebono":
            ans = ["067", 1200]
        elif prod == "Empanada":
            ans = ["090", 1000]
        elif prod == "Pizza":
            ans = ["002", 1500]
        elif prod == "Agua":
            ans = ["001", 3000]
        elif prod == "Jugo":
            ans = ["010", 2700]
        elif prod == "Bombon":
            ans = ["013", 250]
        elif prod == "Helado":
            ans = ["099", 1500]
        elif prod == "Chocolatina":
            ans = ["076", 300]
        elif prod == "Pastel":
            ans = ["024", 1200]
        
        #print(ans[0], ans[1])
        uni = int(input("Cantidad De Unidades De Dicho Producto: "))
        acum = 0
        descuento = 0
        cod = ans[0]
        j = 0
        while j < uni:
            if uni == 1 and cant == 1:
                if rol == "estudiante" or rol == "Estudiante":
                    valor += (ans[1] * 1/2)
                elif rol == "Profesor" or rol == "profesor":
                    descuento = (ans[1] * 1/5)
                    valor += (ans[1] - descuento)
                return("El " + rol + " con cedula " + str(ced) + ", debe pagar $" + str(valor) + " por el producto " + str(cod) + ".")

            else:
                if rol == "estudiante" or rol == "Estudiante":
                    acum += cant * ans[1]
                    valor = (acum * 1/2)
                elif rol == "Profesor" or rol == "profesor":
                    acum += cant * ans[1]
                    descuento = (acum * 1/5)
                    valor = (acum - descuento)
            j += 1
        i += 1
    
    print()    
    return("El " + rol + " con cedula " + str(ced) + ", debe pagar $" + str(valor) + " por varios productos/unidades.")
    
print(cafeteria())
```

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
