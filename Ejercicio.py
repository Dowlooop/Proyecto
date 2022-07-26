from ast import Str
from cgi import print_arguments
from configparser import MAX_INTERPOLATION_DEPTH
from ctypes.wintypes import INT
from tkinter.messagebox import NO


print("==========================================================")
print("PROGRAMA PARA CALCULAR LOS PROMEDIOS DE LOS ESTUDIANTES")
print("==========================================================")


input("PRECIONA ENTER")

print("""      ++++++++++++++INSTRUCIONES++++++++++++++++
                        1)COLOCAR MATERIA
                        2)COLOCAR NOMBRE DE LOS ESTUDIANTES
                        3) COLCOAR PORCENTAJE DE LAS NOTAS DE LOS ESTUDIANTES
                        4)COLOCAR LA MAXIMA NOTA Y LA MANINA NOTA PARA APROBAR O REPROBAR
                        5)TERMINAR EL PROGRAMA""")

NOTAMX=int(input("CUAL ES LA NOTA MAXIMA: "))
NOTAMN=int(input("CUAL ES LA NOTA MINIMA"))
print(f"LA NOTA MAXIMA ES {NOTAMX} y la nota minima es {NOTAMN}")
input("PRECIONA ENTER")
MATERIA=str(input("QUE MATERIA DECEAS COLCOAR: "))
print(f"LA MATERIA QUE HAS ESCOJIDO ES {MATERIA}")
NOMBRE=str(input("CUAL ES EL NOMBRE DEL ESTUDIANTE: "))
print(f"TU NOMBRE ES {NOMBRE}")
NOTA=int(input("CUAL ES TU NOTA: "))
print(f"TU NOTA ES {NOTA}")

if NOTA > NOTAMN:
    print(f"FELICIDAES {NOMBRE} HAS APROBADO LA MATERIA DE {MATERIA}")
elif NOTA < NOTAMN:
    print(f"MAL HAS REPROBADO {NOMBRE} ESTA MATERIA NO SE TE DA ")
elif NOTA > NOTAMX:
    print("IMPOSIBLE XD ESA NOTA ES ERROR")
print("==========================================================")
print("FIN")

