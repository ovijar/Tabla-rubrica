def saludo():
    print("BIENVENIDO A LA TABLA RUBRICA")
    print("= * = *"*10)


def rubrica():
    numero = float(input("¿Que puntaje desea calcular?\n"))
    base = int(input("¿En base a?\n"))
    resultado = numero/base * 4 + 1
    resultado = (round(resultado, 1))
    print(f'El puntaje de ' + str(numero) +
          '\nSu calificacion es = ' + str(resultado))


if __name__ == "__main__":
    saludo()
    rubrica()

"""
UNA TABLA PARA EVALUAR LOS ESTUDIANTE MEDIANTE PUNTAJES OBTENIDOS EN LAS PRUEBAS
EN ESTA SE INGRESA LOS PUNTOS GANADOS EN LA PRUEBA
Y DESPUES SE AGREGA LA BASE DEL PUNTAJE QUE ASIGNA CADA EDUCADOR 
SEGUN SU CRITERIO, POR EJEMPLO: 10 PUNTOS ES LA BASE DEL EXAMEN
COMO RESULTADO SE LA CALIFICACION REDONDEADA A UN DECIMAL.
"""
