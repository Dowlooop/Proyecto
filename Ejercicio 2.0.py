#ESTE ES UN PROGRAMA PARA VER COMO SE ALAMACENA DATOS

from statistics import variance


print(f"============================================================")
print("PROGRAMA PARA ALMACENAR Y ACEDER A DATOS DE MEMORIA")
print(f"============================================================")


variable=int(input("""     ======MENU======
                    1) AÑADIR DATOS 
                    2) ACEDER A DATOS EXITENTES
                    3) RESTEAR Y COLOCAR NUEVOS VALORES A TOMAR EN CUENTA
                    4) SALIR
                    
                    :
                    """))

bandera:YES
while bandera == YES:
    if variable == 1:
        DATOS=str(input("COLOCA EL NOMBRE: "))
        ALAMACENAR=DATOS
    