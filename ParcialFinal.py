###Miguel Angel Nivia O(8958691) y Julio Mazo Reyes(8962011)
###Parcial Final

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
